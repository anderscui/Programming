#![warn(clippy::all)]

use std::net::Ipv4Addr;
use tracing_subscriber::fmt::format::FmtSpan;

use handle_errors::return_error;
use warp::{http::Method, Filter};

mod routes;
mod store;
mod types;

use crate::routes::answer::{add_answer, get_answers};
use crate::routes::question::{add_question, delete_question, get_questions, update_question};
use crate::store::Store;

#[tokio::main]
async fn main() {
    let log_filter = std::env::var("RUST_LOG")
        .unwrap_or_else(|_| "foundation=info,warp=info".to_owned());

    tracing_subscriber::fmt()
        // Use the filter we built above to determine which traces to record.
        .with_env_filter(log_filter)
        // Record an event when each span closes.
        // This can be used to time our routes' durations!
        .with_span_events(FmtSpan::CLOSE)
        .init();

    let store = Store::new();
    let store_filter = warp::any().map(move || store.clone());

    let cors = warp::cors()
        .allow_any_origin()
        .allow_header("content-type")
        .allow_methods(&[Method::PUT, Method::DELETE, Method::GET, Method::POST]);

    let get_q_items = warp::get()
        .and(warp::path("questions"))
        .and(warp::path::end())
        .and(warp::query())
        .and(store_filter.clone())
        .and_then(get_questions)
        .with(warp::trace(|info| {
            tracing::info_span!(
                "get_questions request",
                method = %info.method(),
                path = %info.path(),
                id = %uuid::Uuid::new_v4(),
            )
        }));

    let add_q_item = warp::post()
        .and(warp::path("questions"))
        .and(warp::path::end())
        .and(store_filter.clone())
        .and(warp::body::json())
        .and_then(add_question);

    let update_q_item = warp::put()
        .and(warp::path("questions"))
        .and(warp::path::param::<String>())
        .and(warp::path::end())
        .and(store_filter.clone())
        .and(warp::body::json())
        .and_then(update_question);

    let delete_q_item = warp::delete()
        .and(warp::path("questions"))
        .and(warp::path::param::<String>())
        .and(warp::path::end())
        .and(store_filter.clone())
        .and_then(delete_question);

    let get_a_items = warp::get()
        .and(warp::path("answers"))
        .and(warp::path::end())
        .and(warp::query())
        .and(store_filter.clone())
        .and_then(get_answers);

    let add_a_item = warp::post()
        .and(warp::path("answers"))
        .and(warp::path::end())
        .and(store_filter.clone())
        .and(warp::body::form())
        .and_then(add_answer);

    let routes = get_q_items
        .or(add_q_item)
        .or(update_q_item)
        .or(delete_q_item)
        .or(get_a_items)
        .or(add_a_item)
        .with(cors)
        .with(warp::trace::request())
        .recover(return_error);

    let ip: Ipv4Addr = "127.0.0.1".parse().expect("Please use a valid ip address.");
    let port = 3030;

    // curl http://localhost:3030
    // curl http://localhost:3030/questions
    warp::serve(routes).run((ip, port)).await;
}

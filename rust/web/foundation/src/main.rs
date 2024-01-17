use std::net::Ipv4Addr;

use warp::{Filter, http::Method};
use handle_errors::return_error;

mod store;
mod types;
mod routes;

use crate::store::Store;
use crate::routes::question::{get_questions, add_question, update_question, delete_question};
use crate::routes::answer::{get_answers, add_answer};

#[tokio::main]
async  fn main() {
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
        .and_then(get_questions);

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
        .recover(return_error);

    let ip: Ipv4Addr = "127.0.0.1".parse().expect("Please use a valid ip address.");
    let port = 3030;

    // curl http://localhost:3030
    // curl http://localhost:3030/questions
    warp::serve(routes)
        .run((ip, port))
        .await;
}
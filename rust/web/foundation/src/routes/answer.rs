use std::collections::HashMap;
use tracing::{event, instrument, Level};
use warp::http::StatusCode;
use warp::Rejection;

use crate::store::Store;
use crate::types::answer::{NewAnswer};
use crate::types::pagination::{extract_pagination, Pagination};

#[instrument]
pub async fn get_answers(
    params: HashMap<String, String>,
    store: Store,
) -> Result<impl warp::Reply, Rejection> {
    event!(target: "foundation", Level::INFO, "querying answers");

    let mut pagination = Pagination::default();
    if !params.is_empty() {
        event!(Level::INFO, pagination=true);
        pagination = extract_pagination(params)?;
    }

    match store
        .get_answers(pagination.limit, pagination.offset)
        .await {
        Ok(res) => Ok(warp::reply::json(&res)),
        Err(e) => {
            return Err(warp::reject::custom(e));
        },
    }
}

pub async fn add_answer(
    store: Store,
    new_answer: NewAnswer,
) -> Result<impl warp::Reply, Rejection> {
    match store.add_answer(new_answer).await {
        Ok(_) => Ok(warp::reply::with_status("Answer added", StatusCode::OK)),
        Err(e) => Err(warp::reject::custom(e)),
    }
}

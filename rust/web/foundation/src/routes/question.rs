use handle_errors::Error;
use std::collections::HashMap;
use tracing::{instrument, info};
use warp::http::StatusCode;
use warp::Rejection;

use crate::store::Store;
use crate::types::pagination::extract_pagination;
use crate::types::question::{Question, QuestionId};

#[instrument]
pub async fn get_questions(
    params: HashMap<String, String>,
    store: Store,
) -> Result<impl warp::Reply, Rejection> {
    info!("querying questions");

    if !params.is_empty() {
        let pagination = extract_pagination(params)?;
        info!("using pagination");
        let res: Vec<Question> = store.questions.read().await.values().cloned().collect();
        let res = if pagination.start > res.len() {
            // TODO: how to create an empty slice
            &res[res.len()..]
        } else if pagination.end > res.len() {
            &res[pagination.start..]
        } else {
            &res[pagination.start..pagination.end]
        };
        Ok(warp::reply::json(&res))
    } else {
        info!("no pagination used");
        let res: Vec<Question> = store.questions.read().await.values().cloned().collect();
        Ok(warp::reply::json(&res))
    }
}

pub async fn add_question(
    store: Store,
    question: Question,
) -> Result<impl warp::Reply, warp::Rejection> {
    store
        .questions
        .write()
        .await
        .insert(question.id.clone(), question);
    Ok(warp::reply::with_status("Question added", StatusCode::OK))
}

pub async fn update_question(
    id: String,
    store: Store,
    question: Question,
) -> Result<impl warp::Reply, warp::Rejection> {
    match store.questions.write().await.get_mut(&QuestionId(id)) {
        Some(q) => *q = question,
        None => return Err(warp::reject::custom(Error::QuestionNotFound)),
    }
    Ok(warp::reply::with_status("Question updated", StatusCode::OK))
}

pub async fn delete_question(
    id: String,
    store: Store,
) -> Result<impl warp::Reply, warp::Rejection> {
    match store.questions.write().await.remove(&QuestionId(id)) {
        Some(a) => Ok(warp::reply::with_status(
            format!("Question({}) deleted", a.id),
            StatusCode::OK,
        )),
        None => Err(warp::reject::custom(Error::QuestionNotFound)),
    }
}

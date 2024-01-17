use std::collections::HashMap;
use warp::http::StatusCode;
use warp::Rejection;

use crate::store::Store;
use crate::types::answer::{Answer, AnswerId};
use crate::types::pagination::extract_pagination;
use crate::types::question::QuestionId;

pub async fn get_answers(
    params: HashMap<String, String>,
    store: Store,
) -> Result<impl warp::Reply, Rejection> {
    println!("params: {:?}", params);

    if !params.is_empty() {
        let pagination = extract_pagination(params)?;
        let res: Vec<Answer> = store.answers.read().await.values().cloned().collect();
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
        let res: Vec<Answer> = store.answers.read().await.values().cloned().collect();
        Ok(warp::reply::json(&res))
    }
}

pub async fn add_answer(
    store: Store,
    params: HashMap<String, String>,
) -> Result<impl warp::Reply, warp::Rejection> {
    let answer = Answer {
        id: AnswerId("1".to_string()),
        content: params.get("content").unwrap().to_string(),
        question_id: QuestionId(params.get("questionId").unwrap().to_string()),
    };
    store
        .answers
        .write()
        .await
        .insert(answer.id.clone(), answer);
    Ok(warp::reply::with_status("Answer added", StatusCode::OK))
}

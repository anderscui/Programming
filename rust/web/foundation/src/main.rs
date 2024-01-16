use std::fmt::{Display, Formatter};
use std::io::{Error, ErrorKind};
use std::str::FromStr;

use warp::{Filter, filters::{cors::CorsForbidden},
           http::Method, http::StatusCode,
           reject::Reject, Rejection, Reply};
use serde::Serialize;

#[derive(Debug, Serialize)]
struct QuestionId(String);

impl Display for QuestionId {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "id: {}", self.0)
    }
}

impl FromStr for QuestionId {
    type Err = Error;

    fn from_str(id: &str) -> Result<Self, Self::Err> {
        match id.is_empty() {
            false => Ok(QuestionId(id.to_string())),
            true => Err(Error::new(ErrorKind::InvalidInput, "No id provided")),
        }
    }
}

#[derive(Debug)]
struct InvalidId;
impl Reject for InvalidId {}

#[derive(Debug, Serialize)]
struct Question {
    id: QuestionId,
    title: String,
    content: String,
    tags: Option<Vec<String>>,
}

impl Question {
    fn new(id: QuestionId, title: String, content: String, tags: Option<Vec<String>>) -> Self {
        Question {
            id,
            title,
            content,
            tags
        }
    }

    // fn update_title(&self, new_title: String) -> Self {
    //     Question::new(self.id, new_title, self.content, self.tags)
    // }
}

impl Display for Question {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f,
               "{}, title: {}, content: {}, tags: {:?}",
               self.id, self.title, self.content, self.tags)
    }
}

async fn get_questions() -> Result<impl warp::Reply, Rejection> {
    let qid = QuestionId::from_str( "1").expect("No id provided");
    let question = Question::new(qid,
                                 "title".to_string(),
                                 "content".to_string(),
                                 Some(vec!["rust".to_string()]));
    match question.id.0.parse::<i32>() {
        Ok(_) => {
            Ok(warp::reply::json(&question))
        },
        Err(_) => {
            Err(warp::reject::custom(InvalidId))
        }
    }
}

async fn return_error(r: Rejection) -> Result<impl Reply, Rejection> {
    if let Some(error) = r.find::<CorsForbidden>() {
        Ok(warp::reply::with_status(
            error.to_string(),
            StatusCode::FORBIDDEN,
        ))
    } else if let Some(_) = r.find::<InvalidId>() {
        Ok(warp::reply::with_status(
            "No valid ID presented".to_string(),
            StatusCode::UNPROCESSABLE_ENTITY,
        ))
    } else {
        Ok(warp::reply::with_status(
            "Route not found".to_string(),
            StatusCode::NOT_FOUND,
        ))
    }
}

#[tokio::main]
async  fn main() {
    let cors = warp::cors()
        .allow_any_origin()
        .allow_header("content-type")
        .allow_methods(&[Method::PUT, Method::DELETE, Method::GET, Method::POST]);

    let get_items = warp::get()
        .and(warp::path("questions"))
        .and(warp::path::end())
        .and_then(get_questions)
        .recover(return_error);

    let routes = get_items.with(cors);

    // curl http://localhost:3030
    // curl http://localhost:3030/questions
    warp::serve(routes)
        .run(([127, 0, 0, 1], 3030))
        .await;
}
use std::collections::HashMap;
use std::fmt::{Display, Formatter};
use std::net::Ipv4Addr;
use std::sync::Arc;

use warp::{Filter, filters::{body::BodyDeserializeError, cors::CorsForbidden},
           http::Method, http::StatusCode,
           Rejection, reject::Reject, Reply};
use serde::{Deserialize, Serialize};
use tokio::sync::RwLock;

#[derive(Debug, Deserialize, Serialize, Clone, PartialEq, Eq, Hash)]
struct QuestionId(String);

impl Display for QuestionId {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "id: {}", self.0)
    }
}

#[derive(Debug, Clone, Deserialize, Serialize)]
struct Question {
    id: QuestionId,
    title: String,
    content: String,
    tags: Option<Vec<String>>,
}

impl Display for Question {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f,
               "{}, title: {}, content: {}, tags: {:?}",
               self.id, self.title, self.content, self.tags)
    }
}

#[derive(Debug, Deserialize, Serialize, Clone, PartialEq, Eq, Hash)]
struct AnswerId(String);

#[derive(Debug, Clone, Deserialize, Serialize)]
struct Answer {
    id: AnswerId,
    content: String,
    question_id: QuestionId,
}

#[derive(Clone)]
struct Store {
    questions: Arc<RwLock<HashMap<QuestionId, Question>>>,
    answers: Arc<RwLock<HashMap<AnswerId, Answer>>>,
}

impl Store {
    fn new() -> Self {
        Store {
            questions: Arc::new(RwLock::new(Self::init())),
            answers: Arc::new(RwLock::new(HashMap::new())),
        }
    }

    fn init() -> HashMap<QuestionId, Question> {
        let file = include_str!("../questions.json");
        serde_json::from_str(file).expect("can't read data file.")
    }
}

#[derive(Debug)]
enum Error {
    ParseError(std::num::ParseIntError),
    InvalidRange(usize, usize),
    QuestionNotFound,
    MissingParameters,
}

impl Display for Error {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match *self {
            Error::ParseError(ref err) => {
                write!(f, "can't parse param: {}", err)
            },
            Error::MissingParameters => {
                write!(f, "missing param")
            },
            Error::InvalidRange(start, end) => {
                write!(f, "invalid range value: [{start}, {end})")
            }
            Error::QuestionNotFound => {
                write!(f, "question not found")
            }
        }
    }
}

impl Reject for Error {}

#[derive(Debug)]
struct Pagination {
    start: usize,
    end: usize,
}

fn extract_pagination(params: HashMap<String, String>) -> Result<Pagination, Error> {
    if params.contains_key("start") && params.contains_key("end") {
        let start = params.get("start").unwrap().parse::<usize>().map_err(Error::ParseError)?;
        let end = params.get("end").unwrap().parse::<usize>().map_err(Error::ParseError)?;
        return if end <= start {
            Err(Error::InvalidRange(start, end))
        } else {
            Ok(Pagination {
                start,
                end,
            })
        }
    }
    Err(Error::MissingParameters)
}

async fn get_questions(params: HashMap<String, String>,
                       store: Store) -> Result<impl warp::Reply, Rejection> {
    println!("params: {:?}", params);

    if !params.is_empty() {
        let pagination = extract_pagination(params)?;
        let res: Vec<Question> = store
            .questions
            .read().await
            .values().cloned().collect();
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
        let res: Vec<Question> = store.questions.read().await.values().cloned().collect();
        Ok(warp::reply::json(&res))
    }
}

async fn add_question(
    store: Store,
    question: Question
) -> Result<impl warp::Reply, warp::Rejection> {
    store.questions.write().await.insert(question.id.clone(), question);
    Ok(warp::reply::with_status(
        "Question added",
        StatusCode::OK,
    ))
}

async fn update_question(
    id: String,
    store: Store,
    question: Question
) -> Result<impl warp::Reply, warp::Rejection> {
    match store.questions.write().await.get_mut(&QuestionId(id)) {
        Some(q) => *q = question,
        None => return Err(warp::reject::custom(Error::QuestionNotFound)),
    }
    Ok(warp::reply::with_status(
        "Question updated",
        StatusCode::OK,
    ))
}

async fn delete_question(
    id: String,
    store: Store
) -> Result<impl warp::Reply, warp::Rejection> {
    return match store.questions.write().await.remove(&QuestionId(id)) {
        Some(a) => {
            Ok(warp::reply::with_status(
                format!("Question({}) deleted", a.id),
                StatusCode::OK,
            ))
        },
        None => Err(warp::reject::custom(Error::QuestionNotFound)),
    }
}

async fn get_answers(params: HashMap<String, String>,
                     store: Store) -> Result<impl warp::Reply, Rejection> {
    println!("params: {:?}", params);

    if !params.is_empty() {
        let pagination = extract_pagination(params)?;
        let res: Vec<Answer> = store
            .answers
            .read().await
            .values().cloned().collect();
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

async fn add_answer(
    store: Store,
    params: HashMap<String, String>
) -> Result<impl warp::Reply, warp::Rejection> {
    let answer = Answer {
        id: AnswerId("1".to_string()),
        content: params.get("content").unwrap().to_string(),
        question_id: QuestionId(
            params.get("questionId").unwrap().to_string()
        ),
    };
    store.answers.write().await.insert(answer.id.clone(), answer);
    Ok(warp::reply::with_status(
        "Answer added",
        StatusCode::OK,
    ))
}

async fn return_error(r: Rejection) -> Result<impl Reply, Rejection> {
    if let Some(error) = r.find::<Error>() {
        Ok(warp::reply::with_status(
            error.to_string(),
            StatusCode::RANGE_NOT_SATISFIABLE,
        ))
    } else if let Some(error) = r.find::<CorsForbidden>() {
        Ok(warp::reply::with_status(
            error.to_string(),
            StatusCode::FORBIDDEN,
        ))
    } else if let Some(error) = r.find::<BodyDeserializeError>() {
        Ok(warp::reply::with_status(
            error.to_string(),
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
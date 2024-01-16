use std::collections::HashMap;
use std::fmt::{Display, Formatter};
use std::net::Ipv4Addr;

use warp::{Filter, filters::{cors::CorsForbidden},
           http::Method, http::StatusCode,
           Rejection, Reply};
use serde::{Deserialize, Serialize};
use warp::reject::Reject;

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

#[derive(Clone)]
struct Store {
    questions: HashMap<QuestionId, Question>,
}

impl Store {
    fn new() -> Self {
        Store {
            questions: Self::init(),
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
        let res: Vec<Question> = store.questions.values().cloned().collect();
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
        let res: Vec<Question> = store.questions.values().cloned().collect();
        Ok(warp::reply::json(&res))
    }
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

    let get_items = warp::get()
        .and(warp::path("questions"))
        .and(warp::path::end())
        .and(warp::query())
        .and(store_filter)
        .and_then(get_questions)
        .recover(return_error);

    let routes = get_items.with(cors);

    let ip: Ipv4Addr = "127.0.0.1".parse().expect("Please use a valid ip address.");
    let port = 3030;

    // curl http://localhost:3030
    // curl http://localhost:3030/questions
    warp::serve(routes)
        .run((ip, port))
        .await;
}
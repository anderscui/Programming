use std::fmt::{Display, Formatter};
use warp::reject::Reject;
use warp::{Rejection, Reply};
use warp::body::BodyDeserializeError;
use warp::cors::CorsForbidden;
use warp::http::StatusCode;

#[derive(Debug)]
pub enum Error {
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

pub async fn return_error(r: Rejection) -> Result<impl Reply, Rejection> {
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
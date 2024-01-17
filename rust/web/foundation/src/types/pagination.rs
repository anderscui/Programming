use std::collections::HashMap;

use handle_errors::Error;

#[derive(Debug)]
pub struct Pagination {
    pub start: usize,
    pub end: usize,
}

pub fn extract_pagination(params: HashMap<String, String>) -> Result<Pagination, Error> {
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
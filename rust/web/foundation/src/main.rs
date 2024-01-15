use std::collections::HashMap;
use std::fmt::{Display, format, Formatter};
use std::io::{Error, ErrorKind};
use std::str::FromStr;

use warp::Filter;

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

#[tokio::main]
async  fn main() {
    // let qid = QuestionId::from_str( "1").expect("No id provided");
    // let q = Question::new(qid,
    //                       "title".to_string(),
    //                       "content".to_string(),
    //                       Some(vec!["rust".to_string()]));
    // println!("{}", q);

    let hello = warp::get()
        .map(|| format!("Hello, world!"));

    // curl http://localhost:3030
    warp::serve(hello)
        .run(([127, 0, 0, 1], 3030))
        .await;
}

// #[tokio::main]
// async fn main() -> Result<(), Box<dyn std::error::Error>> {
//     // get the current ip
//     let resp = reqwest::get("https://httpbin.org/ip")
//         .await?
//         .json::<HashMap<String, String>>()
//         .await?;
//     println!("{:#?}", resp);
//     Ok(())
// }
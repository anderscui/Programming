use crate::types::question::QuestionId;
use serde::{Deserialize, Serialize};

#[derive(Debug, Deserialize, Serialize, Clone, PartialEq, Eq, Hash)]
pub struct AnswerId(pub i32);

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct Answer {
    pub id: AnswerId,
    pub content: String,
    pub question_id: QuestionId,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct NewAnswer {
    pub content: String,
    pub question_id: QuestionId,
}

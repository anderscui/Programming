-- Add up migration script here
create table if not exists questions (
    id serial primary key,
    title varchar(255) not null,
    content text not null,
    tags text [],
    created_on timestamp not null default now()
);

create table if not exists answers (
    id serial primary key,
    content text not null,
    created_on timestamp not null default now(),
    question_id integer references questions
);
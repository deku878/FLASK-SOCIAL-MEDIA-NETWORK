drop table if exists posts;

create table posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    content text NOT NULL
);
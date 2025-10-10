CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT,
    image BLOB
);

CREATE TABLE tea_varieties (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    variety TEXT REFERENCES tea_varieties(name),
    title, TEXT,
    content TEXT,
    sent_at TEXT,
    user_id INTEGER REFERENCES users(id),
    rating INTEGER
);

CREATE TABLE comments (
    id INTEGER PRIMARY KEY,
    review_id INTEGER REFERENCES reviews(id),
    user_id INTEGER REFERENCES users(id),
    content TEXT,
    sent_at TEXT
);
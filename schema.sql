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

CREATE UNIQUE INDEX idx_username ON users(username);
CREATE UNIQUE INDEX idx_tea_variety_name ON tea_varieties(name);
CREATE INDEX idx_reviews_variety ON reviews(variety);
CREATE INDEX idx_reviews_variety ON reviews(variety);
CREATE INDEX idx_reviews_user_id ON reviews(user_id);
CREATE INDEX idx_comments_review_id ON comments(review_id);
CREATE INDEX idx_comments_user_id ON comments(user_id);
import db

def get_tea_varieties():
    sql = "SELECT name FROM tea_varieties"
    return db.query(sql)

def populate_tea_varieties():
    varieties = ["vihermau", "mustitee", "valkotassu", "maulong", "miutcha", "rooimisu", "yrttikatti", "purrrer", "calico"]
    for variety in varieties:
        sql = "SELECT COUNT(*) FROM tea_varieties WHERE name = ?"
        count = db.query(sql, [variety])[0][0]
        if count == 0:
            sql = "INSERT INTO tea_varieties (name) VALUES (?)"
            db.execute(sql, [variety])

def get_reviews(tea_variety):
    sql = """SELECT r.id, r.title, r.content, r.sent_at, u.username, r.user_id, r.rating
             FROM reviews r 
             JOIN users u ON r.user_id = u.id 
             WHERE r.variety = ?"""
    return db.query(sql, [tea_variety])

def get_review(review_id):
    sql = """SELECT r.id, r.variety, r.title, r.content, r.user_id, r.rating, u.username, r.sent_at 
             FROM reviews r 
             JOIN users u ON r.user_id = u.id 
             WHERE r.id = ?"""
    result = db.query(sql, [review_id])
    return result[0] if result else None

def add_review(variety, title, content, user_id, rating=None):
    sql = "INSERT INTO reviews (variety, title, content, sent_at, user_id, rating) VALUES (?, ?, ?, datetime('now'), ?, ?)"
    db.execute(sql, [variety, title, content, user_id, rating])

def update_review(review_id, title, content, rating=None):
    sql = "UPDATE reviews SET title = ?, content = ?, rating = ? WHERE id = ?"
    db.execute(sql, [title, content, rating, review_id])

def delete_review(review_id):
    sql = "DELETE FROM comments WHERE review_id = ?"
    db.execute(sql, [review_id])

    sql = "DELETE FROM reviews WHERE id = ?"
    db.execute(sql, [review_id])

def search_reviews(query):
    sql = """SELECT r.title, r.content, r.sent_at, r.variety, r.rating, r.id, u.username, u.id AS user_id 
             FROM reviews r 
             JOIN users u ON r.user_id = u.id 
             WHERE r.content LIKE ? OR r.title LIKE ? OR u.username LIKE ? OR r.variety LIKE ?"""
    params = ["%" + query + "%"] * 4
    return db.query(sql, params)

def variety_exists(variety_name):
    sql = "SELECT COUNT(*) FROM tea_varieties WHERE name = ?"
    count = db.query(sql, [variety_name])[0][0]
    return count > 0

def get_comments(review_id):
    sql = """SELECT c.id, c.content, c.sent_at, u.username , c.user_id
             FROM comments c 
             JOIN users u ON c.user_id = u.id 
             WHERE c.review_id = ? 
             ORDER BY c.sent_at"""
    return db.query(sql, [review_id])

def get_comment(comment_id):
    sql = """SELECT c.id, c.content, c.sent_at, c.user_id, u.username, c.review_id
             FROM comments c
             JOIN users u ON c.user_id = u.id
             WHERE c.id = ?"""
    result = db.query(sql, [comment_id])
    return result[0] if result else None

def add_comment(review_id, user_id, content):
    sql = "INSERT INTO comments (review_id, user_id, content, sent_at) VALUES (?, ?, ?, datetime('now'))"
    db.execute(sql, [review_id, user_id, content])

def edit_comment(comment_id, content):
    sql = """UPDATE comments SET content = ? WHERE id = ?"""
    db.execute(sql, [content, comment_id])

def delete_comment(comment_id):
    sql = """DELETE FROM comments WHERE id = ?"""
    db.execute(sql, [comment_id])

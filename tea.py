import db

def get_tea_varieties():
    sql = "SELECT name FROM tea_varieties"
    return db.query(sql)

def populate_tea_varieties():
    varieties = ['vihermau', 'mustitee', 'valkotassu', 'maulong', 'miutcha', 'rooimisu', 'yrttikatti', 'purrrer', 'calico']
    for variety in varieties:
        sql = "SELECT COUNT(*) FROM tea_varieties WHERE name = ?"
        count = db.query(sql, [variety])[0][0]
        if count == 0:
            sql = "INSERT INTO tea_varieties (name) VALUES (?)"
            db.execute(sql, [variety])

def get_reviews(tea_variety):
    sql = """SELECT r.id, r.content, r.sent_at, u.username, r.user_id 
             FROM reviews r 
             JOIN users u ON r.user_id = u.id 
             WHERE r.variety = ?"""
    return db.query(sql, [tea_variety])

def get_review(review_id):
    sql = "SELECT id, variety, content, user_id FROM reviews WHERE id = ?"
    result = db.query(sql, [review_id])
    return result[0] if result else None

def add_review(variety, content, user_id):
    sql = "INSERT INTO reviews (variety, content, sent_at, user_id) VALUES (?, ?, datetime('now'), ?)"
    db.execute(sql, [variety, content, user_id])

def update_review(review_id, content):
    sql = "UPDATE reviews SET content = ? WHERE id = ?"
    db.execute(sql, [content, review_id])

def delete_review(review_id):
    sql = "DELETE FROM reviews WHERE id = ?"
    db.execute(sql, [review_id])

def search_reviews(query):
    sql = """SELECT r.content, r.sent_at, r.variety, u.username 
             FROM reviews r 
             JOIN users u ON r.user_id = u.id 
             WHERE r.content LIKE ?"""
    return db.query(sql, ['%' + query + '%'])

def variety_exists(variety_name):
    sql = "SELECT COUNT(*) FROM tea_varieties WHERE name = ?"
    count = db.query(sql, [variety_name])[0][0]
    return count > 0

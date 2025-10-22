from werkzeug.security import check_password_hash, generate_password_hash
import db

def create_user(username, password):
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    db.execute(sql, [username, password_hash])

def check_login(username, password):
    sql = "SELECT id, password_hash FROM users WHERE username = ?"
    result = db.query(sql, [username])

    if len(result) == 1:
        user_id, password_hash = result[0]
        if check_password_hash(password_hash, password):
            return user_id

    return None

def get_user(user_id):
    sql = """SELECT id, username, image IS NOT NULL has_image
             FROM users
             WHERE id = ?"""
    result = db.query(sql, [user_id])
    return result[0] if result else None

def get_reviews(user_id):
    sql = """SELECT r.id, r.variety, r.title, r.content, r.sent_at, r.rating, t.name AS variety_name 
             FROM reviews r 
             JOIN tea_varieties t ON r.variety = t.name 
             WHERE r.user_id = ?
             ORDER BY r.sent_at DESC"""
    return db.query(sql, [user_id])

def update_image(user_id, image):
    sql = "UPDATE users SET image = ? WHERE id = ?"
    db.execute(sql, [image, user_id])

def get_image(user_id):
    sql = "SELECT image FROM users WHERE id = ?"
    result = db.query(sql, [user_id])
    return result[0][0] if result else None

def user_exists(user_id):
    sql = "SELECT COUNT(*) FROM users WHERE id = ?"
    count = db.query(sql, [user_id])[0][0]
    return count > 0

def get_stats(user_id):
    sql_most_reviewed = """SELECT r.variety, COUNT(r.id) as review_count
                                FROM reviews r
                                WHERE r.user_id = ?
                                GROUP BY r.variety
                                ORDER BY review_count DESC
                                LIMIT 1"""
    most_reviewed_tea = db.query(sql_most_reviewed, [user_id])

    sql_avg_rating = """SELECT AVG(r.rating) as average_rating
                        FROM reviews r
                        WHERE r.user_id = ?"""
    avg_rating_result = db.query(sql_avg_rating, [user_id])
    average_rating = avg_rating_result[0]['average_rating'] if avg_rating_result else None

    sql_comments_given = """SELECT COUNT(*) as comments_given
                            FROM comments c
                            WHERE c.user_id = ?"""
    comments_given_result = db.query(sql_comments_given, [user_id])
    comments_given = comments_given_result[0]['comments_given'] if comments_given_result else 0

    sql_comments_received = """SELECT COUNT(*) as comments_received
                               FROM comments c
                               JOIN reviews r ON c.review_id = r.id
                               WHERE r.user_id = ?"""
    comments_received_result = db.query(sql_comments_received, [user_id])
    comments_received = comments_received_result[0]['comments_received'] if comments_received_result else 0

    stats = {
        "most_reviewed_tea": most_reviewed_tea[0] if most_reviewed_tea else None,
        "average_rating": average_rating,
        "comments_given": comments_given,
        "comments_received": comments_received
    }

    return stats
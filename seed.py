import random
import sqlite3
import datetime

db = sqlite3.connect("database.db")
cursor = db.cursor()

db.execute("DELETE FROM comments")
db.execute("DELETE FROM reviews")
db.execute("DELETE FROM users")
db.execute("DELETE FROM tea_varieties")

user_count = 1000
review_count = 10**6
comment_count = 10**7

usernames = [f"Testikisuli {i}" for i in range(1, user_count + 1)] 
tea_varieties = ["vihermau", "mustitee", "valkotassu", "maulong", "miutcha", "rooimisu", "yrttikatti", "purrrer", "calico"]
review_titles = [
    "Mahtavaa!",
    "Paras tee ikinä!",
    "Tassun täydellistä rentoutumista",
    "Kissan suosikki",
    "Tee-rveellistä ja ihanaa!"
]

review_contents = [
    "Tämä tee on ihan kissanmiau! Rakastan sitä!",
    "Täydellinen tee mukavaan iltapäivään.",
    "En saa tästä teestä tarpeekseni!",
    "Tämä on luottoteeni, kun haluan rentoutua.",
    "Pelkkää ihanuutta täynnä!"
]

for variety in tea_varieties:
    cursor.execute("INSERT INTO tea_varieties (name) VALUES (?)", [variety])

user_ids = []
for username in usernames:
    cursor.execute("INSERT INTO users (username) VALUES (?)", [username])
    user_ids.append(cursor.lastrowid)

review_ids = []
for i in range(1, review_count + 1):
    user_id = random.choice(user_ids)
    variety = random.choice(tea_varieties)
    title = random.choice(review_titles)
    content = random.choice(review_contents)
    rating = random.randint(1, 5)
    cursor.execute("""INSERT INTO reviews (variety, title, content, sent_at, user_id, rating)
                      VALUES (?, ?, ?, ?, ?, ?)""",
                   [variety, title, content, datetime.datetime.now(), user_id, rating])
    review_ids.append(cursor.lastrowid)

for i in range(1, comment_count + 1):
    user_id = random.choice(user_ids)
    review_id = random.choice(review_ids)
    comment_content = f"Kommentin kirjoitti {usernames[user_ids.index(user_id)]} teehetkeen {review_id}."
    cursor.execute("""INSERT INTO comments (review_id, user_id, content, sent_at)
                      VALUES (?, ?, ?, ?)""",
                   [review_id, user_id, comment_content, datetime.datetime.now()])

db.commit()
db.close()
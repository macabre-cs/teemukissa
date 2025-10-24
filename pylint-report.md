# Pylint-raportti

Pylint antaa seuraavan raportin sovelluksesta:

```
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:1:0: C0410: Multiple imports on one line (sqlite3, secrets, math, time) (multiple-imports)
app.py:15:0: C0410: Multiple imports on one line (config, users, tea) (multiple-imports)
app.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:27:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:37:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:43:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:49:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:65:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:82:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:89:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:94:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:101:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:125:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:145:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:145:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:187:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:187:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:220:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:247:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:274:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:281:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:308:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:331:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:363:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:391:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:391:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:427:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:436:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:427:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:447:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:447:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:472:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:484:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module db
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:1:0: C0410: Multiple imports on one line (sqlite3, time) (multiple-imports)
db.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:12:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:12:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:12:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
db.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:31:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:38:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module seed
seed.py:70:0: C0301: Line too long (105/100) (line-too-long)
seed.py:1:0: C0114: Missing module docstring (missing-module-docstring)
seed.py:13:0: C0103: Constant name "user_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:14:0: C0103: Constant name "review_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:15:0: C0103: Constant name "comment_count" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module tea
tea.py:48:0: C0301: Line too long (123/100) (line-too-long)
tea.py:67:0: C0301: Line too long (105/100) (line-too-long)
tea.py:105:0: C0301: Line too long (105/100) (line-too-long)
tea.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tea.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
tea.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
tea.py:29:0: C0116: Missing function or method docstring (missing-function-docstring)
tea.py:38:0: C0116: Missing function or method docstring (missing-function-docstring)
tea.py:47:0: C0116: Missing function or method docstring (missing-function-docstring)
tea.py:52:0: C0116: Missing function or method docstring (missing-function-docstring)
tea.py:57:0: C0116: Missing function or method docstring (missing-function-docstring)
tea.py:65:0: C0116: Missing function or method docstring (missing-function-docstring)
tea.py:80:0: C0116: Missing function or method docstring (missing-function-docstring)
tea.py:86:0: C0116: Missing function or method docstring (missing-function-docstring)
tea.py:95:0: C0116: Missing function or method docstring (missing-function-docstring)
tea.py:104:0: C0116: Missing function or method docstring (missing-function-docstring)
tea.py:109:0: C0116: Missing function or method docstring (missing-function-docstring)
tea.py:114:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:23:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:40:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:45:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:51:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:57:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:57:0: R0914: Too many local variables (16/15) (too-many-locals)
users.py:1:0: R0801: Similar lines in 2 files
==seed:[18:28]
==tea:[10:20]
    "vihermau",
    "mustitee",
    "valkotassu",
    "maulong",
    "miutcha",
    "rooimisu",
    "yrttikatti",
    "purrrer",
    "calico",
] (duplicate-code)

------------------------------------------------------------------
Your code has been rated at 8.31/10 (previous run: 8.31/10, +0.00)
```

Käydään läpi raportin sisältö ja perustellaan, miksi kyseisiä asioita ei ole korjattu sovelluksessa.

## Docstring-ilmoitukset

Pitkälti suurinosa pylintin valituksista koostuu näistä:

```
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
```

Nämä ilmoitukset tarkoittavat sitä, että moduuleissa ja funktioissa ei ole tehty docstring-kommentteja. Kurssin ohjeiden mukaan niitä ei tarvitse tehdä, joten ne on jätetty tekemättä.

## Import-ilmoitukset

```
app.py:15:0: C0410: Multiple imports on one line (config, users, tea) (multiple-imports)
db.py:1:0: C0410: Multiple imports on one line (sqlite3, time) (multiple-imports)
```

Sovelluksen käyttämä versio:
```python
import config, users, tea
```

Pylintin toivoma:
```python
import config
import users
import tea
```

Nämä ilmoitukset tarkoittavat sitä, että koodissa on samalla rivillä useampi `import`-komento. Sovelluksen kehittäjän näkökulmasta, on siistimpää kun ne ovat samalla rivillä, jottei tiedoston ensimmäiset n-riviä koostu vain importeista. Pylintin mieliksi Flask-importit on kasattu eri riveille, koska niitä oli kovin monta.

## Tarpeeton else

Pylint ilmoittaa meille raportissa esimerkiksi seuraavat ilmoitukset liittyen `else`-haaroihin:

```
app.py:274:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:436:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
```

Tarkastellaan ensimmäisen ilmoituksen funktiota:

```python
@app.route("/add_comment", methods=["POST"])
def add_comment():
.
.
.
    if source == "tea":
        return redirect(f"/tea/{review['variety']}")
    if source == "review":
        return redirect(f"/review/{review['id']}")
    else:
        abort(400)
```

Tämä koodi voidaan kirjoittaa myös ilman elseä näin:

```python
@app.route("/add_comment", methods=["POST"])
def add_comment():
.
.
.
    if source == "tea":
        return redirect(f"/tea/{review['variety']}")
    if source == "review":
        return redirect(f"/review/{review['id']}")
    abort(400)
```

Näin ei kuitenkaan ole tehty, koska sovelluksen logiikan seuraamisen kannalta on selkeämpää, että erillinen `else`-haara on kirjoitettu. Se tuo paremmin esille, miten koodi voi toimia eri tilanteissa. Muut ilmoitukset ovat vastaavia tilanteita.

## Puuttuva palautusarvo

Raportissa näkyy seuraavat ilmoitukset, jotka liittyvät funktioiden palautusarvoihin:

```
app.py:145:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:187:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:447:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
```

Nämä ilmoitukset aiheuttaa tilanne, jossa funktio käsittelee metodit `GET` ja `POST` mutta ei muita metodeja.

Tarkastellaan kolmannen ilmoituksen funktiota:

```python
@app.route("/add_image", methods=["GET", "POST"])
def add_image():
    require_login()

    if request.method == "GET":
        return render_template("add_image.html")

    if request.method == "POST":
        check_csrf()
        file = request.files["image"]
        if not file.filename.endswith(".jpg"):
            flash("Lähettämäsi tiedosto ei ole jpg-tiedosto! :O")
            return redirect("/add_image")

        image = file.read()
        if len(image) > 100 * 1024:
            flash("Lähettämäsi tiedosto on liian suuri ;)))")
            return redirect("/add_image")

        user_id = session["user_id"]
        users.update_image(user_id, image)
        flash("Kuvan lisääminen onnistui!! :3")
        return redirect("/user/" + str(user_id))
```

Tämä funktio käsittelee käyttäjän profiilikuvan asettamista. Tämä funktio palauttaa arvon, kun `request.method` on `GET` tai `POST`. Periaatteessa olisi myös mahdollista, että `request.method` olisi jotain muuta kuin `GET` tai `POST`, mutta käytännössä tämä tilanne ei ole mahdollinen. Funktion dekoraattorissa on ehto, että metodin tulee olla `GET` tai `POST`. Ei siis ole oikeata riskiä, että funktio ei jossain tilanteessa palauttaisi mitään arvoa. Pylintin raportoimat muut ilmoitukset tästä aiheesta ovat kaikki samanlaisia kuin tämä esimerkki.

## Vakion nimi

Raportissa on seuraava ilmoitus liittyen vakion nimeen:

```
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
```

Pylint tulkitsee tämän muuttujan vakioksi, jonka takia sen tulisi olla kirjoitettu isoilla kirjaimilla. Sovelluksen kehittäjän näkökulmasta muuttuja näyttää paremmalta, kun sen nimi on kirjoitettu pienillä kirjaimilla.

Muuttujaa käytetään koodissa näin:

```python
app.secret_key = config.secret_key
```

Pylint myös ilmoittaa näistä muuttujista:

```
seed.py:13:0: C0103: Constant name "user_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:14:0: C0103: Constant name "review_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:15:0: C0103: Constant name "comment_count" doesn't conform to UPPER_CASE naming style (invalid-name)
```

Koodissa ne näyttävät tältä:

```python
user_count = 1000
review_count = 10**6
comment_count = 10**7
```

Käytännössä nämä ovat oikeasti vain muuttujia (kuten aikaisemmassa tapauksessa), joita käytetään testidatan luomiseen. Mielestäni (eli tyylikkäästi sovelluksen kehittäjän näkökulmasta) ne ovat myös tässä kontekstissa luettavampia näin.

## Vaarallinen oletusarvo

Raportissa seuraavat ilmoitukset liittyvät vaaralliseen oletusarvoon:

```
db.py:12:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:31:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
```

Tarkastellaan toisen ilmoituksen funktiota:

```python
def query(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params).fetchall()
    con.close()
    return result
```

Voimme huoletta jättää huomiotta tämän ilmoituksen, koska oletusarvona olevaa tyhjä listaa ei missään kohtaa muokata. Se vain luetaan ja lähetetään tietokantaan. Riskinä olisi, jos funktio muokkaisi listaa jollain tavalla. Se voisi aiheuttaa erilaisia ongelmia. Muut ilmoitukset tästä aiheesta ovat vastaavia.

## Liian pitkä rivi

Raportissa on muutama ilmoitus liian pitkistä koodiriveistä:

```
seed.py:70:0: C0301: Line too long (105/100) (line-too-long)
tea.py:48:0: C0301: Line too long (123/100) (line-too-long)
tea.py:67:0: C0301: Line too long (105/100) (line-too-long)
tea.py:105:0: C0301: Line too long (105/100) (line-too-long)
```

Tarkastellaan pisintä näistä:

```python
    sql = "INSERT INTO reviews (variety, title, content, sent_at, user_id, rating) VALUES (?, ?, ?, datetime('now'), ?, ?)"
```

On totta, että rivi on aika pitkä, mutta mielestäni se on luettavampi näin kuin esim näin:

```python
    sql = """INSERT INTO reviews (variety, title, content, sent_at, user_id, rating) 
    VALUES (?, ?, ?, datetime('now'), ?, ?)"""
```

Molemmat on mielestäni ihan ok, itse preferoin tässä pidempää riviä. Raportin muut ilmoitukset ovat vastaavia ja perustelut niihin ovat samanlaisia kuin tähän.

## Liian monta muuttujaa

Pylint ilmoittaa meille, että meillä on yhden funktion sisällä liian monta muuttujaa.

```
users.py:57:0: R0914: Too many local variables (16/15) (too-many-locals)
```

Tarkastellaan funktiota:

```python
def get_stats(user_id):
    sql_total_reviews = """SELECT COUNT(*) as total_reviews
                           FROM reviews
                           WHERE user_id = ?"""
    total_reviews_result = db.query(sql_total_reviews, [user_id])
    total_reviews = (
        total_reviews_result[0]["total_reviews"] if total_reviews_result else 0
    )

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
    average_rating = (
        avg_rating_result[0]["average_rating"] if avg_rating_result else None
    )

    sql_comments_given = """SELECT COUNT(*) as comments_given
                            FROM comments c
                            WHERE c.user_id = ?"""
    comments_given_result = db.query(sql_comments_given, [user_id])
    comments_given = (
        comments_given_result[0]["comments_given"] if comments_given_result else 0
    )

    sql_comments_received = """SELECT COUNT(*) as comments_received
                               FROM comments c
                               JOIN reviews r ON c.review_id = r.id
                               WHERE r.user_id = ?"""
    comments_received_result = db.query(sql_comments_received, [user_id])
    comments_received = (
        comments_received_result[0]["comments_received"]
        if comments_received_result
        else 0
    )

    stats = {
        "total_reviews": total_reviews,
        "most_reviewed_tea": most_reviewed_tea[0] if most_reviewed_tea else None,
        "average_rating": average_rating,
        "comments_given": comments_given,
        "comments_received": comments_received,
    }

    return stats
```

Pitäähän se paikkansa, että funktiossa on aika monta muuttujaa ja se on aika pitkä. Sen pilkkominen paloihin ei kuitenkaan tekisi siitä erityisesti luettavampaa tai parempaa, joten se on sovelluksen kehittäjän näkökulmasta hiukan turhaa. Tämä funktio käyttää kaikkia muuttujia ja tarvitsee niitä tallentamaan eri SQL-kyselyiden tuloksia.

## Toisteista koodia

Pylint ilmoittaa meille, että meillä on kahdessa tiedostossa toisteista koodia.

```
users.py:1:0: R0801: Similar lines in 2 files
==seed:[18:28]
==tea:[10:20]
    "vihermau",
    "mustitee",
    "valkotassu",
    "maulong",
    "miutcha",
    "rooimisu",
    "yrttikatti",
    "purrrer",
    "calico",
] (duplicate-code)
```

Tilanne on kuitenkin oikeasti se, että tiedostossa `seed.py` luomme sovelluksen testaamiseen testidataa kun taas tiedostossa `tea.py` alustamme "oikean" tietokannan. Tämä ilmoitus on mielestäni triviaali, silla kyseessä on vain yksi lista. Sen korjaaminen tekisi koodista monimutkaisempaa turhaan.
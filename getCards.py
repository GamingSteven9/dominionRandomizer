# Gets the cards from the given database
def getCards(con, c):
    cur = con.cursor()
    cur.execute("SELECT * FROM base1")
    rows = cur.fetchall()
    for row in rows:
        c[row[0]] = [row[1], row[2]]
    return c
# Gets the cards from the given database
def getCards(con, c):
    cur = con.cursor()
    cur.execute("SELECT * FROM Base2E")
    rows = cur.fetchall()
    for row in rows:
        match row[3]:
            case None:
                c[row[0]] = [row[1], row[2]]
            case _:
                c[row[0]] = [row[1], row[2], row[3]]
    print(c)
    return c
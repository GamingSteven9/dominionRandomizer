# Gets the cards from the given database
def getCards(con, c, selectedExpansions):
    cur = con.cursor()
    rows = []
    for i in range(0, len(selectedExpansions)):
        match selectedExpansions[i]:
            case "Base":
                cur.execute("SELECT * FROM Base")
                rows = rows + cur.fetchall()
            case "Base2E":
                cur.execute("SELECT * FROM Base2E")
                rows = rows + cur.fetchall()
            case "Intrigue":
                cur.execute("SELECT * FROM Intrigue")
                rows = rows + cur.fetchall()
            case "Intrigue2E":
                cur.execute("SELECT * FROM Intrigue2E")
                rows = rows + cur.fetchall()
    #print(rows)
    for row in rows:
        match row[3]: # Adds the second card type if the given card has two
            case None:
                c[row[0]] = [row[1], row[2]]
            case _:
                c[row[0]] = [row[1], row[2], row[3]]
    #print(c)
    return c
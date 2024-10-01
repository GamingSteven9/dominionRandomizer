# Gets the cards from the selected expansions
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
            case "Seaside":
                cur.execute("SELECT * FROM Seaside")
                rows = rows + cur.fetchall()
            case "Seaside2E":
                cur.execute("SELECT * FROM Seaside2E")
                rows = rows + cur.fetchall()
            case "Alchemy":
                cur.execute("SELECT * FROM Alchemy")
                rows = rows + cur.fetchall()
            case "Prosperity":
                cur.execute("SELECT * FROM Prosperity")
                rows = rows + cur.fetchall()
            case "Prosperity2E":
                cur.execute("SELECT * FROM Prosperity2E")
                rows = rows + cur.fetchall()
            case "Cornucopia":
                cur.execute("SELECT * FROM Cornucopia")
                rows = rows + cur.fetchall()
            case "Cornucopia2E":
                cur.execute("SELECT * FROM Cornucopia2E")
                rows = rows + cur.fetchall()
            case "Hinterlands":
                cur.execute("SELECT * FROM Hinterlands")
                rows = rows + cur.fetchall()
            case "Hinterlands2E":
                cur.execute("SELECT * FROM Hinterlands2E")
                rows = rows + cur.fetchall()
            case "Dark_Ages":
                cur.execute("SELECT * FROM Dark_Ages")
                rows = rows + cur.fetchall()
            case "Guilds":
                cur.execute("SELECT * FROM Guilds")
                rows = rows + cur.fetchall()
            case "Guilds2E":
                cur.execute("SELECT * FROM Guilds2E")
                rows = rows + cur.fetchall()
            case "Adventures":
                cur.execute("SELECT * FROM Adventures")
                rows = rows + cur.fetchall()
            case "Empires":
                cur.execute("SELECT * FROM Empires")
                rows = rows + cur.fetchall()
            case "Nocturne":
                cur.execute("SELECT * FROM Nocturne")
                rows = rows + cur.fetchall()
            case "Renaissance":
                cur.execute("SELECT * FROM Renaissance")
                rows = rows + cur.fetchall()
            case "Menagerie":
                cur.execute("SELECT * FROM Menagerie")
                rows = rows + cur.fetchall()
            case "Allies":
                cur.execute("SELECT * FROM Allies")
                rows = rows + cur.fetchall()
            case "Plunder":
                cur.execute("SELECT * FROM Plunder")
                rows = rows + cur.fetchall()
            case "Rising_Sun":
                cur.execute("SELECT * FROM Rising_Sun")
                rows = rows + cur.fetchall()
            case "Promos":
                cur.execute("SELECT * FROM Promos")
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
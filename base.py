from createConnection import create_connection
from getCards import getCards
from generateKingdom import generateKingdom

cards = {}

connection = create_connection("expansions\\base1.db") # Creates connection to sqlite database
cards = getCards(connection, cards) # Gets name of cards from database
kingdom = generateKingdom(cards) # Generates the kingdom
print(kingdom)
from random import sample

from createConnection import create_connection
from getCards import getCards
from updateTextBox import updateTextBox
from getExpansions import getExpansions

# Generates the kingdom cards that will be used from the cards given
def generateKingdom(chk_vars, t_box):
    cards = {} # Stores the names of the cards
    connection = create_connection("expansions\\expansions.db") # Creates a connection to the database with the expansions 
    selectedExpansions = getExpansions(chk_vars)
    cards = getCards(connection, cards, selectedExpansions) # Gets name of cards from the chosen expansions
    kingdom = sample(sorted(cards), k=10)
    updateTextBox(t_box, kingdom) # Updates the textbox to display the generated kingdom
    return None
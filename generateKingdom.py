from random import sample

# Generates the kingdom cards that will be used from the cards given
def generateKingdom(cards):
    kingdom = sample(sorted(cards), k=5)
    #print(kingdom)
    return kingdom
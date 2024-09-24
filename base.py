import tkinter as tk
from tkinter import ttk

from createConnection import create_connection
from getCards import getCards
from generateKingdom import generateKingdom
from updateTextBox import updateTextBox
from createCheckBoxes import createCheckBoxes

cards = {}

# Creates the window for the applications
root = tk.Tk()
root.title("Dominion Randomizer")
root.geometry("1000x1000")

generatedKingdom = tk.Label(root, text="Generated Kingdom")

expanions = ["Base", "Base 2e", "Intrigue", "Intrigue 2e", "Seaside", "Seaside 2e", "Alchemy", "Prosperity", "Prosperity 2e", "Cornucopia", "Cornucopia 2e", "Hinterlands", "Hinterlands 2e", "Dark Ages", "Guilds", "Guilds 2e",
             "Adventures", "Empires", "Nocturne", "Renaissance", "Menagerie", "Allies", "Plunder", "Rising Sun", "Promos"]

connection = create_connection("expansions\\base1.db") # Creates connection to sqlite database
cards = getCards(connection, cards) # Gets name of cards from database

chk_vars = [] # Create a list for the checkbox variables

t_box = tk.Text(root, height=12, width=40)
t_box.pack(expand=True)

createCheckBoxes(expanions, chk_vars, root) # Creates the checkboxes

def getExpansions():
    selected_Expansions = [var.get() for var in chk_vars]
    kingdom = generateKingdom(cards) # Generates the kingdom
    updateTextBox(t_box, kingdom) # Updates the textbox to display the generated kingdom

    print(selected_Expansions)

    
getKingdom = tk.Button(root, text="Generate Kingdom", command=getExpansions)
getKingdom.pack()

root.mainloop()
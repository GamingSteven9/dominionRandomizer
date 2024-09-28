import tkinter as tk
from generateKingdom import generateKingdom
from updateTextBox import updateTextBox

def getExpansions(chk_vars, cards, t_box):
    selected_Expansions = [var.get() for var in chk_vars]
    kingdom = generateKingdom(cards) # Generates the kingdom
    updateTextBox(t_box, kingdom) # Updates the textbox to display the generated kingdom

    print(selected_Expansions)
import tkinter as tk

from generateKingdom import generateKingdom
from createCheckBoxes import createCheckBoxes
from updateTextBox import updateTextBox

chk_vars = [] # Create a list for the checkbox variables

# Creates the window for the applications
root = tk.Tk()
root.title("Dominion Randomizer")
root.geometry("1000x1000")

generatedKingdom = tk.Label(root, text="Generated Kingdom")

expansions = ["Base", "Base2E", "Intrigue", "Intrigue2E", "Seaside", "Seaside2E", "Alchemy", "Prosperity", "Prosperity2E", "Cornucopia", "Cornucopia2E", "Hinterlands", "Hinterlands2E", "Dark_Ages", "Guilds", "Guilds2E",
             "Adventures", "Empires", "Nocturne", "Renaissance", "Menagerie", "Allies", "Plunder", "Rising_Sun", "Promos"] # List with the names of the expansions

t_box = tk.Text(root, height=10, width=100) # Creates the textbox used to display the generated kingdom
t_box.pack(expand=True)

createCheckBoxes(expansions, chk_vars, root) # Creates the checkboxes
    
getKingdom = tk.Button(root, text="Generate Kingdom", command=(lambda: updateTextBox(t_box, generateKingdom(chk_vars, t_box)))) # Button that displays the generated kingdom in the textbox
getKingdom.pack()

root.mainloop()
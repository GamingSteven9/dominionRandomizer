import tkinter as tk

def createCheckBoxes(expanions, chk_vars, root):
    # Creates the checkboxes
    for option in expanions:
        var = tk.StringVar(value="Unchecked")
        chk_vars.append(var)
        chk = tk.Checkbutton(root, offvalue="Unchecked", onvalue=str(option), text=option, variable=var) #Option is the name of the expansion
        #print(chk.select())
        chk.pack(anchor=tk.W)
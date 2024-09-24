import tkinter as tk

'''class Checkbutton(tk.Checkbutton):
    def __init__(self, parent, **kwargs):
        self.var = tk.StringVar
        super().__init__(parent, variable=self.var, **kwargs)

    def __str__(self):
        return f"Checkbutton: {self['text']}={self.checked}"'''

def createCheckBoxes(expanions, chk_vars, root):
    # Creates the checkboxes
    for option in expanions:
        chk_vars.append(var)
        chk = tk.Checkbutton(root, text=option, onvalue=1, offvalue=0, variable=var) #Option is the name of the expansion
        #print(chk.select())
        chk.pack(anchor=tk.W)
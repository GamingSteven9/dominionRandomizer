import tkinter as tk
from tkinter import ttk

def updateTextBox(t_box, kingdom): # Updates the textbox
    t_box.config(state='normal')
    t_box.delete('1.0', 'end')
    t_box.insert('1.0',kingdom)
    t_box.config(state='disabled')
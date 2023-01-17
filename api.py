import tkinter as tk
from tkinter import simpledialog
import sys

ROOT = tk.Tk()
ROOT.withdraw()

# Ask lang

def askNum(text:str):
    USER_INP = simpledialog.askinteger(title="Rosary", prompt=text)
    if USER_INP == None:
        sys.exit("Program cancelled by user")
    return USER_INP

def draw(text:str):
    USER_INP = simpledialog.askstring(title="Rosary", prompt=text)
    if USER_INP == None:
        sys.exit("Program cancelled by user")
import tkinter as tk
from tkinter import simpledialog
import sys

ROOT = tk.Tk()
ROOT.withdraw()

def askNum(text:str, title:str = " ")->int:
    USER_INP = simpledialog.askinteger(title=title, prompt=text)
    if USER_INP == None:
        sys.exit("Program cancelled by user")
    return USER_INP

def draw(text:str, title:str = " ")->str:
    USER_INP = simpledialog.askstring(title=title, prompt=text)
    if USER_INP == None:
        sys.exit("Program cancelled by user")
    return USER_INP
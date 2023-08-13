from tkinter import *

class Buttons(Button):
    
    def __init__(self,type):
        super().__init__()
        self.config(text=type)
        self.config(highlightthickness=0)
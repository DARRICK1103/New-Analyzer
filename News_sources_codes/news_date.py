from tkinter import *
from PIL import Image, ImageTk
from datetime import date as dt

class Date:
    def __init__(self, root):
        self.root = root

    def create(self):
        # Create label on root for row 1
        welcome = Label(self.root, text="Welcome to NewsNet", font=("Arial", 20))
        empty_space3 = Label(self.root)
        today_date = dt.today().strftime("%d %B %Y")  # Get today's date and format it as string
        
        date_label = Label(self.root, text=today_date, font=("Arial", 20), fg="#707070")

        welcome.grid(row=0, column=0, pady=10)
        empty_space3.grid(row=0, column=1, padx=350)
        date_label.grid(row=0, column=2, padx=30, pady=10)

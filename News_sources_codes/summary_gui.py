from tkinter.ttk import Separator
import user_manager
from tkinter import *
from PIL import Image, ImageTk
import news_structure1 as nw1
import news_date as ndate
import news_structure2 as nw2
import os
import sys
import news

screen_width=1920
screen_height=1080
value=4

if len(sys.argv) < 2:
    print("Usage: python summary_gui.py <news_id>")
    sys.exit(1)

news_id = sys.argv[1]

current_news = news.get(news_id)

def load_image(file_path, x, y):
    img = Image.open(file_path)
    new_img = img.resize((x, y))
    photo_img = ImageTk.PhotoImage(new_img)
    return photo_img

root = Tk()
frame_news = Frame(root)
frame_news.pack()
label = Label(frame_news, text="Summary📝", font=('Arial', 14, "bold") )
label.grid(row=0, column=0)
frame_text = Frame(frame_news, width=100,borderwidth=2, relief="groove")
frame_text.grid(row=1, column=0, pady=20, padx=20)



# Add text to the Text widget
long_text = current_news.SUMMARY

# Set anchor to center and wraplength to 900 pixels
text_label = Label(frame_text, text=long_text, font=('Arial', 12), wraplength=600, justify="left", pady=10, padx=10)
text_label.pack()

def close_window():
    root.destroy()

# Add a button to close the window
close_button = Button(frame_news, text="Close", command=close_window, bg="grey", fg="white", font=('Arial', 12))
close_button.grid(row=2, column=0, pady=30, padx=20, sticky="e")

root.mainloop()
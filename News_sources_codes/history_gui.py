from tkinter.ttk import Separator
import user_manager
from tkinter import *
from PIL import Image, ImageTk
import news_structure1 as nw1
import news_date as ndate
import news_structure2 as nw2
import os
import sys
import NewsAnalyzer
from datetime import datetime
import requests
from PIL import Image
from io import BytesIO
import time
import webbrowser
import category
import news
import read_history
import binascii
from PIL import ImageOps

def load_image_url(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)

def load_image(file_path, x, y):
    img = Image.open(file_path)
    new_img = img.resize((x, y))
    photo_img = ImageTk.PhotoImage(new_img)
    return photo_img

root = Tk()

root.title('Main Page')

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

# Create a frame with a black background
frame1 = Frame(root, bg="#1C1C1C", width=1600, height=100)
frame1.pack(fill=X)

# Open image
img = Image.open("Image/news_icon.png")

# Resize image
new_img = img.resize((80, 65))

# Convert image to PhotoImage
photo_img = ImageTk.PhotoImage(new_img)


empty_space2 = Label(frame1,  bg="#1C1C1C", width=80)
empty_space2.grid(row=0, column=0)

# Create a label and display the image on the frame
label = Label(frame1, image=photo_img, bg="#1C1C1C")
label.grid(row=0, column=2, padx=30, pady=20)


label_name = Label(frame1, text="NewsNet", font = ("Arial", 20), bg="#1C1C1C", fg="white")
label_name.grid(row=0, column=3, padx=7)

frame2 = Frame(root, bg="#1C1C1C", width=1600, height=10)
frame2.pack(fill=X)


separator = Separator(frame2, orient='horizontal', style='Separator.TSeparator')
separator.pack(fill='x')

empty_space = Label(frame2,  bg="#1C1C1C")
empty_space.pack()

# Create a canvas with scrollbars
canvas = Canvas(root)
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.config(yscrollcommand=scrollbar.set)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Create a frame to hold the content
content_frame = Frame(canvas, borderwidth=2, relief="groove")

# Bind mouse wheel to scrollbar
def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    if canvas.bbox("all")[1] < 0:
        canvas.yview_scroll(-1, "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)

# Set the content_frame to expand to fill the window
content_frame.pack(expand=True, fill=BOTH) 

# Set the canvas to expand to fill the content_frame
canvas.create_window((0, 0), window=content_frame, anchor="nw")


#-------------------------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------------------------
# News



if len(sys.argv) < 2:
    print("Usage: python home_gui.py <user_id> <news_id>")
    sys.exit(1)

user_id = sys.argv[1]
news_id = sys.argv[2]

current_news = news.get(news_id)


frame_button = Frame(content_frame)
frame_button.grid(row=0, column=0)

def onlick_home(window):
    window.destroy()
    os.system(f"python News_sources_codes/home_gui.py {user_id}")

img_home = load_image("Image/home.png",70, 65)
button_home = Button(frame_button, image=img_home, bd=0, highlightthickness=0, command=lambda:onlick_home(root))
button_home.grid(row=0, column=0, padx=65, pady=10)

empty_space1 = Label(frame_button)
empty_space1.grid(row=0, column=1, padx=530)

def onclick_summary(summary):
    os.system(f"python News_sources_codes/summary_gui.py \"{summary}\"")

img_summary = load_image("Image/summary.png", 70, 65)
button_summary = Button(frame_button, image=img_summary, bd=0, highlightthickness=0, command=lambda: onclick_summary(current_news.SUMMARY))
button_summary.grid(row=0, column=2, padx=65, pady=10)

frame_news = Frame(content_frame, width=100, borderwidth=2, relief="groove")
frame_news.grid(row=1, column=0, padx=100)

date = current_news.DATE

# Check if date is available
if date is not None:
    if isinstance(date, str):
        # Parse the date string into a datetime object
        date_obj = datetime.strptime(date, "%Y-%m-%d %H:%M")
        formatted_date = "🕛 " + date_obj.strftime("%d %B %Y")
    else:
        formatted_date = ""
else:
    formatted_date = ""

author = "| By " + current_news.AUTHOR



# set anchor to center and wraplength to 300 pixels
tittle = Label(frame_news, text=current_news.TITTLE, width=80, anchor="center", wraplength=900, font=('Arial', 20, 'bold'))

tittle.grid(row=0, column=0)


label_date = Label(frame_news, text= formatted_date, fg="grey" ,font=('Arial', 12))
label_date.grid(row=1, column=0)


label_aurthor = Label(frame_news, text=author, fg="grey" ,font=('Arial', 12),wraplength=900)
label_aurthor.grid(row=2, column=0)

empty_space3 = Label(frame_news)
empty_space3.grid(row=3, column=0)

# Assuming NEWS_PIC contains a hexadecimal string
image_data = binascii.unhexlify(current_news.NEWS_PIC)
img_path = BytesIO(image_data)
img_news = load_image_url(img_path, 500, 300)

label_img_news = Label(frame_news, image=img_news)
label_img_news.image = img_news  # Store a reference to prevent image from being garbage collected
label_img_news.grid(row=4, column=0, pady=10)

empty_space4 = Label(frame_news)
empty_space4.grid(row=5, column=0)


frame_text = Frame(frame_news, width=100)
frame_text.grid(row=6, column=0, pady=20)



# Set anchor to center and wraplength to 900 pixels
text_label = Label(frame_text, text=current_news.CONTENT, font=('Arial', 12), wraplength=900, justify="left")
text_label.pack()

def open_url():
    webbrowser.open(current_news.URL)

button_ori = Button(frame_text, text="See Original", font=('Arial', 12), justify="center", command=open_url)
button_ori.pack(pady=50)

empty_space5 = Label(frame_news)
empty_space5.grid(row=7, column=0, pady=50)

#-------------------------------------------------------------------------------------------------------
# Update the canvas scroll region
canvas.create_window((0, 0), window=content_frame, anchor=NW)
content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
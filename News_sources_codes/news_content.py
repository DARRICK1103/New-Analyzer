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
import subprocess

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

if len(sys.argv) < 4:
    print("Usage: python news_content.py <url> <category> <user_id>")
    sys.exit(1)

url = sys.argv[1]
category_news = sys.argv[2]
user_id = sys.argv[3]


# download the news using the url
article, img_url = NewsAnalyzer.getContent(url)
title = article.title # tittle of the news
date = article.publish_date
author = article.authors
summary = article.summary
content = article.text

# -------------------------------------------------------------------------------------------
# database
cat = category.get(category_news)

# Download the image from the URL
response = requests.get(img_url, stream=True)
response.raise_for_status()

# Get the image binary data
image_data = response.content

# Convert image_data to a hexadecimal string
image_hex = binascii.hexlify(image_data).decode()

authors_str = ', '.join(article.authors)

# Create a News object with the image data
new = news.News("", authors_str, article.publish_date, content, summary, url, cat.CATEGORY_ID, '1', image_hex, title)

news.insert(new)

news_id = news.getID()
# Get the current date and time
today_date_time = datetime.now()

# Convert the date and time to a string representation if needed
today_date_time_str = today_date_time.strftime("%Y-%m-%d %H:%M:%S")

# Assuming the read_history function takes the following parameters:
# read_history(news_content, user_id, news_id, date_time, status)
his_new = read_history.History("", user_id, news_id, today_date_time_str, '1')
read_history.insert(his_new)

# -------------------------------------------------------------------------------------------

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

def onclick_summary(news_id):
    subprocess.Popen(["python", "News_sources_codes/summary_gui.py", str(news_id)])

img_summary = load_image("Image/summary.png", 70, 65)
button_summary = Button(frame_button, image=img_summary, bd=0, highlightthickness=0, command=lambda: onclick_summary(news_id))
button_summary.grid(row=0, column=2, padx=65, pady=10)

frame_news = Frame(content_frame, width=100, borderwidth=2, relief="groove")
frame_news.grid(row=1, column=0, padx=100)

# Check if publish_date is available
if isinstance(date, datetime):
    # Format the date
    formatted_date = "🕛 " + date.strftime("%d %B %Y")
else:
    formatted_date = ""


if author is not None and any(char.strip() for char in author):
    author = "| By " + ", ".join(author)
else:
    author = ""

img_path = 0
# Check if img_url is not None and has a valid scheme
if isinstance(img_url, str) and img_url.startswith(('http://', 'https://')):
    try:
        response = requests.get(img_url)
        response.raise_for_status()  # Check for any HTTP errors
        
        img_data = response.content
        img_file = BytesIO(img_data)
        img_path = img_file
    
    except requests.exceptions.SSLError as e:
        print(f"SSL error occurred for image ")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred for image ")
else:
    print(f"Invalid image URL for image ")




# set anchor to center and wraplength to 300 pixels
tittle = Label(frame_news, text=title, width=80, anchor="center", wraplength=900, font=('Arial', 20, 'bold'))

tittle.grid(row=0, column=0)


label_date = Label(frame_news, text= formatted_date, fg="grey" ,font=('Arial', 12))
label_date.grid(row=1, column=0)


label_aurthor = Label(frame_news, text=author, fg="grey" ,font=('Arial', 12),wraplength=900)
label_aurthor.grid(row=2, column=0)

empty_space3 = Label(frame_news)
empty_space3.grid(row=3, column=0)

img_news = load_image(img_path, 500, 300)
label_img_news = Label(frame_news, image=img_news)
label_img_news.grid(row=4, column=0, pady=10)

empty_space4 = Label(frame_news)
empty_space4.grid(row=5, column=0)


frame_text = Frame(frame_news, width=100)
frame_text.grid(row=6, column=0, pady=20)



# Set anchor to center and wraplength to 900 pixels
text_label = Label(frame_text, text=content, font=('Arial', 12), wraplength=900, justify="left")
text_label.pack()

def open_url():
    webbrowser.open(url)

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
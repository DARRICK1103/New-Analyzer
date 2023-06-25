import PIL
import user_manager
from tkinter import *
from PIL import Image, ImageTk
import news_structure1 as nw1
import news_date as ndate
import news_structure2 as nw2
import os
import newsAPI
import random
import requests
from PIL import Image
from io import BytesIO
import sys

if len(sys.argv) < 2:
    print("Usage: python home_gui.py <user_id>")
    sys.exit(1)

user_id = sys.argv[1]

print(user_id)

root = Tk()

root.title('Main Page')

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


# Create a canvas with scrollbars
canvas = Canvas(root)
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.config(yscrollcommand=scrollbar.set)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Create a frame to hold the content
content_frame = Frame(canvas)

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

# Create a frame with a black background
frame1 = Frame(content_frame, bg="#1C1C1C")
frame1.pack(fill="both", expand=False, side="top")

# Open image
img = Image.open("Image/news_icon.png")

# Resize image
new_img = img.resize((80, 65))

# Convert image to PhotoImage
photo_img = ImageTk.PhotoImage(new_img)

# Create a label and display the image on the frame
label = Label(frame1, image=photo_img, bg="#1C1C1C")

# Create buttons with custom font and colors
font = ("Arial", 12)
bg_color = "#4B4B4B"
fg_color = "#FFFFFF"

def onclick_trending(window):
    window.destroy()
    os.system(f"python News_sources_codes/trending_gui.py {user_id}")

def onclick_sports(window):
    window.destroy()
    os.system(f"python News_sources_codes/sports_gui.py {user_id}")

def onlick_entertainment(window):
    window.destroy()
    os.system(f"python News_sources_codes/entertainment_gui.py {user_id}")

def onclick_lifestyle(window):
    window.destroy()
    os.system(f"python News_sources_codes/lifestyle_gui.py {user_id}")


home_button = Button(frame1, text="Home", font=font, bg="white", fg="black", padx=15, pady=5, width=13)
trending_button = Button(frame1, text="Trending", font=font, bg=bg_color, fg=fg_color, padx=15, pady=5, width=13, command=lambda:onclick_trending(root))
sports_button = Button(frame1, text="Sports", font=font, bg=bg_color, fg=fg_color, padx=15, pady=5, width=13, command=lambda:onclick_sports(root))
entertainment_button = Button(frame1, text="Entertainment", font=font, bg=bg_color, fg=fg_color, padx=15, pady=5, width=13, command=lambda:onlick_entertainment(root))
lifestyle_button = Button(frame1, text="Technology", font=font, bg=bg_color, fg=fg_color, padx=15, pady=5, width=13, command=lambda:onclick_lifestyle(root))

# Create a frame for search bar
search_frame = Frame(frame1, padx=15, pady=5)

# Open and resize image
img2 = Image.open("Image/search.png")
new_img2 = img2.resize((20, 20))

# Convert image to PhotoImage
photo_img2 = ImageTk.PhotoImage(new_img2)

# Create search button and entry widget
search_entry = Label(search_frame,text="Search" ,font=font, bd=0, width=20, anchor=W)
#search_entry.insert(0, "Search")

def onclick_search(window):
    window.destroy()
    os.system(f"python News_sources_codes/search_gui.py {user_id}")

search_button = Button(search_frame, image=photo_img2, borderwidth=0, activebackground="#1C1C1C", command=lambda:onclick_search(root))

# Define function to perform search


# Open image
img3 = Image.open("Image/profile.png")

# Resize image
new_img3 = img3.resize((80, 65))

# Convert image to PhotoImage
photo_img3 = ImageTk.PhotoImage(new_img3)

def onclick_profile(window):
    window.destroy()
    os.system(f"python News_sources_codes/setting_gui.py {user_id}")

# Create a button and display the image on the frame
button3 = Button(frame1, image=photo_img3, bg="#1C1C1C",  command=lambda:onclick_profile(root))

# Arrange the elements with spacing and padding
label.grid(row=0, column=0, padx=10, pady=10)

button3.grid(row=0, column=1, padx=50)
home_button.grid(row=0, column=2, padx=15, pady=10)
trending_button.grid(row=0, column=3, padx=15, pady=10)
sports_button.grid(row=0, column=4, padx=15, pady=10)
entertainment_button.grid(row=0, column=5, padx=15, pady=10)
lifestyle_button.grid(row=0, column=6, padx=15, pady=10)
empty_space2 = Label(frame1, bg="#1C1C1C")
empty_space2.grid(row=0, column=7, padx=18)
search_entry.pack(side=LEFT)
search_button.pack(side=LEFT)
search_frame.grid(row=0, column=8, padx=10, pady=10)

frame2 = Frame(content_frame)

news_date = ndate.Date(frame2)
news_date.create()

# Arrange the elements
frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0)

frame_news1 = Frame(content_frame)
news = newsAPI.getNewsItem()

news1 = nw1.news1(news, frame_news1)
news1.create(user_id)

print(f"done first one")

frame_news1.grid(row=2, column=0)
frame3 = Frame(content_frame)

'''  Create a vertical straight line beside the label
# Create a vertical straight line
canvas = Canvas(frame3, width=2, height=30)
canvas.create_line(1, 0, 1, 30, fill='black')

label_news = Label(frame3, text="News")

# Arrange in grid for frame3
canvas.grid(row=0, column=0, padx=(5,0), pady=5) # Use padx to position the line to the left of the label
label_news.grid(row=0, column=1, pady=5)

'''

label_news = Label(frame3, text="Trending", font=("Arial", 16),padx=10, pady=10)
label_news.grid(row=0, column=0)
frame3.grid(row=3, column=0)

# Move label_news to the left
#label_news.grid(column=0)
remaining_news = news[5:]  # Store the remaining news items starting from index 5 until the end

frame4 = Frame(content_frame)
news2 = nw2.news2(frame4, remaining_news)
news2.create("General", user_id)
frame4.grid(row=4, column=0)
print("done trending")

# Frame 5 - Sport Label
frame5 = Frame(content_frame)
label_sports = Label(frame5, text="Sports", font=("Arial", 16),padx=10, pady=10)
label_sports.grid(row=0, column=0)
frame5.grid(row=5, column=0)
  
# Frame 6
frame6 = Frame(content_frame)
news_s = newsAPI.getSports() # get sports news
news3 = nw2.news2(frame6, news_s)
news3.create("Sports", user_id)
frame6.grid(row=6, column=0)
print("done sports")


# Frame 7 - Entertainment Label
frame7 = Frame(content_frame)
label_entertainment = Label(frame7, text="Entertainment", font=("Arial", 16),padx=10, pady=10)
label_entertainment.grid(row=0, column=0)
frame7.grid(row=7, column=0)

# Frame 8
frame8 = Frame(content_frame)
news_e = newsAPI.getEntertainment() # get entertainment 
news4 = nw2.news2(frame8, news_e)
news4.create("Entertainment", user_id)
frame8.grid(row=8, column=0)
print("done entertainment")

# Frame 9 - Lifestyle Label
frame9 = Frame(content_frame)
label_lifestyle = Label(frame9, text="Technology", font=("Arial", 16),padx=10, pady=10)
label_lifestyle.grid(row=0, column=0)
frame9.grid(row=9, column=0)


# Frame 10
frame10 = Frame(content_frame)
news_l = newsAPI.getTechnology()
news5 = nw2.news2(frame10, news_l)
news5.create("Technology", user_id)
frame10.grid(row=10, column=0)
print("done technology")


def onclick_refresh(window):
    window.destroy()
    os.system(f"python News_sources_codes/home_gui.py {user_id}")

# Create refresh button
button_refresh = Button(content_frame, text="Refresh", width=10, height=3, command=lambda:onclick_refresh(root))
button_refresh.grid(row=11, column=0, pady=15)

# Frame 11
frame11 = Frame(content_frame, bg="#1C1C1C", height=500)
description = Label(frame11, text="NewsNet aims to provide a deeper understanding and insight into current events.", fg="white", font=("Helvetica", 14), bg="#1C1C1C")
description.pack(pady=10)

right = Label(frame11, text="Copyright © 2023 by Darrick Tang, Zi Bin and Yu Xuan", fg="white", font=("Helvetica", 10), bg="#1C1C1C")
right.pack(pady=50)

frame11.grid(row=12, column=0, columnspan=3, sticky="ew", pady=10)


# Update the canvas scroll region
canvas.create_window((0, 0), window=content_frame, anchor=NW)
content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop() 
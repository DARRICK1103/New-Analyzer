import user_manager
from tkinter import *
from PIL import Image, ImageTk
import news_structure1 as nw1
import news_date as ndate
import news_structure2 as nw2
import os

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


def onclick_sports(window):
    window.destroy()
    os.system("python News_sources_codes/sports_gui.py")

def onclick_lifestyle(window):
    window.destroy()
    os.system("python News_sources_codes/lifestyle_gui.py")

def onlick_home(window):
    window.destroy()
    os.system("python News_sources_codes/home_gui.py")

def onclick_entertainment(window):
    window.destroy()
    os.system("python News_sources_codes/entertainment_gui.py")


home_button = Button(frame1, text="Home", font=font, bg=bg_color, fg=fg_color, padx=15, pady=5, width=13, command=lambda:onlick_home(root))
trending_button = Button(frame1, text="Trending", font=font, bg="white", fg="black", padx=15, pady=5, width=13)
sports_button = Button(frame1, text="Sports", font=font, bg=bg_color, fg=fg_color, padx=15, pady=5, width=13, command=lambda:onclick_sports(root))
entertainment_button = Button(frame1, text="Entertainment", font=font, bg=bg_color, fg=fg_color, padx=15, pady=5, width=13, command=lambda:onclick_entertainment(root))
lifestyle_button = Button(frame1, text="Lifestyle", font=font, bg=bg_color, fg=fg_color, padx=15, pady=5, width=13, command=lambda:onclick_lifestyle(root))


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
    os.system("python News_sources_codes/search_gui.py")

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
    os.system("python News_sources_codes/setting_gui.py")

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

label_trending = Label(frame2, text="Trending", font=('Arial', 25),)
label_trending.pack()
# Arrange the elements
frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0, sticky="W", padx=30, pady=10)

frame3 = Frame(content_frame)
img_path = "Image/news_row1_1.jpeg"
title = "We're in the AOL phase of artificial intelligence, tech CEO says, as industry raves about A.I."
structure1 = nw2.news2(frame3, img_path, img_path, img_path, title, "news", title)
structure1.create()
frame3.grid(row=2, column=0, pady=10)

frame4 = Frame(content_frame)
img_path = "Image/news_row1_1.jpeg"
title = "We're in the AOL phase of artificial intelligence, tech CEO says, as industry raves about A.I."
structure2 = nw2.news2(frame4, img_path, img_path, img_path, title, "news", title)
structure2.create()
frame4.grid(row=3, column=0, pady=10)

frame5 = Frame(content_frame)
img_path = "Image/news_row1_1.jpeg"
title = "We're in the AOL phase of artificial intelligence, tech CEO says, as industry raves about A.I."
structure3 = nw2.news2(frame5, img_path, img_path, img_path, title, "news", title)
structure3.create()
frame5.grid(row=4, column=0, pady=10)

frame6 = Frame(content_frame)
img_path = "Image/news_row1_1.jpeg"
title = "We're in the AOL phase of artificial intelligence, tech CEO says, as industry raves about A.I."
structure4 = nw2.news2(frame6, img_path, img_path, img_path, title, "news", title)
structure4.create()
frame6.grid(row=5, column=0, pady=10)

frame7 = Frame(content_frame)
img_path = "Image/news_row1_1.jpeg"
title = "We're in the AOL phase of artificial intelligence, tech CEO says, as industry raves about A.I."
structure5 = nw2.news2(frame7, img_path, img_path, img_path, title, "news", title)
structure5.create()
frame7.grid(row=6, column=0, pady=10)


# Create refresh button
button_refresh = Button(content_frame, text="Refresh", width=10, height=3)
button_refresh.grid(row=11, column=0, pady=15)

# Frame 11
frame11 = Frame(content_frame, bg="#1C1C1C", height=500)
description = Label(frame11, text="NewsNet aims to provide a deeper understanding and insight into current events.", fg="white", font=("Helvetica", 14), bg="#1C1C1C")
description.pack(pady=20)

right = Label(frame11, text="Copyright © 2023 by Darrick Tang, Zi Bin and Yu Xuan", fg="white", font=("Helvetica", 10), bg="#1C1C1C")
right.pack(pady=10)

frame11.grid(row=12, column=0, columnspan=3, sticky="ew", pady=10)

# Update the canvas scroll region
canvas.create_window((0, 0), window=content_frame, anchor=NW)
content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))



root.mainloop()

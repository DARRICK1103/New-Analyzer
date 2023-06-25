import user_manager
from tkinter import *
from PIL import Image, ImageTk
import news_structure1 as nw1
import news_date as ndate
import news_structure2 as nw2
import news_structure3 as nw3
import os
import newsAPI
import requests
from PIL import Image
from io import BytesIO
import sys

if len(sys.argv) < 2:
    print("Usage: python home_gui.py <user_id>")
    sys.exit(1)

user_id = sys.argv[1]

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

def onclick_home(window):
    window.destroy()
    os.system(f"python News_sources_codes/home_gui.py {user_id}")

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

home_button = Button(frame1, text="Home", font=font, bg=bg_color, fg=fg_color, padx=15, pady=5, width=13, command=lambda:onclick_home(root))
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

search_button = Button(search_frame, image=photo_img2, borderwidth=0, activebackground="#1C1C1C")
search_button.config(state="disabled")
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

# -----------------------------------------------------------------------------------------------

frame2 = Frame(content_frame)
new_img4 = img2.resize((35, 35))

# Convert image to PhotoImage
photo_img4 = ImageTk.PhotoImage(new_img4)

def clear_text(event):
    search_entry2.delete(0, "end")

# Create search button and entry widget
search_entry2 = Entry(frame2, font=('Arial', 25), bd=0, width=28, justify=LEFT)
search_entry2.insert(0, "Search")
search_entry2.bind("<FocusIn>", clear_text)
frame3 = Frame(content_frame)

web_img = []  # store image path
tittle = []  # store title
url = []

button_frame = None
button_frame2 = None
button_frame3 = None
button_frame4 = None

def get_entry_text(entry_widget):
    text = entry_widget.get()
    print(text)
    news = newsAPI.searchNews(text)
    if news is not None:
        for i in range(len(news)):
            img_url = news[i]['urlToImage']
            
            # Check if img_url is not None and has a valid scheme
            if isinstance(img_url, str) and img_url.startswith(('http://', 'https://')):
                try:
                    response = requests.get(img_url)
                    response.raise_for_status()  # Check for any HTTP errors
                    
                    img_data = response.content
                    img_file = BytesIO(img_data)
                    web_img.append(img_file)
                    tittle.append(news[i]['title'])
                    url.append(news[i]['url'])
                    if len(web_img) >=8:
                        break
                except requests.exceptions.SSLError as e:
                    print(f"SSL error occurred for image {i + 1}: {str(e)}")
                except requests.exceptions.RequestException as e:
                    print(f"Error occurred for image {i + 1}: {str(e)}")
            else:
                print(f"Invalid image URL for image {i + 1}")

    result = len(web_img)
    print(f"{result} results found")

    def onclick(window, news_url):
        # Find the root window
        root = window.winfo_toplevel()
        
        # Destroy the root window
        root.destroy()
        category = "General"
        # Open a new window for news_content.py
        os.system(f"python News_sources_codes/news_content.py {news_url} {category} {user_id}")
    
    if result >= 4:
        button_frame = nw3.ButtonFrame(frame3, web_img[0], tittle[0], '', command=lambda: onclick(root, url[0]))
        button_frame2 = nw3.ButtonFrame(frame3, web_img[1], tittle[1], '', command=lambda: onclick(root, url[1]))
        button_frame.grid(row=0, column=0, pady=3, padx=10)
        button_frame2.grid(row=1, column=0, pady=3, padx=10)
        
        button_frame3 = nw3.ButtonFrame(frame3, web_img[2], tittle[2], '', command=lambda: onclick(root, url[2]))
        button_frame4 = nw3.ButtonFrame(frame3, web_img[3], tittle[3], '', command=lambda: onclick(root, url[3]))

        button_frame3.grid(row=0, column=1, pady=5, padx=10)
        button_frame4.grid(row=1, column=1, pady=5, padx=10)

        result_label = Label(content_frame, text=f"{result} results found")
        result_label.grid(row=3, column=0, columnspan=2, sticky="nsew")
        if result != 4:
            def onclickMore():
                # Remove all widgets from the frame
                for widget in frame3.winfo_children():
                    widget.destroy()
                global web_img, url, tittle
                # TO DO: CHANGE LEN SIZE + CHANGE BUTTONFRAME
                if len(web_img) >= 1:
                 # Update the image and text in button_frame
                    button_frame = nw3.ButtonFrame(frame3, web_img[4], tittle[4], '', command=lambda: onclick(root, url[4]))
                    button_frame.grid(row=0, column=0, pady=3, padx=10)
               

                if len(web_img) >= 2:
                    # Update the image and text in button_frame2
                    button_frame2 = nw3.ButtonFrame(frame3, web_img[5], tittle[5], '', command=lambda: onclick(root, url[5]))
                    button_frame2.grid(row=1, column=0, pady=3, padx=10)
     

                if len(web_img) >= 3:
                    # Update the image and text in button_frame3
                    button_frame3 = nw3.ButtonFrame(frame3, web_img[6], tittle[6], '', command=lambda: onclick(root, url[6]))
                    button_frame3.grid(row=0, column=1, pady=5, padx=10)
           

                if len(web_img) >= 4:
                    # Update the image and text in button_frame4
                    button_frame4 = nw3.ButtonFrame(frame3, web_img[7], tittle[7], '', command=lambda: onclick(root, url[7]))
                    button_frame4.grid(row=1, column=1, pady=5, padx=10)
           
                

            button_more = Button(content_frame, text="More", bg="black", fg="white", bd=3, width=20, font=font, height=2, command=onclickMore)
            button_more.grid(row=4, column=0, sticky="E", padx=88,pady=35)
    elif result == 3:
        button_frame = nw3.ButtonFrame(frame3, web_img[0], tittle[0], '', command=lambda: onclick(root, url[0]))
        button_frame2 = nw3.ButtonFrame(frame3, web_img[1], tittle[1], '', command=lambda: onclick(root, url[1]))
        button_frame.grid(row=0, column=0, pady=3, padx=10)
        button_frame2.grid(row=1, column=0, pady=3, padx=10)
        button_frame3 = nw3.ButtonFrame(frame3, web_img[2], tittle[2], '', command=lambda: onclick(root, url[2]))
        button_frame3.grid(row=0, column=1, pady=5, padx=10)
    elif result == 2:
        button_frame = nw3.ButtonFrame(frame3, web_img[0], tittle[0], '', command=lambda: onclick(root, url[0]))
        button_frame2 = nw3.ButtonFrame(frame3, web_img[1], tittle[1], '', command=lambda: onclick(root, url[1]))
        button_frame.grid(row=0, column=0, pady=3, padx=10)
        button_frame2.grid(row=1, column=0, pady=3, padx=10)
    elif result == 1:
        button_frame = nw3.ButtonFrame(frame3, web_img[0], tittle[0], '', command=lambda: onclick(root, url[0]))
        button_frame.grid(row=0, column=0, pady=3, padx=10)
    else:
        next
    

search_button2 = Button(frame2, image=photo_img4, borderwidth=0, activebackground="#1C1C1C", command=lambda: get_entry_text(search_entry2))

search_entry2.pack(side=LEFT, padx=5)
search_button2.pack(side=LEFT,padx=5)

frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0, pady=30)
# Add the frame to the content frame grid
frame3.grid(row=2, column=0)
#---------------------------------------------------------------------------------------

# Disable scrollbar if content is shorter than canvas
content_height = content_frame.winfo_reqheight()
canvas_height = canvas.winfo_height()
if content_height <= canvas_height:
    scrollbar.config(command=None)
    canvas.unbind_all("<MouseWheel>")

# Update the canvas scroll region
canvas.create_window((0, 0), window=content_frame, anchor=NW)
content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()

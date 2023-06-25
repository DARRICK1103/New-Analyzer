from tkinter import *
from PIL import Image, ImageTk
import newsAPI
import random
import requests
from PIL import Image
from io import BytesIO
import time
import os

def load_image(file_path):
    img = Image.open(file_path)
    new_img = img.resize((375, 150))
    photo_img = ImageTk.PhotoImage(new_img)
    return photo_img

class news2:
    def __init__(self, root, news):
        self.root = root
        self.news = news

        # Keep a reference to the PhotoImage objects
        self.c1 = None
        self.c2 = None
        self.c3 = None
        self.current = 0
    
    def setCurrent(self, i):
        self.current = i

    def getCurrent(self):
        return self.current

    def create(self, category, user_id):

        web_img = []  # store image path
        tittle = []  # store title
        url = []
        for i in range(min(15, len(self.news))):
            img_url = self.news[i]['urlToImage']
            
            # Check if img_url is not None and has a valid scheme
            if isinstance(img_url, str) and img_url.startswith(('http://', 'https://')):
                try:
                    response = requests.get(img_url)
                    response.raise_for_status()  # Check for any HTTP errors
                    
                    img_data = response.content
                    img_file = BytesIO(img_data)
                    web_img.append(img_file)
                    tittle.append(self.news[i]['title'])
                    url.append(self.news[i]['url'])
                except requests.exceptions.SSLError as e:
                    print(f"SSL error occurred for image {i + 1}: {str(e)}")
                except requests.exceptions.RequestException as e:
                    print(f"Error occurred for image {i + 1}: {str(e)}")
            else:
                print(f"Invalid image URL for image {i + 1}")

            if len(web_img) == 3:
                self.setCurrent(i)
                break

        # Convert image to PhotoImage
        self.c1 = load_image(web_img[0])

        def onclick(window, url):
             # Find the root window
            root = window.winfo_toplevel()
            
            # Destroy the root window
            root.destroy()
            
            # Open a new window for news_content.py
            os.system(f"python News_sources_codes/news_content.py {url} {category} {user_id}")

        # Row 2 elements
        button_row2_1 = Button(self.root, text=tittle[0], font=('Arial', 10), image=self.c1, compound="top", wraplength=300, anchor="n", justify="center",command=lambda: onclick(self.root, url[0]))

    

        # Convert image to PhotoImage
        self.c2 = load_image(web_img[1])

        # Row 2 elements
        button_row2_2 = Button(self.root, text=tittle[1], font=('Arial', 10), image=self.c2, compound="top", wraplength=300, anchor="n", justify="center",command=lambda: onclick(self.root, url[1]))

      

        # Convert image to PhotoImage
        self.c3 = load_image(web_img[2])

        # Row 2 elements
        button_row2_3 = Button(self.root, text=tittle[2], font=('Arial', 10), image=self.c3, compound="top", wraplength=300, anchor="n", justify="center",command=lambda: onclick(self.root, url[2]))
        button_row2_1.grid(row=0, column=0, pady=10, padx=12)
        button_row2_2.grid(row=0, column=1, pady=10, padx=10)
        button_row2_3.grid(row=0, column=2, pady=10, padx=10)

        button_row2_1.config(height=200)
        button_row2_2.config(height=200)
        button_row2_3.config(height=200)

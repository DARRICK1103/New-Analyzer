from tkinter import *
from PIL import Image, ImageTk
import newsAPI
import random
import requests
from PIL import Image
from io import BytesIO
import time
import os


class news1:
    def __init__(self, articles, root):
        self.articles = articles
        self.root = root
        
        # Keep a reference to the PhotoImage objects
        self.row2_1 = None
        self.row2_2_1 = None
        self.row2_2_2 = None
        self.row2_2_3 = None
        self.row2_2_4 = None
    
    def create(self, user_id):
        global row2_1, row2_2_1, row2_2_2, row2_2_3, row2_2_4   
        web_img = []  # store image path
        tittle = []  # store title
        url = []
        start_time = time.time()
        for i in range(20):
            img_url = self.articles[i]['urlToImage']
            
            # Check if img_url is not None and has a valid scheme
            if isinstance(img_url, str) and img_url.startswith(('http://', 'https://')):
                try:
                    response = requests.get(img_url)
                    response.raise_for_status()  # Check for any HTTP errors
                    
                    img_data = response.content
                    img_file = BytesIO(img_data)
                    web_img.append(img_file)
                    tittle.append(self.articles[i]['title'])
                    url.append(self.articles[i]['url'])
                except requests.exceptions.SSLError as e:
                    print(f"SSL error occurred for image {i + 1}: {str(e)}")
                except requests.exceptions.RequestException as e:
                    print(f"Error occurred for image {i + 1}: {str(e)}")
            else:
                print(f"Invalid image URL for image {i + 1}")
            
            if len(web_img) == 8:
                break

        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Execution time: {execution_time} seconds")

        # Open and resize image
        img_row2_1 = Image.open(web_img[0])

        new_img_row2_1 = img_row2_1.resize((550, 250))

        # Convert image to PhotoImage
        row2_1 = ImageTk.PhotoImage(new_img_row2_1)

        def onclick(window, url):
             # Find the root window
            root = window.winfo_toplevel()
            
            # Destroy the root window
            root.destroy()
            
            category = "General"

            # Open a new window for news_content.py
            os.system(f"python News_sources_codes/news_content.py {url} {category} {user_id}")


        # Row 2 elements
        button_row2_1 = Button(self.root, text=tittle[0], font=('Arial', 10), image=row2_1, compound="top", wraplength=530, command=lambda: onclick(self.root, url[0]))


        # Second Frame on row 2
        frame_row2_2 = Frame(self.root)


        # Second Frame on row 2 - subframes
        frame_row2_2_1 = Frame(frame_row2_2)
        frame_row2_2_1.grid(row=0, column=0)

        frame_row2_2_2 = Frame(frame_row2_2)
        frame_row2_2_2.grid(row=0, column=1)

        frame_row2_2_3 = Frame(frame_row2_2)
        frame_row2_2_3.grid(row=1, column=0)

        frame_row2_2_4 = Frame(frame_row2_2)
        frame_row2_2_4.grid(row=1, column=1)


        # Open and resize image
        img_row2_2_1 = Image.open(web_img[1])
        new_img_row2_2_1 = img_row2_2_1.resize((300, 108))

        img_row2_2_2 = Image.open(web_img[2])
        new_img_row2_2_2 = img_row2_2_2.resize((300, 108))

        img_row2_2_3 = Image.open(web_img[3])
        new_img_row2_2_3 = img_row2_2_3.resize((300, 108))

        img_row2_2_4 = Image.open(web_img[4])
        new_img_row2_2_4 = img_row2_2_4.resize((300, 108))

      


        # Convert image to PhotoImage
        row2_2_1 = ImageTk.PhotoImage(new_img_row2_2_1)
        row2_2_2 = ImageTk.PhotoImage(new_img_row2_2_2)
        row2_2_3 = ImageTk.PhotoImage(new_img_row2_2_3)
        row2_2_4 = ImageTk.PhotoImage(new_img_row2_2_4)

        # Row 2 frame 2 button 1
        button_row2_2_1 = Button(frame_row2_2, text=tittle[1], font=('Arial', 10), image=row2_2_1, compound="top", wraplength=300, command=lambda: onclick(self.root, url[1]))
        button_row2_2_1.grid(row=0,column=0, padx=5, pady=5)
         
        # Row 2 frame 2 button 2
        button_row2_2_2 = Button(frame_row2_2, text=tittle[2], font=('Arial', 10), image=row2_2_2, compound="top", wraplength=300, command=lambda: onclick(self.root, url[2]))
        button_row2_2_2.grid(row=0, column=1, padx=5, pady=5)
                             
        # Row 2 frame 2 button 3
        button_row2_2_3 = Button(frame_row2_2, text=tittle[3], font=('Arial', 10),  image=row2_2_3, compound="top", wraplength=300, command=lambda: onclick(self.root, url[3]))
        button_row2_2_3.grid(row=1, column=0, padx=5, pady=5)

        # Row 2 frame 2 button 4
        button_row2_2_4 = Button(frame_row2_2, text=tittle[4], font=('Arial', 10),  image=row2_2_4, compound="top", wraplength=300, command=lambda: onclick(self.root, url[4]))
        button_row2_2_4.grid(row=1, column=1, padx=5, pady=5)


        # Row 2
        empty_space1 = Label(self.root)
        empty_space1.grid(row=0, column=0, padx=12)
        button_row2_1.grid(row=0, column=1, pady=10, padx=3)
        frame_row2_2.grid(row=0, column=2)

        button_row2_1.config(height=378)
        button_row2_2_1.config(height=180)
        button_row2_2_2.config(height=180)
        button_row2_2_3.config(height=180)
        button_row2_2_4.config(height=180)

       
from tkinter.ttk import Combobox, Style
import user_manager
from tkinter import *
from PIL import Image, ImageTk
import news_structure1 as nw1
import news_date as ndate
import news_structure2 as nw2
import os
import news_structure3 as nw3
import sys
from datetime import datetime
from tkinter import messagebox

def load_image(file_path, x, y):
    img = Image.open(file_path)
    new_img = img.resize((x, y))
    photo_img = ImageTk.PhotoImage(new_img)
    return photo_img


root = Tk()
root.title('Main Page')

content_frame1 = Frame(root)
content_frame1.grid(row=0, column=0, sticky="W", padx=25)

label = Label(content_frame1, text="User Login", font=('Arial', 20))
label.grid(row=0, column=0, padx=1, pady=3)


#----------------------------------------------------------------------
# Frame email

content_frame = Frame(root, borderwidth=2, relief="solid")
content_frame.grid(row=1, column=0, padx=26, pady=10)

#--------------------------------------------------------------------

frame_email = Frame(content_frame)
frame_email.grid(row=2, column=0, padx=10, pady=3, sticky="W")

label_email = Label(frame_email, text="Email ", font=('Arial', 12))
label_email.grid(row=0, column=0, padx=10, pady=5, sticky="W")


email = Entry(frame_email, width=30, font=('Arial', 11))
email.insert(0, "")


email.grid(row=1, column=0, padx=10)

#----------------------------------------------------------------------
# frame password

frame_password = Frame(content_frame)
frame_password.grid(row=3, column=0, padx=10, pady=3, sticky="W")

label_password = Label(frame_password, text="Password", font=('Arial', 12))
label_password.grid(row=0, column=0, padx=10, pady=5, sticky="W")

password = Entry(frame_password, width=30, font=('Arial', 11))
password.insert(0, "")
password.grid(row=1, column=0, padx=10)

empty = Label (content_frame)
empty.grid(row = 4, column=0, pady=3)
#----------------------------------------------------------------------

def onClick(window):
    if email.get() and password.get():
        user = user_manager.getLogin(email.get(), password.get())
        
        if user is None:
            messagebox.showinfo("Error", "Please make sure you type in your correct email and password.")
        else:
            user_id = user.USER_ID
            window.destroy()
            os.system(f"python News_sources_codes/home_gui.py {user_id}")
    else:
        messagebox.showinfo("Error", "Please fill in all the required fields.")

button_save = Button(root, text="Sign in", foreground='white', background='black', font=('Arial', 12), command=lambda:onClick(root))
button_save.grid(row=5, column=0, padx=25, pady=10, sticky="WE")

empty = Label(root)
empty.grid(row=7, column=0, padx=1, pady=3)

root.mainloop()
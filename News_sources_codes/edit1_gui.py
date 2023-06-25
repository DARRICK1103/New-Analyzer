from tkinter.ttk import Style
import user_manager
from tkinter import *
from PIL import Image, ImageTk
import news_structure1 as nw1
import news_date as ndate
import news_structure2 as nw2
import os
import news_structure3 as nw3
import sys
import requests
from PIL import Image
from io import BytesIO
from tkinter import filedialog
from tkinter import messagebox
import base64
'''
if len(sys.argv) < 2:
    print("Usage: python setting_gui.py <user_id>")
    sys.exit(1)

user_id = sys.argv[1]
'''
user_id = "U000000001"

def load_image(file_path, x, y):
    img = Image.open(file_path)
    new_img = img.resize((x, y))
    photo_img = ImageTk.PhotoImage(new_img)
    return photo_img


root = Tk()
root.title('Main Page')

content_frame = Frame(root)
content_frame.pack()

label = Label(content_frame, text="My Profile", font=('Arial', 20))
label.grid(row=0, column=0, padx=3, pady=3)

user = user_manager.get(user_id)
image_stream = BytesIO(user.PIC)

profile_img = load_image(image_stream, 145, 100)

label_profile = Label(content_frame, image=profile_img, text="", compound="top", highlightthickness=1, highlightbackground="black")

label_profile.grid(row=1, column=0, pady=3, padx=20)

label_file_path = Label(content_frame, text="", font=('Arial', 12))
label_file_path.grid(row=3, column=0, pady=10)

def on_upload_button_click():
    global file_path
    # Open file dialog to select an image file
    file_path = filedialog.askopenfilename(initialdir='Desktop', title='Select an image file', filetypes=(('Image Files', '*.png *.jpg *.jpeg *.gif'),))
    
    if file_path:
        # Update the label to display the selected file path
        
        uploaded_image = Image.open(file_path)
        resized_image = uploaded_image.resize((145, 100))
        profile_img = ImageTk.PhotoImage(resized_image)
        label_profile.configure(image=profile_img)
        label_profile.image = profile_img  # Store a reference to avoid garbage collection

# Create the "Upload" button
button_upload = Button(content_frame, text="Upload", command=on_upload_button_click)
button_upload.grid(row=2, column=0, pady=10)

frame_name = Frame(content_frame)
frame_name.grid(row=1, column=1, padx=4, pady=10)

label_name = Label(frame_name, text="Display Name: ", font=('Arial', 12))
label_name.grid(row=0, column=0, padx=40, pady=5)



name = Entry(frame_name, width=25)
name.insert(0, user.NAME)

name.grid(row=1, column=0)

def onClick(window):
    if name.get():
        current_user = user_manager.get(user_id)
        current_user.NAME = name.get()
        current_user.PIC = file_path

        # Update the user in the database
        user_manager.update(current_user)
        messagebox.showinfo("Success", "Updated user info")
    else:
        messagebox.showinfo("Error", "Error 404. Please try again!")

button_save = Button(content_frame, text="Save Changes", foreground='black', background='green', font=('Arial', 12), command=lambda:onClick(root))
button_save.grid(row=2, column=1, padx=10)

root.mainloop()

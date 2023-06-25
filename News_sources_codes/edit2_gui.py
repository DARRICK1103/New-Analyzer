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

content_frame1 = Frame(root)
content_frame1.grid(row=0, column=0, sticky="W", padx=25)

label = Label(content_frame1, text="My Info", font=('Arial', 20))
label.grid(row=0, column=0, padx=1, pady=3)


#----------------------------------------------------------------------
# Frame email

content_frame = Frame(root, borderwidth=2, relief="solid")
content_frame.grid(row=1, column=0, padx=26, pady=10)

frame_email = Frame(content_frame)
frame_email.grid(row=1, column=0, padx=10, pady=3, sticky="W")

label_email = Label(frame_email, text="Email ", font=('Arial', 12))
label_email.grid(row=0, column=0, padx=10, pady=5, sticky="W")

user = user_manager.get(user_id)

email = Entry(frame_email, width=25, font=('Arial', 11))
email.insert(0, user.EMAIL)


email.grid(row=1, column=0, padx=10)

#----------------------------------------------------------------------
# frame password

frame_password = Frame(content_frame)
frame_password.grid(row=2, column=0, padx=10, pady=3, sticky="W")

label_password = Label(frame_password, text="Password", font=('Arial', 12))
label_password.grid(row=0, column=0, padx=10, pady=5, sticky="W")

password = Entry(frame_password, width=25, font=('Arial', 11))
password.insert(0, user.PASSWORD)
password.grid(row=1, column=0, padx=10)


#----------------------------------------------------------------------
# Frame gender

frame_gender = Frame(content_frame)
frame_gender.grid(row=3, column=0, padx=10, pady=3, sticky="W")

label_gender = Label(frame_gender, text="Gender", font=('Arial', 12))
label_gender.grid(row=0, column=0, padx=10, pady=5, sticky="W")

gender_var = StringVar()
if user.GENDER == "MALE" or user.GENDER == "male":
    gender_var.set("female")
else:
    gender_var.set("male")
    

def toggle_gender():
    if gender_var.get() == "male":
        gender_var.set("female")
    else:
        gender_var.set("male")

male_button = Radiobutton(frame_gender, text="Male", variable=gender_var, value="male", font=('Arial', 11), fg="black", indicatoron=0, width=10, command=toggle_gender)
male_button.grid(row=1, column=0, padx=12)
male_button.config(foreground='white', background='black')

female_button = Radiobutton(frame_gender, text="Female", variable=gender_var, value="female", font=('Arial', 11), fg="black", indicatoron=0, width=10, command=toggle_gender)
female_button.grid(row=1, column=1)
female_button.config(foreground='white', background='black')


#----------------------------------------------------------------------
# Frame for birthday
frame_birthday = Frame(content_frame)
frame_birthday.grid(row=4, column=0, padx=10, pady=3)

# Label for birthday
label_birthday = Label(frame_birthday, text="Birthday", font=('Arial', 12))
label_birthday.grid(row=0, column=0, padx=10, pady=3, sticky="W")

# Label for day
label_month = Label(frame_birthday, text="Month", font=('Arial', 12))
label_month.grid(row=1, column=0, padx=11,  pady=3, sticky="W")

user_birthday = user.BIRTHDAY  # Assuming user.BIRTHDAY is already a datetime.date object

if user_birthday is not None:
    # Extract the month, day, and year as strings
    birthday_month = user_birthday.strftime("%m")
    birthday_day = user_birthday.strftime("%d")
    birthday_year = user_birthday.strftime("%Y")
else:
    birthday_month = '01'
    birthday_day = '00'
    birthday_year = '0000'

# create a list of months
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# create a Combobox for month selection
month = Combobox(frame_birthday, values=months, state="readonly", font=('Arial', 11), width=10)
month.current(int(birthday_month) - 1)  
month.grid(row=1, column=1, padx=10, pady=3)

# Label for day
label_day = Label(frame_birthday, text="Day", font=('Arial', 12))
label_day.grid(row=1, column=2, padx=10, pady=3)

# Entry field for day
day_entry = Entry(frame_birthday, width=5, font=('Arial', 11))
day_entry.insert(0, birthday_day)
day_entry.grid(row=1, column=3)

# Label for year
label_year = Label(frame_birthday, text="Year", font=('Arial', 12))
label_year.grid(row=1, column=4, padx=10, pady=3)

# Entry field for year
year_entry = Entry(frame_birthday, width=10, font=('Arial', 11))
year_entry.insert(0, birthday_year)
year_entry.grid(row=1, column=5)


#----------------------------------------------------------------------

def onClick(window):
    user_email = email.get()
    user.PASSWORD = password.get()
    if gender_var.get() == "male":
        user.GENDER = "female"
    else:
        user.GENDER = "male"

    selected_month = month.current() + 1  # Get the index of the selected month
    selected_day = int(day_entry.get())
    selected_year = int(year_entry.get())

    updated_birthday = f"{selected_year:04d}-{selected_month:02d}-{selected_day:02d}"
    user.BIRTHDAY = updated_birthday

    checkEmail = user_manager.check_email_duplicate(user_email)

    if (user_email != user.EMAIL) and (checkEmail is False):
        messagebox.showinfo("Error", "Email already exists. Please choose a different email.")
        print(checkEmail)
    elif (user_email == user.EMAIL) or (user_email != user.EMAIL and checkEmail is True):
        user.EMAIL = user_email
        user_manager.update(user)
        messagebox.showinfo("Success", "Updated user info")
    else:
        messagebox.showinfo("Error", "Error 404. Please try again!")

   

button_save = Button(root, text="Save Changes", foreground='black', background='green', font=('Arial', 12), command=lambda:onClick(root))
button_save.grid(row=5, column=0, padx=25, pady=10, sticky="E")

root.mainloop()
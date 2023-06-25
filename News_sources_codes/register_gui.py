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

label = Label(content_frame1, text="User Registration", font=('Arial', 20))
label.grid(row=0, column=0, padx=1, pady=3)


#----------------------------------------------------------------------
# Frame email

content_frame = Frame(root, borderwidth=2, relief="solid")
content_frame.grid(row=1, column=0, padx=26, pady=10)

#--------------------------------------------------------------------

# Name

frame_name = Frame(content_frame)
frame_name.grid(row=1, column=0, padx=10, pady=3, sticky="W")

label_name = Label(frame_name, text="Name ", font=('Arial', 12))
label_name.grid(row=0, column=0, padx=10, pady=5, sticky="W")


name = Entry(frame_name, width=30, font=('Arial', 11))
name.insert(0, "")


name.grid(row=1, column=0, padx=10)

#----------------------------------------------------------------------

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


#----------------------------------------------------------------------
# Frame gender

frame_gender = Frame(content_frame)
frame_gender.grid(row=4, column=0, padx=10, pady=3, sticky="W")

label_gender = Label(frame_gender, text="Gender", font=('Arial', 12))
label_gender.grid(row=0, column=0, padx=10, pady=5, sticky="W")


gender_var = StringVar()
gender_var.set("female")
    

def toggle_gender():
    if gender_var.get() == "male":
        gender_var.set("female")
    else:
        gender_var.set("male")

male_button = Radiobutton(frame_gender, text="Male", variable=gender_var, value="male", font=('Arial', 11), fg="black", indicatoron=0, width=12, command=toggle_gender)
male_button.grid(row=1, column=0, padx=11)
male_button.config(foreground='white', background='black')

female_button = Radiobutton(frame_gender, text="Female", variable=gender_var, value="female", font=('Arial', 11), fg="black", indicatoron=0, width=12, command=toggle_gender)
female_button.grid(row=1, column=1)
female_button.config(foreground='white', background='black')


#----------------------------------------------------------------------

# Frame for birthday
frame_birthday = Frame(content_frame)
frame_birthday.grid(row=6, column=0, padx=10, pady=3)

# Label for birthday
label_birthday = Label(frame_birthday, text="Birthday", font=('Arial', 12))
label_birthday.grid(row=0, column=0, padx=10, pady=3, sticky="W")

# Label for day
label_month = Label(frame_birthday, text="Month", font=('Arial', 12))
label_month.grid(row=1, column=0, padx=11,  pady=3, sticky="W")



# create a list of months
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# create a Combobox for month selection
month = Combobox(frame_birthday, values=months, state="readonly", font=('Arial', 11), width=10)
month.current(0)  
month.grid(row=1, column=1, padx=10, pady=3)

# Label for day
label_day = Label(frame_birthday, text="Day", font=('Arial', 12))
label_day.grid(row=1, column=2, padx=10, pady=3)

# Entry field for day
day_entry = Entry(frame_birthday, width=5, font=('Arial', 11))
day_entry.insert(0, "")
day_entry.grid(row=1, column=3)

# Label for year
label_year = Label(frame_birthday, text="Year", font=('Arial', 12))
label_year.grid(row=1, column=4, padx=10, pady=3)

# Entry field for year
year_entry = Entry(frame_birthday, width=10, font=('Arial', 11))
year_entry.insert(0, "")
year_entry.grid(row=1, column=5)


#----------------------------------------------------------------------

def onClick():
    
    user_name = name.get()
    user_email = email.get()
    user_password = password.get()
    if gender_var.get() == "male":
        user_gender = "female"
    else:
        user_gender = "male"
    selected_month = month.current() + 1  # Get the index of the selected month
    
    if user_name and user_email and user_password and user_gender and selected_month and day_entry.get() and year_entry.get():
       # Perform the desired actions when all entries are not empty
        selected_day = int(day_entry.get())
        selected_year = int(year_entry.get())

        user_birthday = f"{selected_year:04d}-{selected_month:02d}-{selected_day:02d}"
        if(user_gender == 'male'):
            img = 'Image/male_profile.png'
        else:
            img = 'Image/female_profile.png'
        checkEmail = user_manager.check_email_duplicate(user_email)
        if checkEmail is True:
            user = user_manager.User('', img, user_name, user_gender, user_birthday, user_email, user_password, '1')
            user_manager.insert(user)
            messagebox.showinfo("Success", "Sucessfully register a account.")
        else:
            messagebox.showinfo("Error", "Email already exists. Please choose a different email.")
         # Clear input fields
        name.delete(0, "end")
        email.delete(0, "end")
        password.delete(0, "end")
        gender_var.set("female")
        month.current(0)
        day_entry.delete(0, "end")
        year_entry.delete(0, "end")
    else:
        # Handle the case when any of the entries are empty
        messagebox.showinfo("Error", "Please fill in all the required fields.")



button_save = Button(root, text="Register", foreground='white', background='black', font=('Arial', 12), command=onClick)
button_save.grid(row=5, column=0, padx=25, pady=10, sticky="WE")

def goToLogin(window):
    window.destroy()
    os.system(f"python News_sources_codes/login_gui.py")

sign_in_label = Label(root, text="Already have an account? Sign in", fg="steel blue", cursor="hand2", font=('Arial', 12))
sign_in_label.grid(row=6, column=0, pady=10)


# Bind the function to the label
sign_in_label.bind("<Button-1>", lambda e: goToLogin(root))

empty = Label(root)
empty.grid(row=7, column=0, padx=1, pady=3)

root.mainloop()
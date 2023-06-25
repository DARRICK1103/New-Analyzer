from tkinter import *
from PIL import Image, ImageTk

class ButtonFrame(Frame):
    def __init__(self, parent, img_path, title, date, command=None):
        super().__init__(parent, bg='white', width=510, height=250)
        self.img_path = img_path
        self.title = title
        self.date = date
        self.command = command

        self.photo = None
        self.label = None
        self.title_label = None
        self.text_frame = None

        self.create_widgets()

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def create_widgets(self):
        # Load image and create PhotoImage object
        img = Image.open(self.img_path)
        img = img.resize((220, 200))
        self.photo = ImageTk.PhotoImage(img)

        # Create label with image
        self.label = Label(self, bg='white')
        self.label.config(image=self.photo)
        self.label.grid(row=0, column=0, rowspan=2, padx=10, pady=10)
        self.label.bind("<Button-1>", self.on_click)

        # Create text frame
        self.text_frame = Frame(self, bg='white', width=240, height=200)
        self.text_frame.grid(row=0, column=1, sticky=W, padx=10, pady=10)
        self.text_frame.pack_propagate(False)  # Fix size of text frame

        # Create title label
        self.title_label = Label(self.text_frame, text=self.title, font=('Arial', 12), bg='white', wraplength=170)
        self.title_label.pack(fill=BOTH, expand=True)
        self.title_label.bind("<Button-1>", self.on_click)

        # Create date label
        date_label = Label(self.text_frame, text=self.date, font=('Arial', 10), fg='gray', bg='white')
        date_label.pack(side=RIGHT)

    def on_enter(self, event):
        self.config(bg='lightgray')

    def on_leave(self, event):
        self.config(bg='white')

    def on_click(self, event):
        if self.command:
            self.command()

    def pack(self, **kwargs):
        super().pack(**kwargs)
        self.label.bind("<Button-1>", lambda event: self.event_generate("<Button-1>", when="tail"))
        self.label.bind("<Enter>", lambda event: self.event_generate("<Enter>", when="tail"))
        self.label.bind("<Leave>", lambda event: self.event_generate("<Leave>", when="tail"))
        self.title_label.bind("<Button-1>", lambda event: self.event_generate("<Button-1>", when="tail"))

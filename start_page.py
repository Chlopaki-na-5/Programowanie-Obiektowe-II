import tkinter as tk
from tkinter import ttk


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.frames = None
        self.controller = controller
        self.width = 50
        self.height = 10
        self.white = "white"
        self.image_button = tk.PhotoImage(file=r".\button.png")

        self.create()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    #center panel of center panel
    def center(self):
        m0 = tk.Label(frame_center, width=self.width * 3,
                      height=self.height * 5, background="lightblue",
                      text="Ekran startowy")
        m0.grid(row=0, column=0)

    #center panel
    def create_center(self):
        global frame_center
        frame_center = tk.Frame(self, highlightbackground="black", highlightthickness="5")
        self.center()
        frame_center.grid(row=1, column=1)

    #left panel with buttons
    def create_left(self):
        frame_left = tk.Frame(self, width=100)
        self.buttons(frame_left)
        frame_left.grid(row=1, column=0)

    #right panel with button
    def create_right(self):
        frame_right = tk.Frame(self, width=100)
        self.buttons(frame_right)
        frame_right.grid(row=1, column=2)

    def buttons(self, frame):
        width_image = 30
        height_image = 10

        image = self.image_button.zoom(19, 19).subsample(39)

        b0 = tk.Label(frame, width=width_image, height=height_image)
        b1_label = tk.Label(frame, width=width_image, height=height_image)
        b1 = tk.Button(b1_label, image=image, command=lambda: self.controller.show_frame(Bilet_page))
        b1.image = image

        b1.grid()

        b2 = tk.Label(frame, width=width_image, height=height_image)
        b3_label = tk.Label(frame, width=width_image, height=height_image)
        b3 = tk.Button(b3_label, image=image, command=lambda: self.controller.show_frame(Bilet_page))

        b3.grid()

        b4 = tk.Label(frame, width=width_image, height=height_image)

        b0.grid(row=0, column=0)
        b1_label.grid(row=1, column=0)
        b2.grid(row=2, column=0)
        b3_label.grid(row=3, column=0)
        b4.grid(row=4, column=0)

    def create(self):
        self.create_left()
        self.create_center()
        self.create_right()
        # self.frame.pack()
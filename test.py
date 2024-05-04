import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 35)
width_of_label = 50
height_of_label = 10

width_image = 30
height_image = 10
white = 'white'

def whiteLabel():
    return tk.Label(frame_center, width=width_of_label, height=height_of_label,
                      background=white, padx=0, pady=0, highlightthickness="0")

class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=False)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Bilet_page):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, padx=0, pady=0)

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.frames = None
        self.controller = controller
        self.white = "white"
        self.image_button = tk.PhotoImage(file=r".\button.png")

        self.create()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    #center panel of center panel
    def center(self):
        m0 = tk.Label(frame_center, width=width_of_label*3, height=height_of_label*5 + 1,
                      background="lightblue",
                      text="Ekran startowy", padx=0, pady=0)
        m0.grid(row=0, column=0)

    #center panel
    def create_center(self):
        global frame_center
        frame_center = tk.Frame(self,
                                highlightbackground="black", highlightthickness="5", padx=0, pady=0)
        self.center()
        frame_center.grid(row=0, column=1, padx=0, pady=0)

    #left panel with buttons
    def create_left(self):
        frame_left = tk.Frame(self, width=100, padx=0, pady=0)
        self.buttons(frame_left)
        frame_left.grid(row=0, column=0, padx=0, pady=0)

    #right panel with button
    def create_right(self):
        frame_right = tk.Frame(self, width=100, padx=0, pady=0)
        self.buttons(frame_right)
        frame_right.grid(row=0, column=2, padx=0, pady=0)

    def buttons(self, frame):

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

class Bilet_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.frames = None
        self.controller = controller
        self.white = "white"
        self.image_button = tk.PhotoImage(file=r".\button.png")
        self.create()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def buttons(self, frame):
        width_image = 30
        height_image = 10

        image = self.image_button.zoom(19, 19).subsample(39)

        b0 = tk.Label(frame, width=width_image, height=height_image)
        b1_label = tk.Label(frame, width=width_image, height=height_image)
        b1 = tk.Button(b1_label, image=image,
                       command=lambda: self.controller.show_frame(StartPage))
        b1.image = image

        b1.grid()

        b2 = tk.Label(frame, width=width_image, height=height_image)
        b3_label = tk.Label(frame, width=width_image, height=height_image)
        b3 = tk.Button(b3_label, image=image)

        b3.grid()

        b4 = tk.Label(frame, width=width_image, height=height_image)

        b0.grid(row=0, column=0)
        b1_label.grid(row=1, column=0)
        b2.grid(row=2, column=0)
        b3_label.grid(row=3, column=0)
        b4.grid(row=4, column=0)

    def left(self):
        l0 = whiteLabel()
        l1 = tk.Label(frame_center, width=width_of_label, height=height_of_label, background="lightblue",
                      text="Bilet Ulgowy")
        l2 = whiteLabel()
        l3 = tk.Label(frame_center, width=width_of_label, height=height_of_label, background="lightblue")
        l4 = whiteLabel()
        l0.grid(row=0, column=0)
        l1.grid(row=1, column=0)
        l2.grid(row=2, column=0)
        l3.grid(row=3, column=0)
        l4.grid(row=4, column=0)

    def center(self):
        m0 = whiteLabel()
        m1 = whiteLabel()
        m2 = whiteLabel()
        m3 = whiteLabel()
        m4 = whiteLabel()
        m0.grid(row=0, column=1)
        m1.grid(row=1, column=1)
        m2.grid(row=2, column=1)
        m3.grid(row=3, column=1)
        m4.grid(row=4, column=1)

    def right(self):
        r0 = whiteLabel()
        r1 = tk.Label(frame_center, width=width_of_label, height=height_of_label, background="lightblue",
                      text="Bilet Normalny")
        r2 = whiteLabel()
        r3 = tk.Label(frame_center, width=width_of_label, height=height_of_label, background="lightblue")
        r4 = whiteLabel()

        r0.grid(row=0, column=2)
        r1.grid(row=1, column=2)
        r2.grid(row=2, column=2)
        r3.grid(row=3, column=2)
        r4.grid(row=4, column=2)

    def create_center(self):
        global frame_center
        frame_center = tk.Frame(self, highlightbackground="black",
                                highlightthickness="5", padx=0, pady=0)
        self.left()
        self.center()
        self.right()
        frame_center.grid(row=0, column=1)

    def create_right(self):
        frame_right = tk.Frame(self, width=100, padx=0, pady=0)
        self.buttons(frame_right)
        frame_right.grid(row=0, column=2)

    def create_left(self):
        frame_left = tk.Frame(self, width=100, padx=0, pady=0)
        self.buttons(frame_left)
        frame_left.grid(row=0, column=0)

    def create(self):
        self.create_left()
        self.create_center()
        self.create_right()
        # self.frame.pack()


# Driver Code
app = tkinterApp()
app.mainloop()

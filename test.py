import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 35)
width_of_label = 50
height_of_label = 10

width_image = 30
height_image = 10
white = 'white'


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Bilet(metaclass=SingletonMeta):
    ilosc = 0
    is_normalne = None

    def change_count(self, how_many):
        print("Before ", self.ilosc)
        if (self.ilosc + how_many >= 0):
            self.ilosc += how_many
            print(self.ilosc)


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
        for F in (StartPage, Bilet_page, Ilosc_Biletow_page, Pay_page):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, bilet_page respectively with
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
        self.image = tk.PhotoImage(file=r".\image1.png")

        self.create()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    # left panel with buttons
    def create_left(self):
        frame_left = tk.Frame(self, width=100, padx=0, pady=0)
        self.buttons(frame_left)
        frame_left.grid(row=0, column=0, padx=0, pady=0)

        # center panel
    def create_center(self):
        global frame_center
        frame_center = tk.Frame(self,
                                highlightbackground="black", highlightthickness="5", padx=0, pady=0)
        self.center()
        frame_center.grid(row=0, column=1, padx=0, pady=0)

        # right panel with button
    def create_right(self):
        frame_right = tk.Frame(self, width=100, padx=0, pady=0)
        self.buttons(frame_right)
        frame_right.grid(row=0, column=2, padx=0, pady=0)

    #center panel of center panel
    def center(self):
        m0 = tk.Label(frame_center,padx=0, pady=0, image=self.image)
        m0.grid(row=0, column=0)



    def buttons(self, frame):
        width_image = 20
        height_image = 7

        image = self.image_button.zoom(10, 10).subsample(39)

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
        self.image = tk.PhotoImage(file=r".\image2.png")

        self.create()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


    def change_page(self, choose):
        bilet = Bilet()
        bilet.is_normalne = choose
        self.controller.show_frame(Ilosc_Biletow_page)

    def buttons(self, frame, choose):
        width_image = 20
        height_image = 7

        image = self.image_button.zoom(10, 10).subsample(40)

        b0 = tk.Label(frame, width=width_image, height=height_image)
        b1_label = tk.Label(frame, width=width_image, height=height_image)
        b1 = tk.Button(b1_label, image=image,
                       command=lambda: self.change_page(choose))
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

    def center(self):
        m0 = tk.Label(frame_center, padx=0, pady=0, image=self.image)
        m0.grid(row=0, column=0)


    def create_center(self):
        global frame_center
        frame_center = tk.Frame(self, highlightbackground="black",
                                highlightthickness="5", padx=0, pady=0)
        self.center()
        frame_center.grid(row=0, column=1)

    def create_right(self):
        frame_right = tk.Frame(self, padx=0, pady=0)
        self.buttons(frame_right, True)
        frame_right.grid(row=0, column=2)

    def create_left(self):
        frame_left = tk.Frame(self, padx=0, pady=0)
        self.buttons(frame_left, False)
        frame_left.grid(row=0, column=0)

    def create(self):
        self.create_left()
        self.create_center()
        self.create_right()

class Ilosc_Biletow_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.frames = None
        self.controller = controller
        self.white = "white"
        self.image_button = tk.PhotoImage(file=r".\button.png")
        self.image = tk.PhotoImage(file=r".\image3.png")

        self.create()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def change_count(self, how_many):
        bilet = Bilet()
        bilet.change_count(how_many)

    def change_page(self, page):
        if page == -1:
            self.controller.show_frame(Bilet_page)
        else:
            self.controller.show_frame(Pay_page)

    def buttons(self, frame, how_many_to_change):
        width_image = 20
        height_image = 7

        image = self.image_button.zoom(10, 10).subsample(39)

        b0 = tk.Label(frame, width=width_image, height=height_image)
        b1_label = tk.Label(frame, width=width_image, height=height_image)
        b1 = tk.Button(b1_label, image=image,
                       command=lambda: self.change_count(how_many_to_change))
        b1.image = image

        b1.grid()

        b2 = tk.Label(frame, width=width_image, height=height_image)
        b3_label = tk.Label(frame, width=width_image, height=height_image)
        b3 = tk.Button(b3_label, image=image,
                       command=lambda: self.change_page(how_many_to_change))

        b3.grid()

        b4 = tk.Label(frame, width=width_image, height=height_image)

        b0.grid(row=0, column=0)
        b1_label.grid(row=1, column=0)
        b2.grid(row=2, column=0)
        b3_label.grid(row=3, column=0)
        b4.grid(row=4, column=0)

    def center(self):
        m0 = tk.Label(frame_center, padx=0, pady=0, image=self.image)
        m0.grid(row=0, column=0)


    def create_center(self):
        global frame_center
        frame_center = tk.Frame(self, highlightbackground="black",
                                highlightthickness="5", padx=0, pady=0)
        self.center()
        frame_center.grid(row=0, column=1)

    def create_right(self):
        frame_right = tk.Frame(self, padx=0, pady=0)
        self.buttons(frame_right, 1)
        frame_right.grid(row=0, column=2)

    def create_left(self):
        frame_left = tk.Frame(self, padx=0, pady=0)
        self.buttons(frame_left, -1)
        frame_left.grid(row=0, column=0)

    def create(self):
        self.create_left()
        self.create_center()
        self.create_right()


class Pay_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.frames = None
        self.controller = controller
        self.white = "white"
        self.image_button = tk.PhotoImage(file=r".\button.png")
        self.image = tk.PhotoImage(file=r".\image3.png")

        self.create()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def change_count(self, how_many):
        bilet = Bilet()
        bilet.change_count(how_many)

    def change_page(self, page):
        if page == -1:
            self.controller.show_frame(Bilet_page)
        else:
            self.controller.show_frame(Pay_page)

    def buttons(self, frame, how_many_to_change):
        width_image = 20
        height_image = 7

        image = self.image_button.zoom(10, 10).subsample(39)

        b0 = tk.Label(frame, width=width_image, height=height_image)
        b1_label = tk.Label(frame, width=width_image, height=height_image)
        b1 = tk.Button(b1_label, image=image,
                       command=lambda: self.change_count(how_many_to_change))
        b1.image = image

        b1.grid()

        b2 = tk.Label(frame, width=width_image, height=height_image)
        b3_label = tk.Label(frame, width=width_image, height=height_image)
        b3 = tk.Button(b3_label, image=image,
                       command=lambda: self.change_page(how_many_to_change))

        b3.grid()

        b4 = tk.Label(frame, width=width_image, height=height_image)

        b0.grid(row=0, column=0)
        b1_label.grid(row=1, column=0)
        b2.grid(row=2, column=0)
        b3_label.grid(row=3, column=0)
        b4.grid(row=4, column=0)

    def center(self):
        m0 = tk.Label(frame_center, padx=0, pady=0, image=self.image)
        m0.grid(row=0, column=0)

    def create_center(self):
        global frame_center
        frame_center = tk.Frame(self, highlightbackground="black",
                                highlightthickness="5", padx=0, pady=0)
        self.center()
        frame_center.grid(row=0, column=1)

    def create_right(self):
        frame_right = tk.Frame(self, padx=0, pady=0)
        self.buttons(frame_right, 1)
        frame_right.grid(row=0, column=2)

    def create_left(self):
        frame_left = tk.Frame(self, padx=0, pady=0)
        self.buttons(frame_left, -1)
        frame_left.grid(row=0, column=0)

    def create(self):
        self.create_left()
        self.create_center()
        self.create_right()

# Driver Code
app = tkinterApp()
app.mainloop()

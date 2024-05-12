import tkinter as tk
from tkinter import ttk
import threading

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
    cena = 0

    def reset(self):
        self.ilosc = 0
        self.is_normalne = None
        self.cena = 0

    def change_count(self, how_many):
        if self.ilosc + how_many >= 0:
            self.ilosc += how_many

    def price(self):
        if self.is_normalne:
            self.cena = round((self.ilosc * 4.0), 2)
            print(type(self.cena))
            print(self.cena)
            return str(round(self.cena, 2)) + "0 zł"
        else:
            self.cena = round((self.ilosc * 2.0), 2)
            return str(self.cena) + "0 zł"

    def pay(self):
        if self.cena > 0:
            return str(self.cena) + "0 zł"
        else:
            return str(0) + " zł"


class TkinterApp(tk.Tk):

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
        for F in (StartPage, Bilet_page, Ilosc_Biletow_page, Pay_page, End_page):
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

class StartPage(tk.Frame, metaclass=SingletonMeta):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.frames = None
        self.controller = controller
        self.white = "white"
        self.image_button = tk.PhotoImage(file=r".\button.png")
        self.image = tk.PhotoImage(file=r".\image1.png")

        self.f_stop = threading.Event()

        self.create()

    def timer(self):
        if not self.f_stop.is_set():
            threading.Timer(60, self.restart).start()
        else:
            self.f_stop.set()
            threading.Timer(60, self.restart).start()

    def restart(self):
        bilet = Bilet()
        bilet.reset()
        ilosc_biletow = Ilosc_Biletow_page
        ilosc_biletow.text.set("Ilość biletów: " + str(bilet.ilosc))
        self.controller.show_frame(StartPage)
        self.timer()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    # left panel with buttons
    def create_left(self):
        frame_left = tk.Frame(self, padx=0, pady=0)
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
        frame_right = tk.Frame(self, padx=0, pady=0)
        self.buttons(frame_right)
        frame_right.grid(row=0, column=2, padx=0, pady=0)

    # center panel of center panel
    def center(self):
        m0 = tk.Label(frame_center, padx=0, pady=0, image=self.image)
        m0.grid(row=0, column=0)

    def create_space(self):
        frame_space = tk.Frame(self, width=450, padx=0, pady=0)
        frame_space.grid(row=0, column=3, padx=0, pady=0)

    def buttons(self, frame):
        width_image = 20
        height_image = 7

        image = self.image_button.zoom(10, 10).subsample(40)

        b0 = tk.Label(frame, width=width_image, height=height_image)
        b1_label = tk.Label(frame, width=width_image, height=height_image)
        b1 = tk.Button(b1_label, image=image, command=lambda: self.change_page())
        b1.image = image

        b1.grid()

        b2 = tk.Label(frame, width=width_image, height=height_image)
        b3_label = tk.Label(frame, width=width_image, height=height_image)
        b3 = tk.Button(b3_label, image=image, command=lambda: self.change_page())

        b3.grid()

        b4 = tk.Label(frame, width=width_image, height=height_image)

        b0.grid(row=0, column=0)
        b1_label.grid(row=1, column=0)
        b2.grid(row=2, column=0)
        b3_label.grid(row=3, column=0)
        b4.grid(row=4, column=0)

    def change_page(self):
        self.timer()
        self.controller.show_frame(Bilet_page)

    def create(self):
        self.create_left()
        self.create_center()
        self.create_right()
        self.create_space()
        # self.frame.pack()


class Bilet_page(tk.Frame, metaclass=SingletonMeta):

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
        startPage = StartPage()
        startPage.timer()
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

    def create_space(self):
        frame_space = tk.Frame(self, width=450, padx=0, pady=0)
        frame_space.grid(row=0, column=3, padx=0, pady=0)

    def create(self):
        self.create_left()
        self.create_center()
        self.create_right()
        self.create_space()


class Ilosc_Biletow_page(tk.Frame, metaclass=SingletonMeta):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.frames = None
        self.controller = controller
        self.white = "white"
        self.image_button = tk.PhotoImage(file=r".\button.png")
        self.image = tk.PhotoImage(file=r".\image3.png")
        self.text = tk.StringVar()

        self.create()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def change_count(self, how_many):
        bilet = Bilet()
        bilet.change_count(how_many)
        self.text.set("Ilość biletów: " + str(bilet.ilosc))

    def change_page(self, page):
        if page == -1:
            bilet = Bilet()
            bilet.reset()
            self.controller.show_frame(Bilet_page)
        else:
            bilet = Bilet()
            if bilet.ilosc > 0:
                p = Pay_page()
                p.text_end.set(bilet.price())
                startPage = StartPage()
                startPage.timer()
                self.controller.show_frame(Pay_page)

    def buttons(self, frame, how_many_to_change):
        width_image = 20
        height_image = 7

        image = self.image_button.zoom(10, 10).subsample(40)

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
        l1 = tk.Label(frame_center, padx=0, pady=0, textvariable=self.text, font=("Arial", 40))
        self.text.set("Ilość biletów: " + str(Bilet.ilosc))
        m0.grid(row=0, column=0)
        l1.grid(row=0, column=0)

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

    def create_space(self):
        frame_space = tk.Frame(self, width=450, padx=0, pady=0)
        frame_space.grid(row=0, column=3, padx=0, pady=0)

    def create(self):
        self.create_left()
        self.create_center()
        self.create_right()
        self.create_space()


class Pay_page(tk.Frame, metaclass=SingletonMeta):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.frames = None
        self.controller = controller
        self.white = "white"
        self.image_button = tk.PhotoImage(file=r".\button.png")
        self.image = tk.PhotoImage(file=r".\image4.png")
        self.text_end = tk.StringVar()

        self.create()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def change_count(self, how_many):
        bilet = Bilet()
        bilet.change_count(how_many)

    def change_page(self, page):
        if page == -1:
            self.controller.show_frame(Ilosc_Biletow_page)
        elif page != 0:
            self.controller.show_frame(End_page)
            bilet = Bilet()
            print("Reszta: " + str(abs(bilet.cena)))
            bilet.reset()
            ilosc_biletow = Ilosc_Biletow_page()
            ilosc_biletow.text.set("Ilość biletów: " + str(bilet.ilosc))
            self.after(5000, lambda: self.controller.show_frame(StartPage))

    def buttons(self, frame, page):
        width_image = 20
        height_image = 7

        image = self.image_button.zoom(10, 10).subsample(40)

        b0 = tk.Label(frame, width=width_image, height=height_image)
        b1_label = tk.Label(frame, width=width_image, height=height_image)
        b1 = tk.Button(b1_label, image=image)
        b1.image = image

        b1.grid()

        b2 = tk.Label(frame, width=width_image, height=height_image)
        b3_label = tk.Label(frame, width=width_image, height=height_image)
        b3 = tk.Button(b3_label, image=image,
                       command=lambda: self.change_page(page))

        b3.grid()

        b4 = tk.Label(frame, width=width_image, height=height_image)

        b0.grid(row=0, column=0)
        b1_label.grid(row=1, column=0)
        b2.grid(row=2, column=0)
        b3_label.grid(row=3, column=0)
        b4.grid(row=4, column=0)

    def center(self):
        bilet = Bilet()
        m0 = tk.Label(frame_center, padx=0, pady=0, image=self.image)
        l1 = tk.Label(frame_center, padx=0, pady=0, textvariable=self.text_end, font=("Arial", 40))
        self.text_end.set(bilet.price())
        m0.grid(row=0, column=0)
        l1.grid(row=0, column=0)

    def create_center(self):
        global frame_center
        frame_center = tk.Frame(self, highlightbackground="black",
                                highlightthickness="5", padx=0, pady=0)
        self.center()
        frame_center.grid(row=0, column=1)

    def create_right(self):
        frame_right = tk.Frame(self, padx=0, pady=0)
        self.buttons(frame_right, 0)
        frame_right.grid(row=0, column=2)

    def create_left(self):
        frame_left = tk.Frame(self, padx=0, pady=0)
        self.buttons(frame_left, -1)
        frame_left.grid(row=0, column=0)

    def change_value(self, how_much):
        bilet = Bilet()
        bilet.cena = round(bilet.cena - how_much, 2)
        self.text_end.set(bilet.pay())
        if bilet.cena <= 0:
            self.after(5000, lambda: self.change_page(1)
                       )

    def create_space(self):
        frame_space = tk.Frame(self, width=400, height=500, padx=0, pady=0)

        image_5zl = tk.PhotoImage(file=r".\5zl.png").zoom(20, 20).subsample(40)
        image_2zl = tk.PhotoImage(file=r".\2zl.png").zoom(20, 20).subsample(40)
        image_1zl = tk.PhotoImage(file=r".\1zl.png").zoom(20, 20).subsample(40)
        image_50gr = tk.PhotoImage(file=r".\50gr.png").zoom(20, 20).subsample(40)
        image_20gr = tk.PhotoImage(file=r".\20gr.png").zoom(20, 20).subsample(40)
        image_10gr = tk.PhotoImage(file=r".\10gr.png").zoom(20, 20).subsample(40)

        padding = 0

        b11 = tk.Button(frame_space, image=image_10gr,
                        command=lambda: self.change_value(0.1))
        b11.image = image_10gr
        b11.grid(row=0, column=0, padx=padding, pady=padding)

        b12 = tk.Button(frame_space, image=image_20gr,
                        command=lambda: self.change_value(0.2))
        b12.image = image_20gr
        b12.grid(row=0, column=1, padx=padding, pady=padding)

        b13 = tk.Button(frame_space, image=image_50gr,
                        command=lambda: self.change_value(0.5))
        b13.image = image_50gr
        b13.grid(row=0, column=2, padx=padding, pady=padding)

        b21 = tk.Button(frame_space, image=image_1zl,
                        command=lambda: self.change_value(1))
        b21.image = image_1zl
        b21.grid(row=1, column=0, padx=padding, pady=padding)

        b22 = tk.Button(frame_space, image=image_2zl,
                        command=lambda: self.change_value(2))
        b22.image = image_2zl
        b22.grid(row=1, column=1, padx=padding, pady=padding)

        b23 = tk.Button(frame_space, image=image_5zl,
                        command=lambda: self.change_value(5))
        b23.image = image_5zl
        b23.grid(row=1, column=2, padx=padding, pady=padding)

        frame_space.columnconfigure(1, minsize=189, weight=1)
        frame_space.rowconfigure(1, minsize=150, weight=1)
        frame_space.grid(row=0, column=3, padx=0, pady=0, sticky='we')
        frame_space.grid_columnconfigure(1, weight=1)

    def money(self, frame):
        width_image = 20
        height_image = 7

    def create(self):
        self.create_left()
        self.create_center()
        self.create_right()
        self.create_space()


class End_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.frames = None
        self.controller = controller
        self.white = "white"
        self.image_button = tk.PhotoImage(file=r".\button.png")
        self.image = tk.PhotoImage(file=r".\image5.png")

        self.create()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    # left panel with buttons
    def create_left(self):
        frame_left = tk.Frame(self, padx=0, pady=0)
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
        frame_right = tk.Frame(self, padx=0, pady=0)
        self.buttons(frame_right)
        frame_right.grid(row=0, column=2, padx=0, pady=0)

    # center panel of center panel
    def center(self):
        m0 = tk.Label(frame_center, padx=0, pady=0, image=self.image)
        m0.grid(row=0, column=0)

    def create_space(self):
        frame_space = tk.Frame(self, width=450, padx=0, pady=0)
        frame_space.grid(row=0, column=3, padx=0, pady=0)

    def buttons(self, frame):
        width_image = 20
        height_image = 7

        image = self.image_button.zoom(10, 10).subsample(40)

        b0 = tk.Label(frame, width=width_image, height=height_image)
        b1_label = tk.Label(frame, width=width_image, height=height_image)
        b1 = tk.Button(b1_label, image=image)
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

    def create(self):
        self.create_left()
        self.create_center()
        self.create_right()
        self.create_space()
        # self.frame.pack()


# Driver Code
app = TkinterApp()
app.mainloop()

#
# 1. (Done)Dodać powrót automatyczny do pierwszej strony
# 2. (Done)Poprawić End_page
# 3. (Done)Dodać okno z wydrukiem biletu?
# 4. (Done)Dodać chwilę, gdy pokazuje, że kwota została zapłacona i automatyczne przeniesienie do dalszej strony

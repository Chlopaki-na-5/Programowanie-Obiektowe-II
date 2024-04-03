import tkinter as tk
from tkinter import *


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Start_page, Bilet_page):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Start_page)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



def factory_page(page):
    match page:
        case 1:
            print("Factory work")
            #Start_page.StartBuilder().build()
            app = tkinterApp()
        case 2:
            print("Page 2")
            Bilet_page.BiletBuilder().build()
        case _:
            print("Page not found")

    app.mainloop()




master = Tk()
frame = tk.Frame(master, width=500)

class Start_page:

    def configure_master(self):
        self.master.geometry("1500x900")
        self.master.config(bg="white")
        self.master.title("Automat biletowy")

    def __init__(self, builder):

        self.width = builder.width
        self.height = builder.height
        self.white = builder.white
        self.master = builder.master

        self.configure_master()
        self.frame = builder.frame
        self.image_button = builder.image_button

    class StartBuilder:

        def __init__(self):
            self.master = Tk()
            self.width = 50
            self.height = 10
            self.frame = tk.Frame(self.master, width=500)
            self.white = "white"
            self.image_button = PhotoImage(file=r"C:\Users\Krecik\Desktop\pythonProject\button.png")

        def change_page(self, page):
            factory_page(page)

        def buttons(self, frame):
            width_image = 30
            height_image = 10

            image = self.image_button.zoom(19, 19).subsample(39)

            b0 = tk.Label(frame, width=width_image, height=height_image, background=self.white)
            b1_label = tk.Label(frame, width=width_image, height=height_image, background=self.white)
            b1 = tk.Button(b1_label, image=image, background=self.white, command= lambda : self.change_page(2))
            b1.image = image

            b1.grid()

            b2 = tk.Label(frame, width=width_image, height=height_image, background=self.white)
            b3_label = tk.Label(frame, width=width_image, height=height_image, background=self.white)
            b3 = tk.Button(b3_label, image=image)

            b3.grid()

            b4 = tk.Label(frame, width=width_image, height=height_image, background=self.white)

            b0.grid(row=0, column=0)
            b1_label.grid(row=1, column=0)
            b2.grid(row=2, column=0)
            b3_label.grid(row=3, column=0)
            b4.grid(row=4, column=0)

        def center(self):
            m0 = tk.Label(frame_center, width=self.width*3, height=self.height*5, background="lightblue", text="Ekran startowy")
            m0.grid(row=0, column=0)

        def create_center(self):
            global frame_center
            frame_center = tk.Frame(self.frame, highlightbackground="black", highlightthickness="5")
            self.center()
            frame_center.grid(row=1, column=1)

        def create_top(self):
            frame_top = tk.Frame(self.frame, height=50, background=self.white)
            frame_top.grid(row=0, column=0)

        def create_right(self):
            frame_right = tk.Frame(self.frame, width=100)
            self.buttons(frame_right)
            frame_right.grid(row=1, column=2)

        def create_left(self):
            frame_left = tk.Frame(self.frame, width=100)
            self.buttons(frame_left)
            frame_left.grid(row=1, column=0)


        def create(self):
            self.create_left()
            self.create_top()
            self.create_center()
            self.create_right()
            self.frame.pack()


        def build(self):
            self.create()
            mainloop()

class Bilet_page:

    def configure_master(self):
        self.master.geometry("1500x900")
        self.master.config(bg="white")
        self.master.title("Automat biletowy")

    def __init__(self, builder):
        self.width = builder.width
        self.height = builder.height
        self.white = builder.white
        self.master = builder.master

        self.configure_master()
        self.frame = builder.frame
        self.image_button = builder.image_button

    class BiletBuilder:

        def __init__(self):
            self.master = Tk()
            self.width = 50
            self.height = 10
            self.frame = tk.Frame(self.master, width=500)
            self.white = "white"
            self.image_button = PhotoImage(file=r"C:\Users\Krecik\Desktop\pythonProject\button.png")

        def change_page(self, page):
            factory_page(page)

        def buttons(self, frame):
            width_image = 30
            height_image = 10

            image = self.image_button.zoom(19, 19).subsample(39)

            b0 = tk.Label(frame, width=width_image, height=height_image, background=self.white)
            b1_label = tk.Label(frame, width=width_image, height=height_image, background=self.white)
            b1 = tk.Button(b1_label, image=image, background=self.white, command= lambda : self.change_page(2))
            b1.image = image

            b1.grid()

            b2 = tk.Label(frame, width=width_image, height=height_image, background=self.white)
            b3_label = tk.Label(frame, width=width_image, height=height_image, background=self.white)
            b3 = tk.Button(b3_label, image=image)

            b3.grid()

            b4 = tk.Label(frame, width=width_image, height=height_image, background=self.white)

            b0.grid(row=0, column=0)
            b1_label.grid(row=1, column=0)
            b2.grid(row=2, column=0)
            b3_label.grid(row=3, column=0)
            b4.grid(row=4, column=0)

        def left(self):
            l0 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            l1 = tk.Label(frame_center, width=self.width, height=self.height, background="lightblue",
                          text="Bilet Ulgowy")
            l2 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            l3 = tk.Label(frame_center, width=self.width, height=self.height, background="lightblue")
            l4 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            l0.grid(row=0, column=0)
            l1.grid(row=1, column=0)
            l2.grid(row=2, column=0)
            l3.grid(row=3, column=0)
            l4.grid(row=4, column=0)

        def center(self):
            m0 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            m1 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            m2 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            m3 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            m4 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            m0.grid(row=0, column=1)
            m1.grid(row=1, column=1)
            m2.grid(row=2, column=1)
            m3.grid(row=3, column=1)
            m4.grid(row=4, column=1)

        def right(self):
            r0 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            r1 = tk.Label(frame_center, width=self.width, height=self.height, background="lightblue",
                          text="Bilet Normalny")
            r2 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            r3 = tk.Label(frame_center, width=self.width, height=self.height, background="lightblue")
            r4 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)

            r0.grid(row=0, column=2)
            r1.grid(row=1, column=2)
            r2.grid(row=2, column=2)
            r3.grid(row=3, column=2)
            r4.grid(row=4, column=2)

        def create_center(self):
            global frame_center
            frame_center = tk.Frame(self.frame, highlightbackground="black", highlightthickness="5")
            self.left()
            self.center()
            self.right()
            frame_center.grid(row=1, column=1)

        def create_top(self):
            frame_top = tk.Frame(self.frame, height=50, background=self.white)
            frame_top.grid(row=0, column=0)

        def create_right(self):
            frame_right = tk.Frame(self.frame, width=100)
            self.buttons(frame_right)
            frame_right.grid(row=1, column=2)

        def create_left(self):
            frame_left = tk.Frame(self.frame, width=100)
            self.buttons(frame_left)
            frame_left.grid(row=1, column=0)


        def create(self):
            self.create_left()
            self.create_top()
            self.create_center()
            self.create_right()
            self.frame.pack()


        def build(self):
            self.create()
            mainloop()
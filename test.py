import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 35)


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
        for F in (StartPage, Bilet_page, Page2):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

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
        self.width = 50
        self.height = 10
        self.white = "white"
        self.image_button = tk.PhotoImage(file=r"C:\Users\Krecik\Desktop\pythonProject\button.png")

        self.create()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def center(self):
        m0 = tk.Label(frame_center, width=self.width * 3, height=self.height * 5, background="lightblue",
                      text="Ekran startowy")
        m0.grid(row=0, column=0)

    def create_center(self):
        global frame_center
        frame_center = tk.Frame(self, highlightbackground="black", highlightthickness="5")
        self.center()
        frame_center.grid(row=1, column=1, padx=20, pady=20)

    def create_left(self):
        frame_left = tk.Frame(self, width=100)
        self.buttons(frame_left)
        frame_left.grid(row=1, column=0)

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


# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 1", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


class Bilet_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.frames = None
        self.controller = controller
        self.width = 50
        self.height = 10
        self.white = "white"
        self.image_button = tk.PhotoImage(file=r"C:\Users\Krecik\Desktop\pythonProject\button.png")

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
        b1 = tk.Button(b1_label, image=image, background=self.white,
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
        frame_center = tk.Frame(self, highlightbackground="black", highlightthickness="5")
        self.left()
        self.center()
        self.right()
        frame_center.grid(row=1, column=1, padx=20, pady=20)

    def create_right(self):
        frame_right = tk.Frame(self, width=100)
        self.buttons(frame_right)
        frame_right.grid(row=1, column=2)

    def create_left(self):
        frame_left = tk.Frame(self, width=100)
        self.buttons(frame_left)
        frame_left.grid(row=1, column=0)

    def create(self):
        self.create_left()
        self.create_center()
        self.create_right()
        # self.frame.pack()


# Driver Code
app = tkinterApp()
app.mainloop()

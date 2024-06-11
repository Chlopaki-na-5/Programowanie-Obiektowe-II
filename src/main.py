import tkinter as tk
from gui_pages import StartPage, Bilet_page, Ilosc_Biletow_page, Pay_page, End_page

class State:
    current_page = None

class TkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=False)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for Page in (StartPage, Bilet_page, Ilosc_Biletow_page, Pay_page, End_page):
            frame = Page(container, self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, padx=0, pady=0)

        self.show_frame(StartPage)

    def show_frame(self, cont):
        for frame in self.frames.values():
            if frame.__class__.__name__ == cont.__name__:
                frame.grid(row=0, column=0, sticky="nsew")
            else:
                frame.grid_remove()


if __name__ == "__main__":
    app = TkinterApp()
    app.mainloop()

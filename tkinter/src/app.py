import logging
import tkinter as tk
import tkinter.ttk as ttk


logger = logging.getLogger("logger")


class App(tk.Tk):
    def init(self) -> None:
        self.title("Template")
        self.state("zoomed")
        self.minsize(200, 200)
        self.configure(background="white")

        self.createWidgets()


    def createWidgets(self) -> None:
        pass

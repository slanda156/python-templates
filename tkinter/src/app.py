import logging
import traceback
import tkinter as tk
import tkinter.messagebox as tkMessageBox

from src.widgets import Widget


logger = logging.getLogger(__name__)


class App(tk.Tk):
    def init(self) -> None:
        self.title("Template")
        self.state("zoomed")
        self.minsize(200, 200)
        self.configure(background="white")

        self.createWidgets()


    def createWidgets(self) -> None:
        self.widget = Widget(self)


    def report_callback_exception(self, *args):
        err = traceback.format_exception(*args)
        strErr = "\n".join(err)
        logger.error(strErr)
        tkMessageBox.showerror("Exception", str(err))

import csv
import os
from tkinter import *
import tkinter as tk
from tkinter import ttk
from WorkTime import workTime
from DynamicGrid import DynamicGrid


class mainGUI(tk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.grid()

        dynamicGrid = DynamicGrid(master)
        dynamicGrid.create_widgets()
        # dynamicGrid.add_row()

        

        self.submitButton = Button(master, command=self.buttonClick, text="Submit")
        self.submitButton.grid(column=0,row=1)

    def buttonClick(self):
        self.worktime = workTime()
        self.worktime.addWorkHours()
        pass

if __name__ == "__main__":
    root = tk.Tk()
    mainFrame = mainGUI(root)
    mainFrame.mainloop()
import tkinter as tk
from tkinter import Tk, Label, Button
import ctypes
import subprocess
import webbrowser
import sys

# Create the GUI for tkinter
class Application(tk.Frame):
    def method_name(self, master):
        return super().__init__(master)

    def __init__(self, master):
        self.method_name(master)
        self.master = master
        master.title("File Selector")
        self.pack()

        # Widget for README.
        self.readme = Button(master, text="Click me to README", command=self.greeting)
        self.readme.pack(side="top", pady=5)

        # Widget for file selection.
        self.file_selection = tk.Button(self, text="Create New File", command=self.NewFile)
        self.file_selection.pack(side="bottom", pady=5)


        #Widget for quit button.
        self.quit = tk.Button(self, text="Quit", fg="red", command=self.master.destroy, pady=5)
        self.quit.pack(side="bottom")


# Definition for saving and importing files.
    def NewFile(f):
        count = 0
        f = open("test.txt", "w+")
        for i in range(10):
            f.write("This is line %d\r\n" & (count + 1))
        webbrowser.open(f)
        f.close()
    def OpenFile():
        return 0
    def About():
        print("This is a simple example of a menu")
    def greeting(file):
        file.pack()
        #file = subprocess.Popen(["README.txt"])
        webbrowser.open("README.txt")


root = tk.Tk()
app = Application(master=root)
app.mainloop()

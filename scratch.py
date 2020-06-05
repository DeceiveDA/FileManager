import tkinter as tk
from tkinter import *
import ctypes
import subprocess
import webbrowser
import sys
import os

# Create the GUI for tkinter
class Application(tk.Frame):
    def method_name(self, master):
        return super().__init__(master)

    def __init__(self, master):
        self.method_name(master)
        master.title("File Selector")
        self.pack()
        bottomframe=Frame(master)
        bottomframe.pack(side = BOTTOM)


        # Widget for README.
        readme = Button(master, text="Click me to README", command=self.greeting)
        readme.pack(side=LEFT, pady=5, padx=5)

        # Widget for file selection.
        file_selection = tk.Button(self, text="Open File", command=self.OpenFile)
        file_selection.pack(side=LEFT, pady=5, padx=5)
        
        #Widget for quit button.
        quit = tk.Button(self, text="Quit", fg="red", command=self.master.destroy)
        quit.pack(side=LEFT, padx=5, pady=5)
        

# Definition for saving and importing files.
    def NewFile(file_selection):
        return 0
    def OpenFile(file_selection):
        usrInput = input()
        os.O_RDWR
        os.path
        print(os.path)
        if(os.path == None):
            print("The file was not found!")
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

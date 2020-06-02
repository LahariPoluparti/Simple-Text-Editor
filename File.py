from tkinter.filedialog import *
from tkinter import *
from tkinter import messagebox
import os


class File:
    text = ""
    filename = "no_file"

    def __init__(self, master,text_file):
        self.master = master
        self.text_file = text_file


    def new_file(self):
        self.text_file.delete("1.0", END)
        self.filename = "no_file"
        
    def save_as(self):
        global filepath
        global text
        filepath = asksaveasfilename(defaultextension=".txt",
            filetypes=[("All Files", "*.*"),
                       ("Text Files", "*.txt"),
                       ("Python Scripts", "*.py"),
                       ("Markdown Documents", "*.md"),
                       ("JavaScript Files", "*.js"),
                       ("HTML Documents", "*.html"),
                       ("CSS Documents", "*.css")])
        if not filepath:
            return

        text = self.text_file.get("1.0", END)
        with open(filepath, "w") as output_file:
            output_file.write(text)
            
        self.filename = filepath
        self.master.title(f"Text Editor - {filepath}")


    def save(self):
        if self.filename == "no_file":
            self.save_as()
        else:
            text = self.text_file.get("1.0", END)
            with open(filepath, "w") as output_file:
                output_file.write(text)

    def open_file(self):
        global filepath
        global text
        filepath = askopenfile(defaultextension=".txt",
            filetypes=[("All Files", "*.*"),
                       ("Text Files", "*.txt"),
                       ("Python Scripts", "*.py"),
                       ("Markdown Documents", "*.md"),
                       ("JavaScript Files", "*.js"),
                       ("HTML Documents", "*.html"),
                       ("CSS Documents", "*.css")])
        if not filepath:
            return
        self.text_file.delete("1.0", END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            self.text_file.insert(END, text)
            self.filename = filepath.name

        self.master.title(f"Text Editor - {filepath}")


    def exit(self):
        
        self.save()
        self.master.quit()



from tkinter.filedialog import *
from tkinter import *

class Edit:
    def __init__(self,master,text_edit):
        self.master = master
        self.text_edit = text_edit
    
    def cut(self):
        self.copy()
        self.text_edit.delete("sel.first", "sel.last")
    

    def copy(self):
        self.text_edit.clipboard_clear()
        self.text_edit.clipboard_append(self.text_edit.selection_get())

    def paste(self):
        self.text_edit.insert(INSERT, self.text_edit.clipboard_get())
        

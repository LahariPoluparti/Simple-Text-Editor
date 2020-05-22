from tkinter import *

#setting the window
root = Tk()
#sets the title to the center
blank_space = " "
root.title(blank_space * 110 + "Text Editor")
root.minsize(800,500) #the minimun size of the window
root.maxsize(800,500) #the maximum size it can go

#textediting
text_edit = Text(root, height=29.5, width = 100)
text_edit.pack()

#Menu bar
menu = Menu(root)
root.config(menu=menu)

sub_menu = Menu(menu)
menu.add_cascade(label="File", menu=sub_menu) #add_cascade -- dropdown
sub_menu.add_command(label="New File") #add options to the file
sub_menu.add_command(label="New Window")
sub_menu.add_command(label="Open")
sub_menu.add_command(label="Save")
sub_menu.add_command(label="Save As")
sub_menu.add_separator()
sub_menu.add_command(label="Exit")

edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu) #add_cascade -- dropdown
edit_menu.add_command(label="Cut") #add options to the file
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Replace")

format_menu = Menu(menu)
menu.add_cascade(label="Format", menu=format_menu) #add_cascade -- dropdown
format_menu.add_command(label="Font") #add options to the file

help_menu = Menu(menu)
menu.add_cascade(label="Help", menu=help_menu) #add_cascade -- dropdown
help_menu.add_command(label="About") #add options to the file

#status bar
status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)



root.mainloop()
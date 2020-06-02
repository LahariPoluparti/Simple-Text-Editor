from tkinter import *
from File import *
from Edit import *

#setting the window
root = Tk()
#sets the title to the center
blank_space = " "
root.title(blank_space * 110 + "Scribble")
root.minsize(800,500) #the minimun size of the window
#root.maxsize(800,500) #the maximum size it can go

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

#textediting
text_edit = Text(root, undo=True)
text_edit.pack(expand=True, fill=BOTH)

file_option = File(root, text_edit)
edit_option = Edit(root,text_edit)

#Menu bar
menu = Menu(root)
root.config(menu=menu)

sub_menu = Menu(menu)
menu.add_cascade(label="File", menu=sub_menu) #add_cascade -- dropdown
sub_menu.add_command(label="New File", command=file_option.new_file) #add options to the file
sub_menu.add_command(label="Open", command=file_option.open_file)
sub_menu.add_command(label="Save", command=file_option.save)
sub_menu.add_command(label="Save As", command=file_option.save_as)
sub_menu.add_separator()
sub_menu.add_command(label="Exit", command=file_option.exit)

edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu) #add_cascade -- dropdown
edit_menu.add_command(label="Undo", command=text_edit.edit_undo)
edit_menu.add_command(label="Redo", command=text_edit.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=edit_option.cut) #add options to the file
edit_menu.add_command(label="Copy", command=edit_option.copy)
edit_menu.add_command(label="Paste", command=edit_option.paste)


#status bar
status = Label(root, text="Welcome to Scribble...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()
#NOTEPAD MINI-PROJECT
#Importing necessary libraries
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
from datetime import datetime
from tkinter import filedialog
import webbrowser
root = Tk()

# GUI logic starts here
root.geometry("415x400")
root.title("Untitled-Notepad")
root.wm_iconbitmap("notepadicon1.ico")
# Scroll Bar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
# writing area in notepad
text = Text(root, font="TimesNewRoman 10", yscrollcommand=scrollbar.set,undo=True)
text.pack(fill="both", expand=True)
file = None
scrollbar.config(command=text.yview)

# mainMenu
mymenu = Menu(root)
yourmenubar = Menu(root)
# file option code starts here
def New():
    global file
    file = None
    root.title("Untitled-Notepad")
def Newwindow():
    root = Tk()
    root.geometry('413x550')
    root.title("New Notepad")
    text1 = Text(root, font="TimesNewRoman 10", yscrollcommand=scrollbar.set)
    text1.pack(fill="both", expand=True)
    root.wm_iconbitmap("notepadicon1.ico")
def Open():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " -Notepad")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()
def Save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        # Save the new file
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " -Notepad")
            print("File Saved")
            showinfo("Save", "Your file is saved")
    else:
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()
def save_as():
    root.filename = filedialog.asksaveasfile(mode="w", defaultextension='.txt')
    if root.filename is None:
        return
    file_save = str(text.get(1.0, END))
    root.filename.write(file_save)
    root.filename.close()
def exit():
    message = messagebox.askquestion('Notepad', "Do you want to save changes")
    if message == "yes":
        save_as()
    else:
        root.destroy()
#def find():
#   pass
m1 = Menu(yourmenubar, tearoff=0)
m1.add_command(label="New",accelerator="Ctrl+N", command=New)
m1.add_command(label="New window",accelerator="Ctrl+Shift+N",command=Newwindow)
m1.add_command(label="Open...",accelerator="Ctrl+O", command=Open)
m1.add_command(label="Save",accelerator="Ctrl+S", command=Save)
m1.add_command(label="Save As...",command=save_as,accelerator="Ctrl+Shift+S")
m1.add_separator()
# m1.add_command(label="Page Setup...",command=Pagesetup)
# m1.add_command(label="Find",command=find)
# m1.add_separator()
m1.add_command(label="Exit", command=exit)
yourmenubar.add_cascade(label="File", menu=m1)
root.config(menu=yourmenubar)
# file option code ends here

# edit option code starts here
def cut():
    text.event_generate(("<<Cut>>"))
def copy():
    text.event_generate(("<<Copy>>"))
def paste():
    text.event_generate(("<<Paste>>"))
def delete():
    message = messagebox.askquestion('Notepad', "Do you want to Delete all")
    if message == "yes":
        text.delete('1.0', 'end')
    else:
        return "break"
# def search():
#    pass
# def find():
#   pass
# def find_next():
#    pass
# def find_previous():
#    pass
# def replace():
#   pass
# def goto():
#    pass
def select_all():
    text.tag_add('sel', '1.0', 'end')
    return 'break'
def timedate():
    d = datetime.now()
    text.insert('end', d)
m2 = Menu(yourmenubar, tearoff=0)
m2.add_command(label="Undo",accelerator="Ctrl+Z",command=text.edit_undo)
m2.add_command(label="Cut",accelerator="Ctrl+X", command=cut)
m2.add_command(label="Copy",accelerator="Ctrl+C", command=copy)
m2.add_command(label="Paste",accelerator="Ctrl+V", command=paste)
m2.add_separator()
m2.add_command(label="Delete All",accelerator="Del", command=delete)
m2.add_separator()
# m2.add_command(label="Search with Bing...",command=search)
# m2.add_command(label="Find...",command=find)
# m2.add_separator()
# m2.add_command(label="Find Next",command=find_next)
# m2.add_command(label="Find Previous",command=find_previous)
# m2.add_command(label="Replace",command=replace)
# m2.add_command(label="Go To...",command=goto)
# m2.add_separator()
m2.add_command(label="Select All",accelerator="Ctrl+A",command=select_all)
m2.add_command(label="Time/Date",accelerator="F5",command=timedate)
yourmenubar.add_cascade(label="Edit", menu=m2)
root.config(menu=yourmenubar)
# edit option code ends here


# Format menu
# def wordwrap():
#   pass
# def font():
#   pass
# m3=Menu(yourmenubar,tearoff=0)
# m3.add_command(label="Word Wrap",command=wordwrap)
# m3.add_command(label="Font...",command=font)
# yourmenubar.add_cascade(label="Format",menu=m3)
# root.config(menu=yourmenubar)

# view option
# def zoom():
#    pass
# def statusbar():
#    pass
#m4=Menu(yourmenubar,tearoff=0)
#m4.add_command(label="Zoom",command=zoom)
# m4.add_command(label="Status Bar",command=statusbar)
# yourmenubar.add_cascade(label="View",menu=m4)
# root.config(menu=yourmenubar)

# help option code starts here
def viewhelp():
    webbrowser.open('https://binged.it/3w0gXhX')
def feedback():
    webbrowser.open('#')
def notepad():
    showinfo("Notepad", "Notepad made by Pranoti")
m5 = Menu(yourmenubar, tearoff=0)
m5.add_command(label="View Help", command=viewhelp)
m5.add_command(label="Send Feedback",command=feedback)
m5.add_command(label="About Notepad", command=notepad)
yourmenubar.add_cascade(label="Help", menu=m5)
root.config(menu=yourmenubar)
# help option code ends here
root.mainloop()



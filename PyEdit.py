from Tkinter import *
from tkFileDialog import *

filename = None
"""
Function to open a new file
"""
def newFile():
    global filename
    filename = "Untitled"
    #delete all text so far, 0th char at 0th line
    text.delete(0.0, END)

def saveFile():
    global filename
    try:
        t = text.get(0.0, END)
        #open filename with write permisions
        f = open(filename, 'w')
        f.write(t)
        f.close()
    except:
        saveAs()

def saveAs():
    f = asksaveasfile(mode = 'w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        #cut out white space
        f.write(t.rstrip())
    except:
        showerror(title="Oops!", message="Unable to save file...")

def openFile():
    f = askopenfile(mode = 'r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

root = Tk()
root.title("PyEdit")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)
#display text box
text = Text(root, width=400, height = 400)
text.pack()
#create menubar
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
#root.destroy is better to use because it destroys the main program loop
filemenu.add_command(label="Quit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()

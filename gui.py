from tkinter import *
from PIL import Image, ImageTk
import os

#locating the python directory
path = os.path.abspath(os.path.dirname(__file__))

def story():
    storyWindow = Tk()
    storyWindow.wm_title("Add Dictionary")
    storyWindow.configure(background="#E5E8E8")
    storyWindow.geometry("750x600+100+100")

    frame1 = Frame(storyWindow, bg="#000000")
    rapunzel = Image.open(path + "\\images\\rapunzel.jpg")
    photo = ImageTk.PhotoImage(rapunzel)
    label = Label(image=photo)
    label.rapunzel = photo # keep a reference!
    label.grid()

    frame2 = Frame(storyWindow, bg="#000000")
    rapunzel = Image.open(path + "\\images\\rapunzel.jpg")
    photo = ImageTk.PhotoImage(rapunzel)
    label = Label(image=photo)
    label.rapunzel = photo # keep a reference!
    label.grid()

    frame3 = Frame(storyWindow, bg="#000000")
    rapunzel = Image.open(path + "\\images\\rapunzel.jpg")
    photo = ImageTk.PhotoImage(rapunzel)
    label = Label(image=photo)
    label.rapunzel = photo # keep a reference!
    label.grid()

    frame4 = Frame(storyWindow, bg="#000000")
    frame5 = Frame(storyWindow, bg="#000000")
    frame6 = Frame(storyWindow, bg="#000000")
    frame7 = Frame(storyWindow, bg="#000000")
    frame8 = Frame(storyWindow, bg="#000000")

    frame1.grid(row=0, column=0)
    frame2.grid(row=0, column=1)
    frame3.grid(row=0, column=2)
    frame4.grid(row=0, column=3)
    frame5.grid(row=0, column=4)
    frame6.grid(row=1, column=0)
    frame7.grid(row=2, column=1)
    frame8.grid(row=3, column=2)
    Label(frame7, text="sfpğjapkfp").grid()
    Label(frame4, text="sfpğjapkfp").grid()
    Label(frame8, text="sfpğjapkfp").grid()


    storyWindow.mainloop()
def saveDictionary():
    subjectTitle = entry1.get()

story()

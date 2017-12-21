from tkinter import *

def addDictionary():
    addingWindow = Toplevel()
    addingWindow.wm_title("Add Dictionary")
    main_window.configure(background="#45B39D")
    topFrame = Frame(addingWindow, bg="#E5E8E8")
    label1 = Label(topFrame, text="Add Your Personal Subject", font="verdana 14 bold")
    label2 = Label(topFrame, texxt="Beware that its case-sensitive.", font="verdana 10 italic")
    entry1 = Entry()

    topFrame.pack(side="top")
    label1.pack()
    label2.pack()
    entry1.pack()

def saveDictionary():
    subjectTitle = entry1.get()

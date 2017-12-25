from tkinter import*
import tkinter.messagebox as tk
import string
import os

# Locating the python directory
path = os.path.abspath(os.path.dirname(__file__))

storyWindow = Toplevel()
storyWindow.title('Short Stories for Children')
storyWindow.configure(background = '#FECBDB')
storyWindow.attributes('-fullscreen', True),

def printStory(storyName):
    infile = open(path + "\\stories\\" + storyName + ".txt", "r")
    storyText = Label(storyWindow, text=infile).grid()

    storyImage = Image.open(path + "\\images\\" + storyName + ".png")
    photo = ImageTk.PhotoImage(storyImage)
    label = Label(image=photo)
    label.storyImage = photo

"""
def createWidgets(storyName):
    storyName = Text(width = 20, height = 20)
    storyName.pack(expand=YES, fill=BOTH)"""

def wordCount(storyName):
    #Get text from textbox and split it by whitespace characters into a list.
    #Then find length of list
    userText = storyName.get("1.0", END)
    wordList = userText.split()
    number_of_words = len(wordList)
    tk2.showinfo('Word Count', 'Words:  ' + str(number_of_words))

def letterCount(storyName):
    userText = storyName.get("1.0", END)
    wordList = userText.split()
    characters = 0
    for i in wordList:
        characters += len(i)
    print("Number of characters in file:", characters)

button1=Button(storyWindow, text='Word Count', background='pink', fg='dark green', font='Century 11 italic underline', command=wordCount)
button2=Button(storyWindow, text='Letter Count', background='pink', fg='dark green', font='Century 11 italic underline', command=letterCount)
button3=Button(storyWindow, text='Back', background='pink', fg='dark green', font='Century 11 italic underline', command=storyWindow.destroy)
button1.grid(row = 0,column =1)
button2.grid(row = 0,column =2)
button3.grid(row = 0,column =0)

"""
def readStory(storyName):
    userText = storyName.get("1.0", END)
    engine = pyttsx.init()
    engine.setProperty('rate', 70)

    voices = engine.getProperty('voices')
    for voice in voices:
        engine.setProperty('voice', voice.id)
        engine.say(userText)
    engine.runAndWait()"""

mainloop()

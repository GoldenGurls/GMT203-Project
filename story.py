from tkinter import*
import tkinter.messagebox as tk
from PIL import Image, ImageTk
import string
import os

# Locating the python directory
path = os.path.abspath(os.path.dirname(__file__))

storyWindow = Toplevel()
storyWindow.title('Short Stories for Children')
storyWindow.configure(background = '#FECBDB')
storyWindow.attributes('-fullscreen', True)

    
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

textFrame = Frame(storyWindow, background="#FECBDB", height=500, width=700)
textFrame.grid(row=1, columnspan=5, rowspan=3)

def printStory(storyName):
    """storyImage = Image.open(path + "\\images\\" + storyName + ".png")
    photo = ImageTk.PhotoImage(storyImage)
    label = Label(image=photo)
    label.storyImage = photo"""

    infile = open(path + "\\stories\\" + storyName + ".txt", "r")
    storyText = infile.readlines()
<<<<<<< HEAD
    toPrint = storyText + ["\n"]
    textLabel = Label(textFrame, text=toPrint, background='#FECBDB').grid()
=======
    textLabel = Label(storyWindow, text=storyText, background='#FECBDB').grid(row=1)
>>>>>>> 9020564dc2e46e571fd76e137ef436af852d319d

    mainloop()

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

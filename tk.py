from tkinter import*
import tkinter.messagebox as tk
import string

class NewWindow():
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title('Short Stories for Children')
        self.main_window.configure(background = '#E5E8E8')
        self.main_window.geometry('500x500')
        #self.label = Label(self.main_window, text = 'aa', background = 'white')
        self.main_window.mainloop()

    def create_widgets():
        self.storyName = Text(width = 20, height = 20)
        self.storyName.pack(expand=YES, fill=BOTH)

    def wordCount():
        #Get text from textbox and split it by whitespace characters into a list. Then find length of list
        userText = self.storyName.get("1.0", END)
        wordList = userText.split()
        number_of_words = len(wordList)
        tk2.showinfo('Word Count', 'Words:  ' + str(number_of_words))

    def letterCount():
        userText = self.storyName.get("1.0", END)
        wordList = userText.split()
        characters = 0
        for i in wordList:
            characters += len(i)

        print ("Number of characters in file:", characters)






NewWindow()

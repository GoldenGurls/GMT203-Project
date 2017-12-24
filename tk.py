from tkinter import*
import tkinter.messagebox as tk
import string

main_window = Tk()
main_window.title('Short Stories for Children')
main_window.configure(background = '#E5E8E8')
main_window.attributes('-fullscreen', True)

def create_widgets():
    storyName = Text(width = 20, height = 20)
    storyName.pack(expand=YES, fill=BOTH)

def wordCount():
        #Get text from textbox and split it by whitespace characters into a list. Then find length of list
    userText = storyName.get("1.0", END)
    wordList = userText.split()
    number_of_words = len(wordList)
    tk2.showinfo('Word Count', 'Words:  ' + str(number_of_words))

def letterCount():
    userText = storyName.get("1.0", END)
    wordList = userText.split()
    characters = 0
    for i in wordList:
        characters += len(i)

    print ("Number of characters in file:", characters)

button1=Button(text='Word Count', background='pink', fg='dark green', font='Century 11 italic underline', command=wordCount)
button2=Button(text='Letter Count', background='pink', fg='dark green', font='Century 11 italic underline', command=letterCount)
button3=Button(text='Back', background='pink', fg='dark green', font='Century 11 italic underline', command=main_window.destroy)
button1.grid(row = 0,column =1)
button2.grid(row = 0,column =2)
button3.grid(row = 0,column =0)





mainloop()

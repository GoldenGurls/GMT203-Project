from tkinter import *
from PIL import Image, ImageTk
import os

# Locating the python directory
path = os.path.abspath(os.path.dirname(__file__))

mainWindow = Tk()
mainWindow.wm_title("Short Stories for Children")
mainWindow.attributes("-fullscreen", True)

def main():

    # ADDING IMAGES

    banner = Image.open(path + "\\images\\banner.png")
    bannerPhoto = ImageTk.PhotoImage(banner)
    bannerLabel = Label(image=bannerPhoto)
    bannerLabel.banner = bannerPhoto

    rapunzel = Image.open(path + "\\images\\rapunzel.png")
    photo1 = ImageTk.PhotoImage(rapunzel)
    label1 = Label(image=photo1)
    label1.rapunzel = photo1 # keep a reference
    button1 = Button(mainWindow, text="Rapunzel", command= lambda: callback("rapunzel"))

    cinderella = Image.open(path + "\\images\\cinderella.png")
    photo2 = ImageTk.PhotoImage(cinderella)
    label2 = Label(image=photo2)
    label2.cinderella = photo2
    button2 = Button(mainWindow, text="Cinderella", command= lambda: callback("cinderella"))

    sleepingBeauty = Image.open(path + "\\images\\sleepingBeauty.png")
    photo3 = ImageTk.PhotoImage(sleepingBeauty)
    label3 = Label(image=photo3)
    label3.sleepingBeauty = photo3
    button3 = Button(mainWindow, text="Sleeping Beauty", command= lambda: callback("sleepingBeauty"))

    snowQueen = Image.open(path + "\\images\\snowQueen.png")
    photo4 = ImageTk.PhotoImage(snowQueen)
    label4 = Label(image=photo4)
    label4.snowQueen = photo4
    button4 = Button(mainWindow, text="Snow Queen", command= lambda: callback("snowQueen"))

    snowWhite = Image.open(path + "\\images\\snowWhite.png")
    photo5 = ImageTk.PhotoImage(snowWhite)
    label5 = Label(image=photo5)
    label5.snowWhite = photo5
    button5 = Button(mainWindow, text="Snow White", command= lambda: callback("snowWhite"))

    pussInBoots = Image.open(path + "\\images\\pussInBoots.png")
    photo6 = ImageTk.PhotoImage(pussInBoots)
    label6 = Label(image=photo6)
    label6.pussInBoots = photo6
    button6 = Button(mainWindow, text="Puss in Boots", command= lambda: callback("pussInBoots"))

    redRidingHood = Image.open(path + "\\images\\redRidingHood.png")
    photo7 = ImageTk.PhotoImage(redRidingHood)
    label7 = Label(image=photo7)
    label7.redRidingHood = photo7
    button7 = Button(mainWindow, text="Little Red Riding Hood", command= lambda: callback("redRidingHood"))

    littleMermaid = Image.open(path + "\\images\\littleMermaid.png")
    photo8 = ImageTk.PhotoImage(littleMermaid)
    label8 = Label(image=photo8)
    label8.littleMermaid = photo8
    button8 = Button(mainWindow, text="Little Mermaid", command= lambda: callback("littleMermaid"))

    matchGirl = Image.open(path + "\\images\\matchGirl.png")
    photo9 = ImageTk.PhotoImage(matchGirl)
    label9 = Label(image=photo9)
    label9.matchGirl = photo9
    button9 = Button(mainWindow, text="Little Match Girl", command= lambda: callback("matchGirl"))

    happyPrince = Image.open(path + "\\images\\happyPrince.png")
    photo10 = ImageTk.PhotoImage(happyPrince)
    label10 = Label(image=photo10)
    label10.happyPrince = photo10
    button10 = Button(mainWindow, text="Happy Prince", command= lambda: callback("happyPrince"))

    hanselAndGratel = Image.open(path + "\\images\\hanselAndGratel.png")
    photo11 = ImageTk.PhotoImage(hanselAndGratel)
    label11 = Label(image=photo11)
    label11.hanselAndGratel = photo11
    button11 = Button(mainWindow, text="Hansel and Gratel", command= lambda: callback("hanselAndGratel"))

    bremen = Image.open(path + "\\images\\bremen.png")
    photo12 = ImageTk.PhotoImage(bremen)
    label12 = Label(image=photo12)
    label12.bremen = photo12
    button12 = Button(mainWindow, text="The Bremen Town Musicians", command= lambda: callback("bremen"))

    antAndGrasshopper = Image.open(path + "\\images\\antAndGrasshopper.png")
    photo13 = ImageTk.PhotoImage(antAndGrasshopper)
    label13 = Label(image=photo13)
    label13.antAndGrasshopper = photo13
    button13 = Button(mainWindow, text="The Ant and The Grasshopper ", command= lambda: callback("antAndGrasshopper"))

    thumbelina = Image.open(path + "\\images\\thumbelina.png")
    photo14 = ImageTk.PhotoImage(thumbelina)
    label14 = Label(image=photo14)
    label14.thumbelina = photo14
    button14 = Button(mainWindow, text="Thumbelina", command= lambda: callback("thumbelina"))

    aliBaba = Image.open(path + "\\images\\aliBaba.png")
    photo15 = ImageTk.PhotoImage(aliBaba)
    label15 = Label(image=photo15)
    label15.aliBaba = photo15
    button15 = Button(mainWindow, text="Ali Baba and Forty Thieves", command= lambda: callback("aliBaba"))

    #Adding the exit button
    exitButon = Button(mainWindow, text = "Quit!", command = lambda: mainWindow.destroy())

    #Adding labels of the story images
    bannerLabel.grid(row=1, column=1, rowspan=1, columnspan=3)
    exitButon.grid(row=2, column=1, rowspan=1, columnspan=3)
    label1.grid(row=1, column=4)
    label2.grid(row=1, column=5)
    label3.grid(row=1, column=6)
    label4.grid(row=3, column=1, columnspan=1)
    label5.grid(row=3, column=2)
    label6.grid(row=3, column=3)
    label7.grid(row=3, column=4)
    label8.grid(row=3, column=5)
    label9.grid(row=3, column=6)
    label10.grid(row=5, column=1, columnspan=1)
    label11.grid(row=5, column=2)
    label12.grid(row=5, column=3)
    label13.grid(row=5, column=4)
    label14.grid(row=5, column=5)
    label15.grid(row=5, column=6)

    #Adding buttons for all of the stories
    button1.grid(row=2, column=4)
    button2.grid(row=2, column=5)
    button3.grid(row=2, column=6)
    button4.grid(row=4, column=1, columnspan=1)
    button5.grid(row=4, column=2)
    button6.grid(row=4, column=3)
    button7.grid(row=4, column=4)
    button8.grid(row=4, column=5)
    button9.grid(row=4, column=6)
    button10.grid(row=6, column=1, columnspan=1)
    button11.grid(row=6, column=2)
    button12.grid(row=6, column=3)
    button13.grid(row=6, column=4)
    button14.grid(row=6, column=5)
    button15.grid(row=6, column=6)

    mainWindow.mainloop()

def callback(storyName):
    import story
    story.printStory(storyName)

main()

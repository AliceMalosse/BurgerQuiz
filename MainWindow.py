#Le Burger quiz
    #MainWindow.py : class describing the widgets in the game window

#Date : 25/06/2023 
#Author : MALOSSE Alice

#Import
from tkinter import Tk, Label, Button, Canvas
from gameCanvas import GameCanvas

#Create and manage the Tkinter Window
class MainWindow(Tk) :
    #init manages the layout of the window
    def __init__(self, gameState):
        Tk.__init__(self)

        #window option
        self.title("Burger Quiz")
        self.minsize(1550, 820) 

        #widget
        self.gameCanvas = GameCanvas()
        self.gameButton2 = Button(self, text="2 Joueurs",command=lambda:gameState.startNewGame(2), bg='black', font='Horseshoes', fg='yellow',relief='flat')
        self.gameButton3 = Button(self, text="3 Joueurs",command=lambda:gameState.startNewGame(3), bg='black', font='Horseshoes', fg='yellow',relief='flat')
        self.gameButton4 = Button(self, text="4 Joueurs",command=lambda:gameState.startNewGame(4), bg='black', font='Horseshoes', fg='yellow',relief='flat')
        self.finalDuelButton = Button(self, text="Burger de la mort subite",command=gameState.startMortSubite(), bg='black', font='Horseshoes', fg='yellow',relief='flat')
        self.quitButton = Button(self, text="Quit", command=self.destroy, bg='black', font=('HorseshoesAndLemonade',22), fg='red',relief='flat')

        self.nuggets = Button(self, text='', command=gameState.nuggets(),bg='black')

        gameState.state = "notStarted"

        #pack
        self.gameCanvas.pack()
        self.gameButton2.place(x=190,y=744)
        self.gameButton3.place(x=310,y=744)
        self.gameButton4.place(x=430,y=744)
        self.finalDuelButton.place(x=550,y=744)
        self.quitButton.place(x=1435,y=730)
        self.nuggets.place(x=290,y=50)

    #detect board click and add keycode to function 
    def manageEvent (self, gameState):
        self.bind('<KeyPress>', lambda event : gameState.canon.handleKeyboardEvent(event.keysym, "KEY_PRESS"))
        self.bind('<KeyRelease>', lambda event : gameState.canon.handleKeyboardEvent(event.keysym, "KEY_RELEASE"))
    
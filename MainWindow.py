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
        self.minsize(1600, 900) 

        #widget
        self.gameCanvas = GameCanvas()
        self.gameButton2 = Button(self, text="2 Joueurs",command=lambda:gameState.startNewGame(2), bg='black', font='Horseshoes', fg='yellow',relief='flat')
        self.gameButton3 = Button(self, text="3 Joueurs",command=lambda:gameState.startNewGame(3), bg='black', font='Horseshoes', fg='yellow',relief='flat')
        self.gameButton4 = Button(self, text="4 Joueurs",command=lambda:gameState.startNewGame(4), bg='black', font='Horseshoes', fg='yellow',relief='flat')
        self.quitButton = Button(self, text="Quit", command=self.destroy, bg='black', font='Horseshoes', fg='red',relief='flat')

        #pack
        self.gameCanvas.pack()
        self.gameButton2.place(x=250,y=775)
        self.gameButton3.place(x=370,y=775)
        self.gameButton4.place(x=490,y=775)
        self.quitButton.place(x=1500,y=775)

    #detect board click and add keycode to function 
    def manageEvent (self, gameState):
        self.bind('<KeyPress>', lambda event : gameState.canon.handleKeyboardEvent(event.keysym, "KEY_PRESS"))
        self.bind('<KeyRelease>', lambda event : gameState.canon.handleKeyboardEvent(event.keysym, "KEY_RELEASE"))
    
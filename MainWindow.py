"""
MainWindow.py
Class describing the widgets in the game window
25/06/2023 by  MALOSSE Alice
"""

from tkinter import Tk, Label, Button, Canvas
from gameCanvas import GameCanvas

class MainWindow(Tk) :
    #init manages the layout of the window
    def __init__(self, gameState):
        Tk.__init__(self)

        #window option
        self.title("Burger Quiz")
        self.minsize(1280, 720) 

        #widget
        self.gameCanvas = GameCanvas()
        self.gameButton = Button(self, text="New Game",command=gameState.startNewGame, bg='black', font='Horseshoes', fg='yellow',relief='flat')
        self.quitButton = Button(self, text="Quit", command=self.destroy, bg='black', font='Horseshoes', fg='white',relief='flat')

        #pack
        self.gameCanvas.pack()
        self.gameButton.place(x=5,y=715)
        self.quitButton.place(x=1275,y=715)

    #detect board click and add keycode to function 
    def manageEvent (self, gameState):
        self.bind('<KeyPress>', lambda event : gameState.canon.handleKeyboardEvent(event.keysym, "KEY_PRESS"))
        self.bind('<KeyRelease>', lambda event : gameState.canon.handleKeyboardEvent(event.keysym, "KEY_RELEASE"))
    
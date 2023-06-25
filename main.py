#Le Burger Quiz

#Import
from tkinter import Tk, Label, Button, Canvas

from MainWindow import MainWindow
#from classes.Sprite import Sprite
from gameState import GameState
from equipe import Equipe
from gameLoop import gameLoop

#Main program

gameState = GameState()
mainWindow = MainWindow(gameState)

#gameState.canon.sprite.setSpriteScale(1)
gameLoop(mainWindow, gameState)


mainWindow.manageEvent(gameState)
mainWindow.mainloop()
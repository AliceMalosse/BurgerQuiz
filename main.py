#Le Burger quiz
    #main.py : main program

#Date : 25/06/2023 
#Author : MALOSSE Alice

#Import
from tkinter import Tk, Label, Button, Canvas

from MainWindow import MainWindow
from gameState import GameState
from equipe import Equipe
from gameLoop import gameLoop

#Main program

gameState = GameState()
mainWindow = MainWindow(gameState)

gameLoop(mainWindow, gameState)

mainWindow.manageEvent(gameState)
mainWindow.mainloop()

#TODO : 
    #Positionner correctement les questions Nuggets
    #Ajouter des sauts a la lignes pour les questions longues
    #Justifier les textes a gauche
    #Programmer l'ajout de points aux equipes

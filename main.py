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
    #Ajouter les conditions de victoire -> skip a l'ecran de burger de la mort
    #Barrer les menus deja choisi
    #Revoir le nombre de question
    #Modifier les indices dans les fonctions de choix de menu

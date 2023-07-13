#Le Burger quiz
    #gameLoop.py : function managing the game and drawing loop

#Date : 25/06/2023 
#Author : MALOSSE Alice

#Import
from gameState import GameState

#Init
framesPerSecond = 30

#Main loop
def gameLoop(mainWindow, gameState):
    #GAME LOGIC
    #gameState.canon.manageEntity(gameState)

    #winning condition
    if gameState.state == "started":
        for i in range(gameState.nbTeam): 
            if gameState.teamList[i].nb_miam==25 : 
                gameState.question.currentEpreuve = len(gameState.question.listEpreuve) - 1

    #DISPLAYING STUFF
    mainWindow.gameCanvas.updateCanvas(gameState)

    #Game loop related to tkinter event loop
    mainWindow.after(int(1000/framesPerSecond), lambda: gameLoop (mainWindow, gameState))
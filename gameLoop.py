"""
gameLoop.py
Function managing the game and drawing loop
25/06/2023 by MALOSSE Alice
"""
from gameState import GameState

framesPerSecond = 30

#Main loop
def gameLoop(mainWindow, gameState):

  #GAME LOGIC
  #gameState.canon.manageEntity(gameState)

  #winning condition
  if gameState.state == "started":
        for i in range(gameState.nbTeam): 
            gameState.teamList[i].nb_miam==25
            gameState.currentPart==gameState.partList[-1]



  #DISPLAYING STUFF
  mainWindow.gameCanvas.updateCanvas(gameState)

  #Game loop related to tkinter event loop
  mainWindow.after(int(1000/framesPerSecond), lambda: gameLoop (mainWindow, gameState))
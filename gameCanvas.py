"""
GameCanvas.py
Class describing the elements on the game canvas.
25/06/2023 by MALOSSE Alice
"""

#Import
from tkinter import Canvas


#Contains all the elements necessary for display
class GameCanvas(Canvas):
    def __init__(self):

        self.height = 900
        self.width = 1600
        Canvas.__init__(self, width = self.width, height = self.height , bg="black")

        
    #Main drawing function. Calls all the other entity related draw function
    def updateCanvas(self, gameState):
        self.delete('all')
        self.textNewGame=self.create_text(120,790,text='New Game :', fill='red', font=('Horseshoes',20))

        #gameState.canon.draw(self)
        #for team in gameState.teamList :
        #    team.draw(self)
        #gameState.currentPart.draw(self)

        if gameState.state=='notStarted' or gameState.state=='endGame':
            self.textTitle=self.create_text(790,290,text='BURGER', fill='yellow', font=('Horseshoes',90))
            self.textTitle=self.create_text(790,410,text='QUIZ', fill='yellow', font=('Horseshoes',90))
        

        

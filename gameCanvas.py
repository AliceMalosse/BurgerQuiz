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

        self.height = 720
        self.width = 1280
        Canvas.__init__(self, width = self.width, height = self.height , bg="black")

        
    #Main drawing function. Calls all the other entity related draw function
    def updateCanvas(self, gameState):
        self.delete('all')
        #gameState.canon.draw(self)
        #for team in gameState.teamList :
        #    team.draw(self)
        #gameState.currentPart.draw(self)

        if gameState.state=='notStarted' or gameState.state=='endGame':
            self.textTitle=self.create_text(640,190,text='BURGER', fill='yellow', font=('Horseshoes',90))
            self.textTitle=self.create_text(640,310,text='QUIZ', fill='yellow', font=('Horseshoes',90))

        

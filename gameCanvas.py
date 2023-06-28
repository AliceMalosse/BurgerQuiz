#Le Burger quiz
    #gameCanvas.py : class describing the elements on the game canvas.

#Date : 25/06/2023 
#Author : MALOSSE Alice


#Import
from tkinter import Canvas, PhotoImage


#Contains all the elements necessary for display
class GameCanvas(Canvas):
    def __init__(self):

        self.height = 900
        self.width = 1600
        Canvas.__init__(self, width = self.width, height = self.height , bg="black")

        #uploading static images
        #TODO : Importer toutes les images fixes (epreuves)
        #TODO : Refaire toutes les images avec des screenshot 
        self.ImLogo = PhotoImage(file="./Ressources/BBQ.gif") #TODO : Remplacer par le logo
        self.ImNuggets = PhotoImage(file="./Ressources/BBQ.gif")
        self.ImSelPoivre = PhotoImage(file="./Ressources/BBQ.gif")
        self.ImMenu = PhotoImage(file="./Ressources/BBQ.gif")
        self.ImAddition = PhotoImage(file="./Ressources/BBQ.gif")
        self.ImBurgerMort = PhotoImage(file="./Ressources/BBQ.gif")
        self.ImAdditionMort = PhotoImage(file="./Ressources/BBQ.gif")

    #Main drawing function. Calls all the other entity related draw function
    def updateCanvas(self, gameState):
        self.delete('all')
        self.textNewGame=self.create_text(120,790,text='New Game :', fill='red', font=('Horseshoes',20))
        self.logoQuiz = self.create_image(50,10,image=self.ImLogo)
        
        gameState.drawRules(self)
        for team in gameState.teamList :
            team.draw(self)

        if gameState.state=='notStarted' or gameState.state=='endGame':
            self.textTitle=self.create_text(790,290,text='BURGER', fill='yellow', font=('Horseshoes',90))
            self.textTitle=self.create_text(790,410,text='QUIZ', fill='yellow', font=('Horseshoes',90))
        

        

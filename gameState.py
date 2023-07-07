#Le Burger quiz
    #gameState.py : class describing the game state (progress, part, ...)

#Date : 25/06/2023 
#Author : MALOSSE Alice

#Import
from equipe import Equipe

#Manage the game state and part
class GameState() :
    #init game variable
    def __init__(self, ):
        self.state="notStarted"
        self.nbTeam=0
        self.teamList=[]
        self.teamName=["Ketchup", "Mayo", "BBQ", "Creamy"]
        self.partList=["Nuggets", "Sel ou poivre", "Menu", "Addition", "Burger de la mort", "Mort subite"]
        self.currentPart=self.partList[0]

    #Called to start a new level or a new game
    def startNewGame(self, nb_team):
        self.state = "started"
        self.nbTeam = nb_team
        self.teamList=[]

        for i in range(self.nbTeam): 
            self.teamList.append(Equipe(self.teamName[i]))

    def startMortSubite(self,) :
        self.startNewGame(2)
        self.currentPart=self.partList[-1]

    #Draw the rules of the current part
    def drawRules (self, ) :
        filepath = "./Ressources/" + self.currentPart
        #TODO
        return 0
    
    def nuggets (self,):
        return 0
    

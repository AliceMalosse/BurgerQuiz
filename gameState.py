#Le Burger quiz
    #gameState.py : class describing the game state (progress, part, ...)

#Date : 25/06/2023 
#Author : MALOSSE Alice

#Import
from equipe import Equipe
from question import Questions

#Manage the game state and part
class GameState() :
    #init game variable
    def __init__(self, ):
        self.state="notStarted"
        self.nbTeam=0
        self.teamList=[]
        self.teamName=["Ketchup", "Mayo", "BBQ", "Creamy"]
        self.question=Questions("./Ressources/editionEte2023-quiz2.txt")
        self.press_next = False

    #Called to start a new level or a new game
    def startNewGame(self, nb_team):
        self.state = "started"
        self.nbTeam = nb_team
        self.teamList=[]

        for i in range(self.nbTeam): 
            self.teamList.append(Equipe(self.teamName[i]))

    def startMortSubite(self,) :
        self.startNewGame(2)

    def next_question(self,) :
        self.press_next=True

    
    

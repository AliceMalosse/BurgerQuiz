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
        self.press_next = False
        self.question = Questions("./Ressources/editionEte2023-quiz1.txt")

    #Called to start a new level or a new game
    def startNewGame(self, nb_team):
        self.state = "started"
        self.nbTeam = nb_team
        self.teamList=[]

        for i in range(self.nbTeam): 
            self.teamList.append(Equipe(self.teamName[i]))

    def chooseQuiz(self, ind) :
        if ind == 1 :
            self.question = Questions("./Ressources/editionEte2023-quiz1.txt")
        elif ind == 2 :
            self.question = Questions("./Ressources/editionEte2023-quiz2.txt")
        else : 
            self.question = Questions("./Ressources/additionPlus.txt")

    def next_question(self,) :
        print ("next - GameState")
        self.question.next_question()

    
    

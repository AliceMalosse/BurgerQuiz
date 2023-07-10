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
        self.question.next_question()

    def update(self, ) :
        self.question.update(self)

    def handleKeyboardEvent (self, event) :
        key = event.char
        if key == "k" :
            try :
                self.teamList[0].plusmiam()
            except :
                print ("No team Ketchup")
        elif key == "m" :
            try :
                self.teamList[1].plusmiam()
            except :
                print ("No team Mayo")
        elif key == "b" :
            try :
                self.teamList[2].plusmiam()
            except :
                print ("No team BBQ")
        elif key == "C" :
            try :
                self.teamList[3].plusmiam()
            except :
                print ("No team Creamy")    

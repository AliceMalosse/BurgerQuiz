from equipe import Equipe

class GameState() :
    #init game variable
    def __init__(self, prevLevel = 0):

        self.state="notStarted"
        self.nbTeam=0
        self.teamList=[]
        self.teamName=["Ketchup", "Mayo", "BBQ", "Creamy"]
        self.partList=["Nuggets", "Sel ou poivre", "Menu", "Addition", "Burger de la mort"]
        self.currentPart=self.partList[0]

    #Called to start a new level or a new game
    def startNewGame(self, nb_team):
        self.state = "started"
        self.nbTeam = nb_team
        self.teamList=[]

        for i in range(self.nbTeam): 
            self.teamList.append(Equipe(self.teamName[i]))

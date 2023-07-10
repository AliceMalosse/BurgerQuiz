#Le Burger quiz
    #question.py : Fichier contenant la classe Equipe

#Date : 25/06/2023 
#Author : MALOSSE Alice

#Classe Epreuve
class Epreuve : 
    def __init__ (self, name, intitule) :
        self.name = name
        self.description = intitule
        self.question = []
        self.current_question = 0
        self.state = "notStarted"
        self.nbQuest = len(self.question)
        if self.name == "Nuggets" : 
            self.nbQuest = 12
        
    def set_question (self, list) :
        self.question = list
        self.nbQuest = len(self.question)
        return 0
    
    def draw (self, gameCanvas) :
        gameCanvas.create_text(753, 245,text=self.name, fill='#403CAC', font=('HorseshoesAndLemonade',50))
        gameCanvas.create_text(753, 285,text=self.description, fill='#5B9BD5', font=('HorseshoesAndLemonade',25))
        if self.name[0] == "N" :
            self.draw_quest(gameCanvas, 390, 310)
            self.drawNuggets(gameCanvas)
        elif self.name[0] != 'B' :
            self.draw_quest(gameCanvas, 390, 340)

    def draw_quest (self, gameCanvas, width, height) :
        gameCanvas.create_text(width, height,text=self.question[self.current_question], fill='#403CAC', font=('HorseshoesAndLemonade',25), width=750, anchor='nw')


    def drawNuggets(self, gameCanvas) : 
        gameCanvas.create_text(390, 420,text=self.question[self.current_question+1], fill='#5B9BD5', font=('HorseshoesAndLemonade',20), width=750, anchor='nw')
        gameCanvas.create_text(390, 490,text=self.question[self.current_question+2], fill='#403CAC', font=('HorseshoesAndLemonade',20), width=750, anchor='nw')
        gameCanvas.create_text(390, 560,text=self.question[self.current_question+3], fill='#5B9BD5', font=('HorseshoesAndLemonade',20), width=750, anchor='nw')
        gameCanvas.create_text(390, 630,text=self.question[self.current_question+4], fill='#403CAC', font=('HorseshoesAndLemonade',20), width=750, anchor='nw')

    def update (self, ) :
        if self.current_question == self.nbQuest or self.current_question == self.nbQuest*5 :
            self.state = "end"



#Classe Questions
class Questions :
    def __init__ (self, question_file) :
        self.filename = question_file
        self.listEpreuve = []
        self.menu = []
        self.extract_question(self.filename)
        self.currentEpreuve = 0
        self.listEpreuve[self.currentEpreuve].state = "started"

    def extract_question(self, filename) : 
        #Initialisation
        with open(filename,"r",encoding='utf-8') as file : 
            lines = file.readlines()
        list_name_epreuve = ["Nuggets\n", "Sel ou poivre\n", "Menus\n", "Menu\n", "Addition\n", "Burger de la mort\n", "Addition de la mort\n"]
        i = 0
        #While there is a next epreuve
        while (lines[i] in list_name_epreuve) :
            if lines[i] == "Menus\n" :    #Set menus list
                for p in range (1,6) :
                    self.menu.append(lines[i+p])
                i+=6
            else :
                epreuve = Epreuve(lines[i], lines[i+1])
                #Get list of questiton
                list_question = []
                i+= 2
                while lines[i][0:3] in ["A :", "B :", "C :", "D :", "Q1 ", "Q2 ", "Q3 ", "Q4 ", "Q5 ", "Q6 ", "Q7 ", "Q8 ", "Q9 ", "Q10", "Q11", "Q12"] :
                    list_question.append(lines[i])
                    i+=1
                epreuve.set_question(list_question)
                self.listEpreuve.append(epreuve)

    def update (self, gameState) :
        self.listEpreuve[self.currentEpreuve].update()
        if self.listEpreuve[self.currentEpreuve].state == 'end' : 
            if self.listEpreuve[self.currentEpreuve].name == 'Burger de la mort' :
                gameState.state = 'end'
            else :
                self.currentEpreuve += 1
                if self.listEpreuve[self.currentEpreuve].name[0] != "M" :
                    self.listEpreuve[self.currentEpreuve].state = "started"

    def next_question (self, ) :
        self.listEpreuve[self.currentEpreuve].current_question += 1
        if self.listEpreuve[self.currentEpreuve].name[0] == "N" :
            self.listEpreuve[self.currentEpreuve].current_question += 4


    def draw (self, gameCanvas) :
        if self.listEpreuve[self.currentEpreuve].name[0] == "M" and self.listEpreuve[self.currentEpreuve].state == "notStarted" :
            #Draw the list of menu
            gameCanvas.create_text(753, 245,text="Menus", fill='#403CAC', font=('HorseshoesAndLemonade',50))
            gameCanvas.create_text(390, 300,text="1 : "+self.menu[0], fill='#5B9BD5', font=('HorseshoesAndLemonade',20), width=750, anchor='nw')
            gameCanvas.create_text(390, 370,text="2 : "+self.menu[1], fill='#5B9BD5', font=('HorseshoesAndLemonade',20), width=750, anchor='nw')
            gameCanvas.create_text(390, 440,text="3 : "+self.menu[2], fill='#5B9BD5', font=('HorseshoesAndLemonade',20), width=750, anchor='nw')
            gameCanvas.create_text(390, 510,text="4 : "+self.menu[3], fill='#5B9BD5', font=('HorseshoesAndLemonade',20), width=750, anchor='nw')
            gameCanvas.create_text(390, 580,text="5 : "+self.menu[4], fill='#5B9BD5', font=('HorseshoesAndLemonade',20), width=750, anchor='nw')
        else :
            self.listEpreuve[self.currentEpreuve].draw(gameCanvas)

    def choose_menu (self, nb) :
        self.currentEpreuve = nb + 2
        self.listEpreuve[self.currentEpreuve].state = "started"

        

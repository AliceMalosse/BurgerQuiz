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
        
    def set_question (self, list) :
        self.question = list
        return 0

#Classe Questions
class Questions :
    def __init__ (self, question_file) :
        self.filename = question_file
        self.listEpreuve = []
        self.menu = []
        self.extract_question(self.filename)

    def extract_question(self, filename) : 
        #Initialisation
        with open(filename) as file : 
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

        

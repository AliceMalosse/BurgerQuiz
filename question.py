#Le Burger quiz
    #question.py : Fichier contenant la classe Equipe

#Date : 25/06/2023 
#Author : MALOSSE Alice

#NB : May not be used

#Import

#Classe Epreuve
class Epreuve : 
    def __init__ (self, name, intitule) :
        self.name = name
        self.description = intitule
        self.question = []
        self.solution = []
        self.reward = 1
        if self.name == "Addition" :
            self.reward = 3
        if len(self.question) != len(self.solution) :
            print("ERROR : Number of question and answer do not correspond")
        
        def set_question (self, list) :
            self.question = list
            return 0
        
        def set_solution (self, list) :
            self.solution = list
            return 0

#Classe Questions
class Questions :
    def __init__ (self, question_file) :
        self.filename = question_file
        self.menu = []
        self.extract_question(self.filename)

    def extract_question(self, filename) : 
        with open(filename) as file : 
            lines = file.readlines()
        list_epreuve = ["Nuggets", "Sel ou poivre", "Menu", "Addition", "Burger de la mort"]
        while lines[0] in list_epreuve or lines!=[] :
            epreuve = Epreuve(lines[0], lines[1])
            list_question = []
            list_solution = []
            i = 2
            while lines[i][-1] == "?" :
                list_question.append(lines[i])
                list_solution.append(lines[i+1])
                i+=2
            epreuve.set_question(list_question)
            epreuve.set_solution(list_solution)
            self.store_epreuve(epreuve)
        return 0

    def store_epreuve (self, epreuve) : 
        if epreuve.name == "Nuggets" :
            self.nuggets = epreuve
        elif epreuve.name == "Sel ou poivre" : 
            self.seloupoivre = epreuve
        elif epreuve.name == "Menu" : 
            self.menu.append(epreuve)
        elif epreuve.name == "Addition" :
            self.addition = epreuve
        else :
            self.burger = epreuve
        return 0

        

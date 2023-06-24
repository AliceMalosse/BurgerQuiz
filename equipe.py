#Le Burger quiz
    #equipe.py : Fichier contenant la classe Equipe

#Import

#Classe Equipe

class Equipe :
    def __init__ (self, new_name) :
        self.name = new_name
        self.nb_miam = 0

    def plusmiam (self, ) :
        self.nb_miam += 1

    def get_nb_miam (self, ) :
        return self.nb_miam


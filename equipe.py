#Le Burger quiz
    #equipe.py : Fichier contenant la classe Equipe

#Date : 25/06/2023 
#Author : MALOSSE Alice

#Import

#Class Equipe
    # Manage team point and gif to print point on the Canvas
class Equipe :
    def __init__ (self, new_name) :
        self.name = new_name
        self.nb_miam = 0

    def plusmiam (self, ) :
        self.nb_miam += 1

    def get_nb_miam (self, ) :
        return self.nb_miam


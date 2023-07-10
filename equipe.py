#Le Burger quiz
    #equipe.py : Fichier contenant la classe Equipe

#Date : 25/06/2023 
#Author : MALOSSE Alice

#Import
from PIL import Image, ImageTk 

#Class Equipe
    # Manage team point and gif to print point on the Canvas
class Equipe :
    def __init__ (self, new_name) :
        self.name = new_name
        self.pos = self.init_position()
        self.nb_miam = 0
        self.gif = self.init_draw()
        self.new_gif = self.gif
        self.canvas = 0

    def plusmiam (self, ) :
        self.nb_miam += 1
        self.new_gif = self.init_draw()

    def get_nb_miam (self, ) :
        return self.nb_miam
    
    def init_position (self, ) :
        if self.name == "Ketchup" :
            position = (200, 350)
        elif self.name == "Mayo" :
            position = (200, 600)
        elif self.name == "Creamy" :
            position = (1370, 350)
        else : #self.name == "BBQ"
            position = (1370, 600)
        return position

    def init_draw (self, ) :
        im = Image.open("./Ressources/"+self.name+".gif")
        im.seek(self.nb_miam)
        im = im.resize((400, 224))
        return ImageTk.PhotoImage(im)

    def draw (self, gameCanvas) : 
        if self.gif != self.new_gif :
            print ("draw new point")
            self.gif = self.new_gif
            gameCanvas.itemconfigure(self.canvas, image = self.new_gif)
            self.new_gif = self.gif
        else :
            self.canvas = gameCanvas.create_image(self.pos[0], self.pos[1], image=self.gif)
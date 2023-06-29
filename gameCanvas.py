#Le Burger quiz
    #gameCanvas.py : class describing the elements on the game canvas.

#Date : 25/06/2023 
#Author : MALOSSE Alice


#Import
from tkinter import Canvas, PhotoImage
from PIL import Image, ImageTk

#Contains all the elements necessary for display
class GameCanvas(Canvas):
    def __init__(self):

        self.height = 900
        self.width = 1600
        Canvas.__init__(self, width = self.width, height = self.height , bg="black")

        #uploading static images
        #self.ImLogo = PhotoImage(file="./Ressources/BBQ.gif") #TODO : Remplacer par le logo
        self.ImLogo = self.treatImage("./Ressources/burgerQuiz.jpg", (300, 419))
        #TODO : creer une banderole pour programme moins lourd
        self.ImNuggets = self.treatImage("./Ressources/nuggets.png", (200, 112))
        self.ImSelPoivre = self.treatImage("./Ressources/seloupoivre.jpg", (200, 124))
        self.ImMenu = PhotoImage(file="./Ressources/BBQ.gif")
        self.ImAddition = self.treatImage("./Ressources/addition.png", (200, 112))
        self.ImBurgerMort = self.treatImage("./Ressources/burgerdelamort.jpg", (250, 185))
        self.ImAdditionMort = PhotoImage(file="./Ressources/BBQ.gif")

    #Main drawing function. Calls all the other entity related draw function
    def updateCanvas(self, gameState):
        self.delete('all')
        self.textNewGame=self.create_text(120,790,text='New Game :', fill='red', font=('Horseshoes',20))

        if gameState.state=="started"  :
            #Logo
            self.logoQuiz = self.create_image(1,1,image=self.ImLogo, anchor="nw")

            #Game differents states
            self.previewNuggets = self.create_image(350, 1, image=self.ImNuggets, anchor="nw")
            self.previewSeloupoivre = self.create_image(550, 1, image=self.ImSelPoivre, anchor="nw")
            #self.previewMenu = self.create_image(350, 1, image=self.ImMenu, anchor="nw")
            #self.previewAddition = self.create_image(350, 1, image=self.ImAddition, anchor="nw")
            self.previewBurgermort = self.create_image(1350, 1, image=self.ImBurgerMort, anchor="nw")
        
            gameState.drawRules() #TODO : Creer les slides de regles
            for team in gameState.teamList :
                team.draw()

        elif gameState.state=='notStarted' or gameState.state=='endGame':
            self.textTitle=self.create_text(790,290,text='BURGER', fill='yellow', font=('Horseshoes',90))
            self.textTitle=self.create_text(790,410,text='QUIZ', fill='yellow', font=('Horseshoes',90))


    def treatImage (self, filename, size) :
        im = Image.open(filename)
        im = im.resize(size)
        return ImageTk.PhotoImage(im)

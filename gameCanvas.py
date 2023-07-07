#Le Burger quiz
    #gameCanvas.py : class describing the elements on the game canvas.

#Date : 25/06/2023 
#Author : MALOSSE Alice


#Import
from tkinter import Canvas, Button
from PIL import Image, ImageTk

#Contains all the elements necessary for display
class GameCanvas(Canvas):
    def __init__(self):

        self.height = 820
        self.width = 1550
        Canvas.__init__(self, width = self.width, height = self.height , bg="black")

        #uploading static images
        self.ImLogo = self.treatImage("./Ressources/logoVertical.PNG", (187, 250))
        self.ImTitle = self.treatImage("./Ressources/BurgerQuiz.PNG", (500, 400))
        self.ImCadre = self.treatImage("./Ressources/cadre.jpg", (795,560))

    #Main drawing function. Calls all the other entity related draw function
    def updateCanvas(self, gameState):
        self.delete('all')
        self.textNewGame=self.create_text(90,763,text='New Game :', fill='red', font=('HorseshoesAndLemonade',20))

        if gameState.state=="started"  :
            #Logo
            self.logoQuiz = self.create_image(1,1,image=self.ImLogo, anchor="nw")

            #Game differents states
            self.textNuggets=self.create_text(290,63,text='Nuggets', fill='#403CAC', font=('HorseshoesAndLemonade',30))
            self.textSeloupoivre=self.create_text(550,63,text='Sel ou Poivre', fill='#5B9BD5', font=('HorseshoesAndLemonade',30))
            self.textMenus=self.create_text(790,63,text='Menus', fill='#403CAC', font=('HorseshoesAndLemonade',30))
            self.textAddition=self.create_text(980,63,text='Addition', fill='#5B9BD5', font=('HorseshoesAndLemonade',30))
            self.textBurgerMort=self.create_text(1300,63,text='Burger de la Mort', fill='#403CAC', font=('HorseshoesAndLemonade',30))

            #Teams
            for team in gameState.teamList :
                team.draw(self)
            
            #Question 
            gameState.question.update(gameState)
            self.cadre = self.create_image(753, 430,image=self.ImCadre)

        elif gameState.state=='notStarted' or gameState.state=='endGame':
            self.logoQuiz = self.create_image(740,350,image=self.ImTitle)

    def treatImage (self, filename, size) :
        im = Image.open(filename)
        im = im.resize(size)
        return ImageTk.PhotoImage(im)

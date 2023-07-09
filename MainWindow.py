#Le Burger quiz
    #MainWindow.py : class describing the widgets in the game window

#Date : 25/06/2023 
#Author : MALOSSE Alice

#Import
from tkinter import Tk, Button, Canvas, Checkbutton
from gameCanvas import GameCanvas

#Create and manage the Tkinter Window
class MainWindow(Tk) :
    #init manages the layout of the window
    def __init__(self, gameState):
        Tk.__init__(self)

        #window option
        self.title("Burger Quiz")
        self.minsize(1550, 820) 

        #widget
        self.gameCanvas = GameCanvas()
        self.checkBox1 = Checkbutton(self, text="Quiz 1", command=lambda:gameState.chooseQuiz(1), bg='black', font='Horseshoes', fg='yellow')
        self.checkBox2 = Checkbutton(self, text="Quiz 2", command=lambda:gameState.chooseQuiz(2), bg='black', font='Horseshoes', fg='yellow')
        self.checkBox3 = Checkbutton(self, text="Burger de la mort subite", command=lambda:gameState.chooseQuiz(3), bg='black', font='Horseshoes', fg='yellow')
        self.gameButton2 = Button(self, text="2 Joueurs",command=lambda:gameState.startNewGame(2), bg='black', font='Horseshoes', fg='yellow',relief='flat')
        self.gameButton3 = Button(self, text="3 Joueurs",command=lambda:gameState.startNewGame(3), bg='black', font='Horseshoes', fg='yellow',relief='flat')
        self.gameButton4 = Button(self, text="4 Joueurs",command=lambda:gameState.startNewGame(4), bg='black', font='Horseshoes', fg='yellow',relief='flat')
        self.nextButton = Button(self, text="Next", command=lambda:gameState.next_question(), bg='black', font=('HorseshoesAndLemonade',22), fg='#403CAC',relief='flat')
        self.quitButton = Button(self, text="Quit", command=self.destroy, bg='black', font=('HorseshoesAndLemonade',22), fg='red',relief='flat')

        gameState.state = "notStarted"

        #pack
        self.gameCanvas.pack()
        self.checkBox1.place(x=150,y=744)
        self.checkBox2.place(x=230,y=744)
        self.checkBox3.place(x=310,y=744)
        self.gameButton2.place(x=730,y=744)
        self.gameButton3.place(x=840,y=744)
        self.gameButton4.place(x=950,y=744)
        self.nextButton.place(x=1200, y=730)
        self.quitButton.place(x=1435,y=730)

    #detect board click and add keycode to function 
    def manageEvent (self, gameState):
        self.bind('<KeyPress>', lambda event : gameState.canon.handleKeyboardEvent(event.keysym, "KEY_PRESS"))
        self.bind('<KeyRelease>', lambda event : gameState.canon.handleKeyboardEvent(event.keysym, "KEY_RELEASE"))
    
import random
import numpy as np
import random, pygame, sys, pygame.font
from tkinter import messagebox as mb
import tkinter as tk
from buttons import *
FONT = pygame.font.SysFont('arial', 20, True)
WHITE    = (255, 255, 255)
BLACK    = (  0,   0,   0)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (128,   0, 200)
PINK     = (255,   0, 255)
GRAY     = (100, 100, 100)

WINDOWWIDTH = 400
WINDOWHEIGHT = 400
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

COLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, PINK, GRAY, BLACK)

Matrixsize = 40

class Game() : 
    pygame.init()


    def __init__(self,width, nbr_color, WINDOWWIDTH = WINDOWWIDTH, WINDOWHEIGHT = WINDOWHEIGHT, DISPLAYSURF = DISPLAYSURF,COLORS = COLORS ,font = FONT, MatrixSize = Matrixsize ) :
        self.width = width
        self.nbr_color = nbr_color
        self.COLORS = COLORS
        self.font = font
        self.WINDOWWIDTH = WINDOWWIDTH
        self.WINDOWHEIGHT = WINDOWHEIGHT
        self.DISPLAYSURF = DISPLAYSURF
        self.Matrixsize = Matrixsize 
        self.grill = []
        self.positions = set()
        self.map = [[(i,j) for i in range(self.width)] for j in range(self.width)]
    def GenerateGrille(self) :

        for col in range(self.width) :
            column = [random.randint(0,self.nbr_color-1) for line in range(self.width)]
            self.grill.append(column)
        return np.array(self.grill)

    def LTCoordOfBox(self, boxx, boxy):
       # Returns the x and y of the left-topmost pixel of the xth & yth box.
        xmargin = int((WINDOWWIDTH - (self.width * Matrixsize)) / 2)
        ymargin = int((WINDOWHEIGHT - (self.width * Matrixsize)) / 2)
        return (boxx * Matrixsize + xmargin, boxy * Matrixsize + ymargin)
    
    
    def ConstruGrille(self):
        for x in range(self.width):
            for y in range(self.width):
                left, top = Game.LTCoordOfBox(self,x, y)
                r, g, b = COLORS[self.grill[y][x]]

                pygame.draw.rect(DISPLAYSURF, (r, g, b), (left, top, Matrixsize, Matrixsize))


    def MajCell(self ,new_val, old_val, pos_x, pos_y) : 
        """
        Description : fonction qui mais a jour chaque cellule de la grille 
    
        Input : 
            - grill : type = array, matrice de taille width**2
            - new_val : type = int, nouvelle valeur de la case [0,0]
            - old_val : type = int, valeur actuelle de la case [0,0]
            - pos_x : type = int, position selon l'axe x
            - pos_y : type = int, position selon l'axe y
            - width : taille de la grille

        Output : Grille mise à jour 
        """
        if self.grill[pos_x][pos_y]==new_val : 
            self.positions.add((pos_x,pos_y))

        if old_val == new_val or self.grill[pos_x][pos_y] != old_val:
            return 

        self.grill[pos_x][pos_y] = new_val 
        self.positions.add((pos_x,pos_y))
        if pos_x > 0:
            Game.MajCell(self ,new_val, old_val, pos_x - 1, pos_y) 
        if pos_x < self.width - 1:
            Game.MajCell(self ,new_val, old_val, pos_x + 1, pos_y) 
        if pos_y > 0:
            Game.MajCell(self ,new_val, old_val, pos_x, pos_y - 1) 
        if pos_y < self.width - 1:
            Game.MajCell(self ,new_val, old_val, pos_x, pos_y + 1) 
    
    def Get_Positions(self,grill,val,): 
        
        for a in self.map : 
            for e in a :
                pos_x,pos_y = e[0],e[1]
                if e in self.positions:
                    if pos_x > 0:
                        if (pos_x-1,pos_y) not in self.positions and grill[pos_x-1][pos_y]==val : 
                            self.positions.add((pos_x-1,pos_y))
                    if pos_x <self.width-1:
                        if (pos_x+1,pos_y) not in self.positions and grill[pos_x+1][pos_y]==val : 
                            self.positions.add((pos_x+1,pos_y))
                    if pos_y > 0:
                        if (pos_x,pos_y-1) not in self.positions and grill[pos_x][pos_y-1]==val : 
                            self.positions.add((pos_x,pos_y-1))
                    if pos_y <self.width-1:
                        if (pos_x,pos_y+1) not in self.positions and grill[pos_x][pos_y+1]==val : 
                            self.positions.add((pos_x,pos_y+1))
                else : 
                    if pos_x > 0:
                        if (pos_x-1,pos_y) in self.positions and grill[pos_x][pos_y]==val : 
                            self.positions.add((pos_x,pos_y))
                    if pos_x <self.width-1:
                        if (pos_x+1,pos_y) in self.positions and grill[pos_x][pos_y]==val : 
                            self.positions.add((pos_x,pos_y))
                    if pos_y > 0:
                        if (pos_x,pos_y)  in self.positions and grill[pos_x][pos_y]==val : 
                            self.positions.add((pos_x,pos_y))
                    if pos_y <self.width-1:
                        if (pos_x,pos_y)  in self.positions and grill[pos_x][pos_y]==val : 
                            self.positions.add((pos_x,pos_y))


    def possible_states(self,listvalue): 
        colors = [e for e in listvalue if e!= self.grill[0][0]]
        for e in colors: 
            state_bis = np.copy(self.grill)
            
        pass
    def AssertEnd(self) : 
        """
        Description : Fonction qui verifie si la grille est complète (i.e si toute les eléments de la matrice sont égaux)

        Input : 
            - grill : type = array, plateau de jeu

        Output : Booleen confirmant la fin de la partie (True) ou non (False)
        """
        init = self.grill[0][0]
        for x in self.grill : 
            for y in x : 
                if y != init :
                    return False
        return True

    def Tourpartour(self, old_val,listvalue, max_moves,counter = 0):
    
        """
        Description : Fonction recursive qui joue au tour par tour la partie
    
        Input : 
            - grill : type = array, plateau de jeu
            - width : type = int, taille de la grille
            - old_val : type = int, valeur actuelle de la case [0,0]
            - listvalue : type = list, liste des valeur possible de la nouvelle valeur de la case
            - counter : type = int, count du nombre de coups valable joués

        Output : la fin de la partie
        """

        end = Game.AssertEnd(self)
        if counter == max_moves +1 : 
            #mb.showinfo("Defaite", "C'est perdu : " + str(counter) + " coups joués") 
            return 
        if end == True: 
            #mb.showinfo("Victoire", "C'est fini en : " + str(counter) + " tour")
            return 
        new_val_str = input("Couleur de case ? mettre 'end' pour finir :  ")
        while new_val_str not in listvalue:
            if new_val_str == "end" :
                return #mb.showinfo("Quitté", "Vous avez arrété la partie")
            
            new_val_str = input("Couleur de case ? mettre 'end' pour finir :  ")
        new_val = int(new_val_str)
        if old_val != new_val :
            counter +=1 
        Game.MajCell(self ,new_val, old_val, 0,0)
        
        print(self.grill)
        print(counter)
        Game.Get_Positions(self,self.grill,new_val)
        Game.ConstruGrille(self)
        pygame.display.update()
        Game.Tourpartour(self, new_val,listvalue, max_moves,counter)

    

    def Partie(self) :
        """
        Description : Fonction qui produit une partie entiere

        Input : 
        - width : type = int, taille de la longueur de la grille de taille width x width
        - nbr_color : type = int, nombre de couleur diférentes
    
        Output : 
        déroulement de toute la partie
        """
        max_moves = np.round((25*(2*self.width)*self.nbr_color)/((14+14)*6))
    
    
        self.grill = Game.GenerateGrille(self)
        global COLORS, WINDOWWIDTH, WINDOWHEIGHT, DISPLAYSURF, FONT
        root = tk.Tk()
        root.withdraw()
        FPS = 10

        WINDOWWIDTH = WINDOWHEIGHT = Matrixsize*self.width + 200

        pygame.display.set_caption("Flood it!")
        FPSCLOCK = pygame.time.Clock()
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        DISPLAYSURF.fill(GRAY)
        for x in range(0,self.nbr_color ) :
            PygameButton(COLORS[x],x * 25, 17, 25, 25, str(x)).Construction(DISPLAYSURF)

        listvalue = listvalue = ["{}".format(i) for i in range(self.nbr_color)]

        old_val= self.grill[0,0]

    
        print(self.grill)

    
        Game.ConstruGrille(self)
        FPSCLOCK.tick(FPS)

        pygame.display.update()

        Game.Tourpartour(self, old_val, listvalue,max_moves)
    
une_p = Game(5,4)
une_p.Partie()

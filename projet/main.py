import random
import numpy as np
import random, pygame, sys, pygame.font
from tkinter import messagebox as mb
import tkinter as tk
from buttons import *


pygame.init()
FONT = pygame.font.SysFont('arial', 20, True)

Matrixsize = 40

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


def GenerateGrille(width, nbr_color) : 

    """
    Description : fonction qui génère la grille

    Input : 
        - width : type = int, taille de la longueur de la grille de taille width x width
        - nbr_color : type = int, nombre de couleurs diférentes
    
    Output : Array de la grille initiale
    
    """

    grill = []

    for col in range(width) :
        column = [random.randint(0,nbr_color-1) for line in range(width)]
        grill.append(column)
    return np.array(grill)

def LTCoordOfBox(boxx, boxy, width):
    # Returns the x and y of the left-topmost pixel of the xth & yth box.
    xmargin = int((WINDOWWIDTH - (width * Matrixsize)) / 2)
    ymargin = int((WINDOWHEIGHT - (width * Matrixsize)) / 2)
    return (boxx * Matrixsize + xmargin, boxy * Matrixsize + ymargin)


def ConstruGrille(board, width):
    for x in range(width):
        for y in range(width):
            left, top = LTCoordOfBox(x, y, width)
            r, g, b = COLORS[board[y][x]]

            pygame.draw.rect(DISPLAYSURF, (r, g, b), (left, top, Matrixsize, Matrixsize))

def AffichageTexte(count):
    countText = FONT.render("Nombre de Coups joués " + str(count), False, BLACK)
    DISPLAYSURF.blit(countText, (600, 20))
    resetText = FONT.render("Change size of the board and reset: ", False, BLACK)
    DISPLAYSURF.blit(resetText, (40,20))
    difficulty = FONT.render("Difficulty", False, BLACK)
    DISPLAYSURF.blit(difficulty, (0, 150))

def MajCell(grill ,new_val, old_val, pos_x, pos_y, width) : 
    """
    Description : fonction qui met a jour chaque cellule de la grille 
    
    Input : 
        - grill : type = array, matrice de taille width**2
        - new_val : type = int, nouvelle valeur de la case [0,0]
        - old_val : type = int, valeur actuelle de la case [0,0]
        - pos_x : type = int, position selon l'axe x
        - pos_y : type = int, position selon l'axe y
        - width : taille de la grille

    Output : Grille mise à jour 
    """

    if old_val == new_val or grill[pos_x][pos_y] != old_val:
        return 
    grill[pos_x][pos_y] = new_val 

    if pos_x > 0:
        MajCell(grill ,new_val, old_val, pos_x - 1, pos_y, width) 
    if pos_x < width - 1:
        MajCell(grill ,new_val, old_val, pos_x + 1, pos_y, width) 
    if pos_y > 0:
        MajCell(grill ,new_val, old_val, pos_x, pos_y - 1, width) 
    if pos_y < width - 1:
        MajCell(grill ,new_val, old_val, pos_x, pos_y + 1, width) 



def AssertEnd(grill) : 
    """
    Description : Fonction qui verifie si la grille est complète (i.e si toute les eléments de la matrice sont égaux)

    Input : 
        - grill : type = array, plateau de jeu

    Output : Booleen confirmant la fin de la partie (True) ou non (False)
    """
    init = grill[0][0]
    for x in grill : 
        for y in x : 
            if y != init :
                return False
    return True

def CreatButtons():
    buttons = []

    for x in range(4,33,4) : 
        buttons.append(PygameButton(RED, 285 + x/4 * 30, 17, 25, 25, str(x)))
    for x in range(3, 8) :
        buttons.append(PygameButton(YELLOW, 0, 100+25*x, 25,25, str(x), True))
    return buttons

def CreatPallete(nColors, width):
    """
    INUTILE
    """
    pallete = []
    for x in range (nColors):
        pallete.append(Colors(50*x, 750, x, width))
    return pallete

def Tourpartour(grill, width, old_val,listvalue, max_moves,counter = 0):
    
    """
    Description : Fonction recursive qui joue au tour par tour la partie
    
    Input : 
        - grill : type = array, plateau de jeu
        - width : type = int, taille de la grille
        - old_val : type = int, valeur actuelle de la case [0,0]
        - listvalue : type = list, liste des valeurs possibles de la nouvelle valeur de la case
        - counter : type = int, count du nombre de coups valables joués

    Output : la fin de la partie
    """

    end = AssertEnd(grill)
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
    MajCell(grill,new_val, old_val, 0,0, width)
    
    print(grill)
    print(counter)
    ConstruGrille(grill, width)

    pygame.display.update()
    Tourpartour(grill,width,new_val,listvalue, max_moves,counter)


    


def Partie(width, nbr_color) :
    """
    Description : Fonction qui produit une partie entière

    Input : 
        - width : type = int, taille de la longueur de la grille de taille width x width
        - nbr_color : type = int, nombre de couleurs diférentes
    
    Output : 
        déroulement de toute la partie
    """
    max_moves = np.round((25*(2*width)*nbr_color)/((14+14)*6))
    
    
    grill =   GenerateGrille(width, nbr_color)
    global COLORS, WINDOWWIDTH, WINDOWHEIGHT, DISPLAYSURF, FONT
    root = tk.Tk()
    root.withdraw()
    FPS = 10

    WINDOWWIDTH = WINDOWHEIGHT = Matrixsize*width + 200

    pygame.display.set_caption("Flood it!")
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    DISPLAYSURF.fill(GRAY)
    for x in range(0,nbr_color + 1) :
        PygameButton(COLORS[x],x * 25, 17, 25, 25, str(x)).Construction(DISPLAYSURF)

    listvalue = listvalue = ["{}".format(i) for i in range(nbr_color)]

    old_val= grill[0,0]

    
    print(grill)

    
    ConstruGrille(grill, width)
    FPSCLOCK.tick(FPS)

    pygame.display.update()

    Tourpartour(grill, width, old_val, listvalue,max_moves)

Partie(8,3)

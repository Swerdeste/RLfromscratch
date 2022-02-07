
from ast import While
from cgi import test
import random
import numpy as np

def GenerateGrille(width, nbr_color) : 

    """
    Description : fonction qui génère la grille

    Input : 
        - width : type = int, taille de la longueur de la grille de taille width x width
        - nbr_color : type = int, nombre de couleur diférentes
    
    Output : Array de la grille initiale
    
    """

    grill = []

    for col in range(width) :
        column = [random.randint(0,nbr_color-1) for line in range(width)]
        grill.append(column)
    return np.array(grill)



def MajCell(grill ,new_val, old_val, pos_x, pos_y, width) : 
    """
    Des
    
    """

    if old_val == new_val or grill[pos_x][pos_y] != old_val:
        return 
    grill[pos_x][pos_y] = new_val # change the color of the current box

    if pos_x > 0:
        MajCell(grill ,new_val, old_val, pos_x - 1, pos_y, width) # on box to the left
    if pos_x < width - 1:
        MajCell(grill ,new_val, old_val, pos_x + 1, pos_y, width) # on box to the right
    if pos_y > 0:
        MajCell(grill ,new_val, old_val, pos_x, pos_y - 1, width) # on box to up
    if pos_y < width - 1:
        MajCell(grill ,new_val, old_val, pos_x, pos_y + 1, width) # on box to down


print(type(random.randint(0,1)))


def AssertEnd(grill) : 
    init = grill[0][0]
    for x in grill : 
        for y in x : 
            if y != init :
                return False
    return True

def Tourpartour(grill, width, old_val,listvalue, counter = 0):
    end = AssertEnd(grill)
    if end == True: 
        return "EndGame"
    new_val_str = input("Couleur de case ? mettre 'end' pour finir :  ")
    while new_val_str not in listvalue:
        if new_val_str == "end" :
            return "Endgame"
        new_val_str = input("Couleur de case ? mettre 'end' pour finir :  ")
    new_val = int(new_val_str)
    if old_val != new_val :
        counter +=1 
    MajCell(grill,new_val, old_val, 0,0, width)
    
    print(grill)
    print(counter)
    Tourpartour(grill,width,new_val,listvalue, counter)
    


def Partie(width, nbr_color) :
    
    grill =   GenerateGrille(width, nbr_color)

    listvalue = listvalue = ["{}".format(i) for i in range(nbr_color)]

    old_val= grill[0,0]
    
    print(grill)

    Tourpartour(grill, width, old_val, listvalue)


#print(GenerateGrille(10,4))
#listvalue = ["{}".format(i) for i in range(4)]
#init_grille = np.array([[3,2,1,0,3,3,1,1,2,0], [1,0,2,0,3,1,1,3,0,0], [0,1,3, 3, 0, 0, 0, 3, 3, 0], [3, 2, 1, 1, 2, 2, 1, 2, 0, 3], [1, 3, 1, 0, 0, 0, 2, 1, 3, 2], [1, 3, 0, 3, 3, 3, 1, 2, 3, 2], [3, 3, 3, 1, 2, 0, 1, 3, 0, 3], [1, 2, 3, 3, 3, 1, 1, 3, 2, 2], [0, 2, 3, 1, 0, 1, 1, 1, 1, 2], [3, 2, 0, 1, 0, 1, 2, 3, 0, 3]])

#test_grille = np.array([[2,2,1,0,3,3,1,1,2,0], [1,0,2,0,3,1,1,3,0,0], [0,1,3, 3, 0, 0, 0, 3, 3, 0], [3, 2, 1, 1, 2, 2, 1, 2, 0, 3], [1, 3, 1, 0, 0, 0, 2, 1, 3, 2], [1, 3, 0, 3, 3, 3, 1, 2, 3, 2], [3, 3, 3, 1, 2, 0, 1, 3, 0, 3], [1, 2, 3, 3, 3, 1, 1, 3, 2, 2], [0, 2, 3, 1, 0, 1, 1, 1, 1, 2], [3, 2, 0, 1, 0, 1, 2, 3, 0, 3]])
#print(test_grille)
#MajCell(test_grille, 1, 2 ,0,0,10)
#print(MajCell(test_grille, 1, 2 ,0,0,10))
#Tourpartour(test_grille,10,2,0,listvalue)

Partie(12,5)
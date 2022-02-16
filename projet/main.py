

import random
import numpy as np

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
    if end == True: 
        return "EndGame"
    new_val_str = input("Couleur de case ? Mettre 'end' pour finir :  ")
    while new_val_str not in listvalue:
        if new_val_str == "end" :
            return "Endgame"
        new_val_str = input("Couleur de case ? Mettre 'end' pour finir :  ")
    new_val = int(new_val_str)
    if old_val != new_val :
        counter +=1 
    MajCell(grill,new_val, old_val, 0,0, width)
    
    print(grill)
    print(counter)
    if counter >= max_moves : 
        print( "You lost")
    else : 
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

    listvalue = listvalue = ["{}".format(i) for i in range(nbr_color)]

    old_val= grill[0,0]
    
    print(grill)

    Tourpartour(grill, width, old_val, listvalue,max_moves)


#print(GenerateGrille(10,4))
#listvalue = ["{}".format(i) for i in range(4)]
#init_grille = np.array([[3,2,1,0,3,3,1,1,2,0], [1,0,2,0,3,1,1,3,0,0], [0,1,3, 3, 0, 0, 0, 3, 3, 0], [3, 2, 1, 1, 2, 2, 1, 2, 0, 3], [1, 3, 1, 0, 0, 0, 2, 1, 3, 2], [1, 3, 0, 3, 3, 3, 1, 2, 3, 2], [3, 3, 3, 1, 2, 0, 1, 3, 0, 3], [1, 2, 3, 3, 3, 1, 1, 3, 2, 2], [0, 2, 3, 1, 0, 1, 1, 1, 1, 2], [3, 2, 0, 1, 0, 1, 2, 3, 0, 3]])

#test_grille = np.array([[2,2,1,0,3,3,1,1,2,0], [1,0,2,0,3,1,1,3,0,0], [0,1,3, 3, 0, 0, 0, 3, 3, 0], [3, 2, 1, 1, 2, 2, 1, 2, 0, 3], [1, 3, 1, 0, 0, 0, 2, 1, 3, 2], [1, 3, 0, 3, 3, 3, 1, 2, 3, 2], [3, 3, 3, 1, 2, 0, 1, 3, 0, 3], [1, 2, 3, 3, 3, 1, 1, 3, 2, 2], [0, 2, 3, 1, 0, 1, 1, 1, 1, 2], [3, 2, 0, 1, 0, 1, 2, 3, 0, 3]])
#print(test_grille)
#MajCell(test_grille, 1, 2 ,0,0,10)
#print(MajCell(test_grille, 1, 2 ,0,0,10))
#Tourpartour(test_grille,10,2,0,listvalue)

Partie(14,5)

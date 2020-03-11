# auteur: Baptiste Lacroix
#lien GitHub: https://github.com/BaptisteLacroix/Puissance4

from random import randint


def initGrid(n,m):
    """
    Génération de la matrice
    """
    matrice = [['.' for i in range(m)] for j in range(n)]
    return matrice


def printGrid(matrice):
    """
    Génération de la grille
    """
    print('\n ', end=' ')
    for i in range(1, len(matrice[0])+1):
        print(i, end='  ')
    print('\n')
    compteur=1
    for line in matrice:
        print(compteur, end=' ')
        compteur += 1
        for row in line:
            print(row,' ', end='')
        print('\n')
    return


def extrait_ligne(matrice,x,y):
    """
    Extraction de la ligne
    """
    resultat = matrice[x] #on récupère la ligne à la position x
    return resultat


def extrait_colonne(matrice,x,y):
    """
    Extraction de la colonne
    """
    resultat = []
    for ligne in matrice: #pour chaque ligne (x)
        resultat.append(ligne[y]) #on prends l'élément à l'indice y (colonne)
    return resultat


def extrait_diagonale1(matrice,x,y):
    """
    Extraction de la diagonale
    """
    resultat = []
    ligne = x
    colonne = y
    while (ligne>0) and (colonne>0): # remonte au bord
        ligne = ligne-1
        colonne = colonne-1
    while (ligne<len(matrice)) and (colonne<len(matrice[0])): # redescent au bout de la diagonale
        resultat.append(matrice[ligne][colonne])
        ligne = ligne+1
        colonne = colonne+1
    return resultat


def extrait_diagonale2(matrice,x,y):
    """
    Extraction de la seconde diagonale
    """
    resultat = []
    ligne = x
    colonne = y
    while (ligne<len(matrice)-1) and (colonne>0): # redescent au bord
        ligne = ligne+1
        colonne = colonne-1
    while (ligne >= 0) and (colonne<len(matrice[0])): # redescent au bout de la diagonale
        resultat.append(matrice[ligne][colonne])
        ligne = ligne-1
        colonne = colonne+1
    return resultat


def liste_gagnante(liste,pion):
    """
    Vérification si 4 pions allignés
    """
    compteur=0
    for i in range(len(liste)):
        if liste[i]==pion:  #si trouve un pion, on incrément compteur qui compte les pions
            compteur+=1
            if compteur == 4:
                return True #si 4 à la suite, on retourne vrai
        else:
            compteur=0 #on remet le compteur à 0 dès que c'est autre chose que le pion
    return False


def maximum_liste(liste): 
    """      
    renvoie l'indice du max dans une liste de nombres
    """
    maximum=0
    indice=0
    for i in range(len(liste)):   #parcourt la liste
        if liste[i]>maximum:
            maximum=liste[i]   
            indice=i           
    return indice              #retourne l'indice


def colonne_possible(matrice,x):
    """
    Vérifie que la colonne n'est pas pleine
    """
    if x<0 or x>len(matrice):
        return False
    print(x)
    if matrice[0][x] == '.':
        return True
    else:
        return False


def coord_de_chute(matrice,y):  
    """
    Renvoie le numéro de la ligne du jeton
    une fois qu'il est tombé.
    """
    coord = extrait_colonne(matrice,0,y)
    numero=-1
    while numero+1 < len(coord) and coord[numero+1] == '.':
        numero += 1
    return numero
    

def insert_jeton(matrice,pion,colonne):
    """
    Permet d'insérer le jeton dans la matrice
    """
    for i in range(1 ,len(matrice) + 1):
        if matrice[len(matrice)-i][colonne] == ".":
            matrice[len(matrice)-i][colonne] = pion #remplace le dernier . par le pion
            return matrice


def point_gagnant(matrice,x,y,pion):
    """
    Vérifie si le point est gagnant
    """
    if liste_gagnante(extrait_colonne(matrice,x,y),pion) or liste_gagnante(extrait_diagonale1(matrice,x,y),pion) or liste_gagnante(extrait_diagonale2(matrice,x,y),pion) or liste_gagnante(extrait_ligne(matrice,x,y),pion):
        return True
    else:
        return False


def colonnes_pleines(matrice):
    """
    Renvoie le nombre de colonnes pleines
    """
    nbr_c=0  #compte le nombre de colonnes pleines
    for i in range(len(matrice[0])):
        if not colonne_possible(matrice,i):
            nbr_c+=1
    return nbr_c


def joueurs(matrice,joueur1,joueur2):   
    """
    Fonction qui créée l'interface Joueur contre Joueur
    """
    
    while not False:
        y=-1
        if colonnes_pleines(matrice)==len(matrice[0]): #égalité
            print("Égalité")
            return

        while not colonne_possible(matrice,y):  #Vérifie pion dans colonne
            y=int(input("Joueur1 : Donnez le numéro de colonne que vous voulez de 1 à "+str(len(matrice[0]))+" :"))-1
        #print("avant",matrice)
        x=coord_de_chute(matrice,y)
        matrice=insert_jeton(matrice,joueur1,y)
        #print("apres",matrice)
        printGrid(matrice)

        if point_gagnant(matrice,x,y,joueur1):
            print("♦♦♦Joueur1 GAGNE♦♦♦")
            return
        y=-1

        while not colonne_possible(matrice,y):  #Vérifie pion dans colonne
            #print(matrice)
            y=int(input("Joueur2 : Donnez le numéro de colonne que vous voulez de 1 à " + str(len(matrice[0])) + " :"))-1
        x=coord_de_chute(matrice,y)
        matrice=insert_jeton(matrice,joueur2,y)
        printGrid(matrice)

        if point_gagnant(matrice,x,y,joueur2):
            print("♦♦♦Joueur2 GAGNE♦♦♦")
            return
    return


def Joueur_IA(matrice,joueur1,joueur2):
    """
    Fonction qui créée l'interface Joueur contre IA
    """
    while True:
        if colonnes_pleines(matrice)==len(matrice[0]): #égalité
            print("♦♦♦Égalité♦♦♦")
            return

        y=-1

        while not colonne_possible(matrice,y):  #Vérifie pion dans colonne
            y=int(input("Joueur1 : Donnez le numéro de colonne que vous voulez de 1 à "+str(len(matrice[0]))+" :"))-1
        #print("avant",matrice)
        x=coord_de_chute(matrice,y)
        matrice=insert_jeton(matrice,joueur1,y)
        #print("apres",matrice)
        printGrid(matrice)

        if point_gagnant(matrice,x,y,joueur1):
            print("♦♦♦Joueur1 GAGNE♦♦♦")
            return
        y=-1

        print('Ordinateur : ')
        y=randint(0,m-1) 

        while not colonne_possible(matrice,y):  #Vérifie qu'on peut mettre un jeton dans cette colonne
            y=randint(0,m-1)
        x=coord_de_chute(matrice,y)  #calcule les coordonnées de chute du jeton pour extraire les 4 listes
        matrice=insert_jeton(matrice,joueur2,y)   #insere le jeton
        printGrid(matrice)
        

        if point_gagnant(matrice,x,y,joueur2):
            print("♦♦♦IA GAGNE♦♦♦")
            return


def main():
    global m
    
    n = int(input("Choisissez le nombres de lignes que vous voulez (n'oubliez pas qu'il faut minimum 4 lignes) : "))
    while n < 4:
        n=0
        n = int(input("Choisissez le nombres de lignes que vous voulez (n'oubliez pas qu'il faut minimum 4 lignes) : "))
        
    m = int(input("Choisissez le nombres de colonnes que vous voulez (n'oubliez pas qu'il faut minimum 4 colonnes) : "))
    while m < 4:
        m=0
        m = int(input("Choisissez le nombres de colonnes que vous voulez (n'oubliez pas qu'il faut minimum 4 colonnes) : "))
        
    matrice = initGrid(n,m)
    printGrid(matrice)
    
    while True:
        try:
            reponse = int(input("Taper : \n 1 Joueur vs Joueur \n 2 Joueur vs ia (IA joue au hasard) \n 3 Quitter :"))
            break

        except ValueError:   #Alerte
            print("Erreur veuillez réessayer")
    
    if reponse==1:
        joueur1 = str(input("Joueur 1 choisissez votre avatar (1 caractère maximum) : "))
        if len(joueur1) != 1:
            joueur1 = str(input("Joueur 1 choisissez votre avatar (1 caractère maximum) : "))
        joueur2 = str(input("Joueur 2 choisissez votre avatar (1 caractère maximum) : "))
        if len(joueur2) != 1 or joueur2 == joueur1:
            joueur2 = str(input("Joueur 2 choisissez votre avatar (1 caractère maximum) : "))
        printGrid(matrice)
        joueurs(matrice,joueur1,joueur2)
        
    elif reponse==2:
        print("Attention le pion de l'IA' est X.")
        joueur2 = 'X'
        joueur1 = str(input("Joueur 1 choisissez votre avatar (1 caractère maximum) : "))
        if len(joueur1) != 1 or joueur1 == joueur2:
            joueur1 = str(input("Joueur 1 choisissez votre avatar (1 caractère maximum) : "))
        printGrid(matrice)
        Joueur_IA(matrice,joueur1,joueur2)
        
    elif reponse==3:
        print("Au revoir.")
    else:
        main()   #relance la fonction
    return

main() 



""" Pour les tests

matrice = 
[['.','.','.','O','.','.','.'],
['.','.','.','O','.','.','.'],
['.','.','.','O','.','.','.'],
['.','.','.','X','.','.','.'],
['.','.','.','X','X','.','.'],
['O','O','.','X','O','.','.']]
"""
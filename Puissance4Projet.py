from random import randint

def initGrid(n,m):
    matrice = [['.' for i in range(m)] for j in range(n)]
    return matrice






def printGrid(matrice):
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
    resultat = matrice[x] #on récupère la ligne à la position x
    return resultat





def extrait_colonne(matrice,x,y):
    resultat = []
    for ligne in matrice: #pour chaque ligne (x)
        resultat.append(ligne[y]) #on prends l'élément à l'indice y (colonne)
    return resultat






def extrait_diagonale1(matrice,x,y):
    resultat = []
    l = x
    c = y
    while (l>0) and (c>0): # remonte au bord
        l = l-1
        c = c-1
    while (l<len(matrice)) and (c<len(matrice[0])): # redescent au bout de la diagonale
        resultat.append(matrice[l][c])
        l = l+1
        c = c+1
    return resultat







def extrait_diagonale2(matrice,x,y):
    resultat = []
    l = x
    c = y
    while (l<len(matrice)-1) and (c>0): # redescent au bord
        l = l+1
        c = c-1
    while (l >= 0) and (c<len(matrice[0])): # redescent au bout de la diagonale
        resultat.append(matrice[l][c])
        l = l-1
        c = c+1
    return resultat






def liste_gagnante(liste,pion):
    if liste.count(pion) == 4:
        return True
    else:
        return False







def colonne_possible(matrice,x):
    if x<0 or x>len(matrice):
        return (False)
    if matrice[0][x] == '.':
        return (True)
    else:
        return (False)





def coord_de_chute(matrice,y):  #la fonction coord_de_chute() prend en paramètres une matrice et un entier n° Colonne qui renvoie le numéro de la ligne du jeton une fois qu'il est tombé.
    coord = extrait_colonne(matrice,0,y)
    numero=-1
    while numero+1 < len(coord) and coord[numero+1] == '.':
        numero += 1
    return numero
    """
    for numero in range(len(coord)):
        if coord[numero]!='.':
            return numero  #renvoie le n° de ligne de chute
    return 6
    """
    






def insert_jeton(matrice,pion,colonne):
    for i in range(1 ,len(matrice) + 1):
        if matrice[len(matrice)-i][colonne] == ".":
            matrice[len(matrice)-i][colonne] = pion #remplace le dernier . par le pion
            return matrice







def point_gagnant(matrice,x,y,pion):
    if liste_gagnante(extrait_colonne(matrice,x,y),pion) or liste_gagnante(extrait_diagonale1(matrice,x,y),pion) or liste_gagnante(extrait_diagonale2(matrice,x,y),pion) or liste_gagnante(extrait_ligne(matrice,x,y),pion):
        return True
    else:
        return False






def colonnes_pleines(mat): #renvoie le nombres de colonnes pleines
    nbr_c=0  #compte le nombre de colonnes pleines
    for i in range(len(matrice[0])):
        if not colonne_possible(matrice,i):
            nbr_c+=1
    return nbr_c






def joueurs(matrice,joueur1,joueur2):   #Joueur vs Joueur
    
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

    while True:
        if colonnes_pleines(matrice)==len(matrice[0]): #égalité
            print("♦♦♦Égalité♦♦♦")
            return

        y=-1

        while not colonne_possible(matrice,y):
            y=int(input("Joueur1 : Donnez le numéro de colonne que vous voulez de 1 à "+str(len(matrice[0]))+" :"))-1
        matrice=insert_jeton(matrice,joueur1,y)
        printGrid(matrice)
        x=coord_de_chute(matrice,y)   #calcule les coordonnées de chute du jeton pour extraire les 4 listes
        if point_gagnant(matrice,x,y,joueur1):
            print("♦♦♦Humain GAGNE♦♦♦")
            return

        print('Ordinateur : ')
        y=randint(0,6) 

        while not colonne_possible(matrice,y):  #Vérifie qu'on peut mettre un jeton ds cette colonne
            y=randint(0,6)
        matrice=insert_jeton(matrice,joueur2,y)   #insere le jeton
        printGrid(matrice)
        x=coord_de_chute(matrice,y)  #calcule les coordonnées de chute du jeton pour extraire les 4 listes

        if point_gagnant(matrice,x,y,joueur2):
            print("♦♦♦IA GAGNE♦♦♦")
    return






def main(matrice,joueur1,joueur2):
    n = int(input("Choisissez le nombres de lignes que vous voulez (n'oubliez pas qu'il faut minimum 4 lignes) : "))
    m = int(input("Choisissez le nombres de colonnes que vous voulez (n'oubliez pas qu'il faut minimum 4 colonnes) : ")
    while True:
        try:
            reponse = int(input("Taper : \n 1 Joueur vs Joueur \n 2 Joueur vs ia (IA joue au hasard) \n 3 Quitter :")) #test si bonne valeur entrée
            break

        except ValueError:          #Alerte
            print("Erreur veuillez réessayer")
    
    if reponse==1:
        printGrid(matrice)
        joueurs(matrice,joueur1,joueur2)
    elif reponse==2:
        printGrid(matrice)
        Joueur_IA(matrice,joueur1,joueur2)
    elif reponse==3:
        print("Au revoir.")
    else:
        main(matrice,joueur1,joueur2)   #relance la fonction
    return


joueur1='O'
joueur2='X'
printGrid(matrice) 
main(matrice,joueur1,joueur2) 





"""matrice = 
[['.','.','.','O','.','.','.'],
['.','.','.','O','.','.','.'],
['.','.','.','O','.','.','.'],
['.','.','.','X','.','.','.'],
['.','.','.','X','X','.','.'],
['O','O','.','X','O','.','.']]
"""
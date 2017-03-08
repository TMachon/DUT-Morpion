############################################################################################################
## Procédure partieMorpion()                                                                              ##
##      Cette procédure gère le déroulement de la partie, et la vonlonté de rejouer du/des utilisateur(s) ##
def partieMorpion () :
    jouer = True #Vrai si le(s) joueur(s) souhaite(nt) faire une partie
    while (jouer) :
        print("\n<!> Le format de réponse pour placer un caractère est '12' pour le placer première ligne, deuximème colonne -par exemple- <!>\n")
        i = 9
        victoire = False #Vrai si l'un des deux joueurs gagne
        cases = [[" "," "," "],[" "," "," "],[" "," "," "]]
        while (not victoire and i>0) : #Tant que personne n'a gagné, et que la grille n'est pas complète(i>0)
            afficherTableau(cases)
            cases=tourJoueur(cases, i%2)
            if (i<=6) : #On ne vérifie la victoire qu'à partir du 3eme tour car il est impossible de gagner avant
                victoire = verifVictoire(cases)
            i-=1
        if (i==0) : #Si la grille est remplié = Si personne n'a gagné
            afficherTableau(cases)
            print("\n -> Egalité !")
        jouer = bool(int(input("\nVoulez-vous rejouer ? (1 pour oui, 0 pour non) ")))


########################################################################################
## Prodédure afficherTableau(tableau2D de chaînes : tab)                              ##
##           tab : contient le contenu des cases du morpion                           ##
##      Cette procédure permet d'afficher le morpion avec le contenu du tableau2D tab ##
def afficherTableau(tab) :
    print("   1   2   3")
    print("  -----------")
    print("1|",tab[0][0],"|",tab[0][1],"|",tab[0][2],"|")
    print(" |---+---+---|")
    print("2|",tab[1][0],"|",tab[1][1],"|",tab[1][2],"|")
    print(" |---+---+---|")
    print("3|",tab[2][0],"|",tab[2][1],"|",tab[2][2],"|")
    print("  -----------")


##################################################################################################
## Fonction tourJoueur(tableau2D de chaïnes : tab, entier : tour) retourne tableau2D de chaïnes ##
##          tab : contient le contenu des cases du morpion                                      ##
##          tour : définit si c'est le tour du joueur 1(tour=1) ou du joueur 2(tour=0)          ##
##      Cette fonction gère la saisie de l'utilisateur chaque joueur en fonction du tour        ##
def tourJoueur(tab, tour) :
    if (tour==1) : #Si c'est le tour du joueur 1
        caractere = "X"
        while (True) :
            choix = str(input("Joueur 1 : Où voulez-vous placer 'X' ?\n"))
            if (verifPlaceLibre(tab, choix)) :
                break
    else : #Si c\'est le tour du joueur 2
        caractere = "O"
        while (True) :
            choix = str(input("Joueur 2 : Où voulez-vous placer 'O' ?\n"))
            if (verifPlaceLibre(tab, choix)) :
                break 
        
    tab[int(choix[0])-1][int(choix[1])-1] = caractere
    return tab


##############################################################################################
## Fonction verifPlaceLibre(tableau2D de chaïnes : tab, entier : val) retourne booléen      ##
##          tab : contient le contenu des cases du next                                     ##
##          val : contient l'emplacement de case saisie par l'utilisateur                   ##
##      Cette fontion vérifie que l'emplacement saisi par l'utilisateur est valide et libre ##
def verifPlaceLibre(tab, val) :
    if (int(val[0])<=3 and int(val[0])>=1 and int(val[1])<=3 and int(val[1])>=1 and tab[int(val[0])-1][int(val[1])-1]==" ") :
    # Si la valeur saisie par l'utilisateur est bien dans la grille, et sur un emplacement libre
        return True
    else :
        print("Erreur : valeur erronée !")
        return False

#########################################################################
## Fonction verifVictoire(tableau2D de chaïnes : tab) retourne booléen ##
##          tab : contient le contenu des cases du morpion             ##
##      Cette fonction permet de verifier si un des joueur a gagné     ##
def verifVictoire(tab) :
    vainqueur = "n/d"
    #Les conditions suivantes testent chacune des lignes possible pour savoir si l'un des deux joueurs l'a rempli
    if (tab[0][0]==tab[0][1]==tab[0][2]!=" ") :
        if (tab[0][0]=="X") :
            vainqueur = "1"
        else :
            vainqueur = "2"
    elif (tab[1][0]==tab[1][1]==tab[1][2]!=" ") :
        if (tab[1][0]=="X") :
            vainqueur = "1"
        else :
            vainqueur = "2"
    elif (tab[2][0]==tab[2][1]==tab[2][2]!=" ") :
        if (tab[2][0]=="X") :
            vainqueur = "1"
        else :
            vainqueur = "2"
    elif (tab[0][0]==tab[1][0]==tab[2][0]!=" ") :
        if (tab[0][0]=="X") :
            vainqueur = "1"
        else :
            vainqueur = "2"
    elif (tab[0][1]==tab[1][1]==tab[2][1]!=" ") :
        if (tab[0][1]=="X") :
            vainqueur = "1"
        else :
            vainqueur = "2"
    elif (tab[0][2]==tab[1][2]==tab[2][2]!=" ") :
        if (tab[0][2]=="X") :
            vainqueur = "1"
        else :
            vainqueur = "2"
    elif (tab[0][0]==tab[1][1]==tab[2][2]!=" ") :
        if (tab[0][0]=="X") :
            vainqueur = "1"
        else :
            vainqueur = "2"
    elif (tab[0][2]==tab[1][1]==tab[2][0]!=" ") :
        if (tab[0][2]=="X") :
            vainqueur = "1"
        else :
            vainqueur = "2"
            
    if (vainqueur=="n/d") : #Si aucune ligne n'est rempli par un joueur = Si personne n'a gagné
        return False
    else :
        afficherTableau(tab)
        print("\n -> Victoire du joueur ",vainqueur)
        return True    


def main () :
    print("\n -- Bienvenue dans ce jeu de morpion (alias TicTacToe) --")
    print(" -- Le joueur 1 commence, et joue avec 'X'. Le joueur 2 joue avec 'O' --")
    partieMorpion()
    
main()

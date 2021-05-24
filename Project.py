#####################
# BI TD 3
# Groupe 3 informatique
# Membre du groupe :
#   SETIA Danielle
#   VOLPE Alexandra
#   COTTIGNIES Leya
#   PONCHELET Arthur (abandon du projet dès le début)
#   ELEVE FANTOME
# url de dépot du projet github :
# https://github.com/uvsq22007117/Generation_2_Terrain_FP

#####################
#Fonctionnement:
    #Au début, vous devez dans le terminal écrire deux valeur (hauteur et longueur). On conseil du 500*500.
    #Afin de générer un terrain, vous pouvez appuyez sur le bouton "génération de terrain"
    #Puis,afin de générer le robot, cliquez sur une parcelle de terre.
    #Pour le faire bouger, vous pouvez utiliser les flèches directionelles de votre clavier.
    #Si vous voulez supprimer FP, vous pouvez appuyer sur le bouton "supprimer fp!"
    #Vous pouvez sauvegarder un terrain en cliquant sur "sauvegarder le terrain", puis lorsque vous générez de nouveau un terrain,
    #   en appuyant sur "charger le terrain" vous revenez sur le terrain précédament sauvegarder.
#####################
# debut du code

#####################
# import des modules

import tkinter as tk
import copy
import random as rd
import math


#####################
# constantes

p = 0, 5
n = 4
T = 0
k = 1

HAUTEUR = int(input("hauteur"))
LARGEUR = int(input("largeur"))
COTE = 10
NB_COL = LARGEUR // COTE
NB_LIG = HAUTEUR // COTE

COULEUR_QUADR = "grey20"
COULEUR_FOND = "grey60"


######################
# variables globales
# liste à deux dimensions telle que tableau[i][j] vaut 0
# si la case (i, j) est morte
# et vaut l'identifiant du carré dessiné à la case (i, j) sinon

tableau = []
coord_cases_bleus = []
val = 0
delai = 100
cpt = 0
deplacement = []
fp_position = [0, 0]

###################
# fonctions


def quadrillage():
    """Dessine un quadrillage dans le canevas avec des carrés de côté COTE"""
    y = 0
    while y <= HAUTEUR:
        canvas.create_line((0, y), (LARGEUR, y), fill=COULEUR_QUADR)
        y += COTE
    i = 0
    while i * COTE <= LARGEUR:
        x = i * COTE
        canvas.create_line((x, 0), (x, HAUTEUR), fill=COULEUR_QUADR)
        i += 1


def xy_to_ij(x, y):
    """Retourne la colonne et la ligne correspondant au
       point du canevas de coordonnées (x,y)"""
    return x // COTE, y // COTE


def change_carre():
    for i in range(0, NB_COL):
        for j in range(0, NB_LIG):
            p = rd.random()
            if p <= 0.5:
                COULEUR_CARRE = "blue"
                tableau[i][j] = 1
            else:
                COULEUR_CARRE = "red"
                tableau[i][j] = 0
            x = COTE*i
            y = COTE*j
            # x et y pixel & j et i colonne et ligne
            carre = canvas.create_rectangle((x, y), (x + COTE, y + COTE), fill=COULEUR_CARRE, outline=COULEUR_QUADR)
    etape()


def trouver_cases_bleus():
    coord_cases_bleus.clear()
    for i in range(0, NB_COL):
        for j in range(0, NB_LIG):
            if tableau[j][i] == 1:
                coord_cases_bleus.append(tuple([j*10, i*10]))
                #print( coord_cases_bleus )


def nb_vivant(i, j):
    """Retourner le nombre de cases voisines vivantes de la case de coordonnées (i, j)"""
    T = 0
    for k in range(max(0, i-1), min(NB_COL, i+2)):
        for el in range(max(0, j-1), min(NB_LIG, j+2)):
            if tableau[k][el] != 0 and [k, el] != [i, j]:
                #voit quelle case est vivante autour de celle de position [i, j]
                T += 0.125
                #un voisin "bon" = 1/8 et à partir de 5/8 la case change
    return T


def automate(i, j):
    """change la couleur d'un carré du quadrillage selon le nombre son nombre de voisins d'ordre k"""
    x = COTE*i
    y = COTE*j
    n = nb_vivant(i, j)
    if tableau[i][j] == 0:
        if n >= 0.625:
            COULEUR_CARRE = "blue"
            canvas.create_rectangle((x, y), (x + COTE, y + COTE), fill=COULEUR_CARRE, outline=COULEUR_QUADR)
            return 1
        else:
            COULEUR_CARRE = "red"
            canvas.create_rectangle((x, y), (x + COTE, y + COTE), fill=COULEUR_CARRE, outline=COULEUR_QUADR)
            return 0
    if tableau[i][j] == 1:
        if n >= 0.625:
            COULEUR_CARRE = "blue"
            canvas.create_rectangle((x, y), (x + COTE, y + COTE), fill=COULEUR_CARRE, outline=COULEUR_QUADR)
            return 1
        else:
            COULEUR_CARRE = "red"
            canvas.create_rectangle((x, y), (x + COTE, y + COTE), fill=COULEUR_CARRE, outline=COULEUR_QUADR)
            return 0


def etape():
    """Fait une étape du jeu de la vie"""
    for i in range(4):
        global tableau
        # copie du tableau
        tableau_res = copy.deepcopy(tableau)
        # traiter toutes les cases du tableau
        for i in range(NB_COL):
            for j in range(NB_LIG):
                tableau_res[i][j] = automate(i, j)
        # on modifie le tableau global
        tableau = tableau_res
        trouver_cases_bleus()


def fp_carre(event):
    """fait apparaître fp sur le terrain par un clic gauche sur une case de terre"""
    global cpt
    x, y = 0, 0
    if cpt < 1:
        i, j = xy_to_ij(event.x, event.y)
        if tableau[i][j] == 0:
            COULEUR_CARRE = "green"
            x = math.floor(event.x / 10) * 10
            y = math.floor(event.y / 10) * 10
            fp_position[0] = x
            fp_position[1] = y
            fp = canvas.create_rectangle((x, y), (x+10, y+10), fill=COULEUR_CARRE, tags='fp')
            cpt += 1


def supp_fp():
    """supprime fp du terrain"""
    global cpt
    canvas.delete("fp")
    cpt = 0


def deplacer(event):
    """faire bouger fp avec les flèches directionnelles"""
    a, b = 0, 0

    if event.keysym == 'Left':
        a = -10
    elif event.keysym == 'Right':
        a = 10
    elif event.keysym == 'Up':
        b = -10
    elif event.keysym == 'Down':
        b = 10

    next_position = [fp_position[0] + a, fp_position[1] + b]

    # interdire le deplacement dans l'eau
    if tuple(next_position) in coord_cases_bleus:
        tk.messagebox.showerror("Not a ground", "You can't move, this area is a part of the sea")

    # interdire le deplacement en dehors du terrain
    elif (next_position[0] < 0 or next_position[1] < 0 or next_position[0] > HAUTEUR or next_position[1] > LARGEUR):
        tk.messagebox.showerror("Out of bounds", "You can't move, this area is out of bounds")

    else:
        canvas.move('fp', a, b)
        deplacement.append(event.keysym)
        update_fp_position(a, b)


def charger():
    """charger la grille depuis le fichier sauvegarde.txt"""
    global tableau
    fic = open("sauvegarde.txt", "r")
    canvas.delete("all")
    quadrillage()
    j = 0
    for ligne in fic:
        i = 0
        val = ligne.split()
        for e in val:
            if e == "0":
                COULEUR_CARRE = "red"
            else:
                COULEUR_CARRE = "blue"
            x = i * COTE
            y = j * COTE
            carre = canvas.create_rectangle((x, y), (x + COTE, y + COTE), fill=COULEUR_CARRE, outline=COULEUR_QUADR)
            tableau[i][j] = carre
            i += 1
        j += 1
    fic.close()


def update_fp_position(a, b):
    """mettre a jour la position de fp"""
    fp_position[0] = fp_position[0] + a
    fp_position[1] = fp_position[1] + b
    #print(fp_position)


def sauvegarder():
    """sauvegarder la grille vers le fichier sauvegarde.txt"""
    fic = open("sauvegarde.txt", "w")
    for j in range(NB_LIG):
        for i in range(NB_COL):
            if tableau[i][j] == 0:
                fic.write("0 ")
            else:
                fic.write("1 ")
        fic.write("\n")
    fic.close()


def undo():
    """annuler la dernière action, ici le déplacement de fp"""
    if(len(deplacement) != 0):
        a, b = 0, 0
        dernier_mouvement = deplacement[-1]
        if dernier_mouvement == 'Left':
            a = 10
        elif dernier_mouvement == 'Right':
            a = -10
        elif dernier_mouvement == 'Up':
            b = 10
        elif dernier_mouvement == 'Down':
            b = -10
        canvas.move('fp', a, b)
        deplacement.pop()
        update_fp_position(a, b)
    else:
        tk.messagebox.showerror("Undo Error", "No more steps left to undo")


#A voir - on peut entrer des valeurs mais pas quitter directement la fenêtre (et je ne sais pas si les valeurs sont prisent en compte ou pas)
def parametre():
    """affiche une fenêtre pour parametrer la valeur des variables p, T, n et k"""
    global p, T, n, k
    fenetre = tk.Tk()
    fenetre1 = tk.Canvas(fenetre, width=400, height=400)
    fenetre1.grid(rowspan=5, columnspan=2)
    label_1 = tk.Label(fenetre, text="valeur de p")
    parametre_1 = tk.Entry(fenetre)
    label_1.grid(row=0, column=0)
    parametre_1.grid(row=0, column=1)
    label_2 = tk.Label(fenetre, text="valeur de T")
    parametre_2 = tk.Entry(fenetre)
    label_2.grid(row=1, column=0)
    parametre_2.grid(row=1, column=1)
    label_3 = tk.Label(fenetre, text="valeur de n")
    parametre_3 = tk.Entry(fenetre)
    label_3.grid(row=2, column=0)
    parametre_3.grid(row=2, column=1)
    label_4 = tk.Label(fenetre, text="valeur de k")
    parametre_4 = tk.Entry(fenetre)
    label_4.grid(row=3, column=0)
    parametre_4.grid(row=3, column=1)
    valider = tk.Button(fenetre, text="valider", command=fenetre1.quit).grid(row=4)
    fenetre1.destroy()
    quadrillage()
    fenetre.mainloop()


#####################
# programme principal

for i in range(NB_COL):
    tableau.append([0] * NB_LIG)

racine = tk.Tk()
racine.title("génération de terrain")


# création des widgets
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg=COULEUR_FOND)
bout_commencer = tk.Button(racine, text="générer un terrain", command=change_carre)
bout_supp = tk.Button(racine, text="supprimer fp", command=supp_fp)
bout_sauvegarde = tk.Button(racine, text="sauvegarder le terrain", command=sauvegarder)
bout_charge = tk.Button(racine, text="charger un terrain", command=charger)
bout_retour = tk.Button(racine, text="undo", command=undo)
bout_parametre = tk.Button(racine, text="choix des paramètres", command=parametre)
canvas.bind("<Button-1>", fp_carre)


# placement des widgets
canvas.grid(row=0, rowspan=6)
bout_commencer.grid(row=0, column=1)
bout_supp.grid(row=1, column=1)
bout_sauvegarde.grid(row=2, column=1)
bout_charge.grid(row=3, column=1)
bout_retour.grid(row=4, column=1)
bout_parametre.grid(row=5, column=1)


# programme principal
quadrillage()
racine.bind("<Key>", deplacer)
racine.mainloop()
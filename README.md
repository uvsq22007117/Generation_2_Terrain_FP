Bienvenue sur le programme de génération de terrain. 
Ici, vous faites bouger FP ;notre petit robot; sur un terrain qui est généré aléatoirement avec des zones d'eau et de terre.
Il a été réalisé par le groupe Trois du TD-3 De Bio-Info (L1 2020-2021)


# Membres:

Cottignies Leya 

Ponchelet Arthur (abandon projet)

Setia Danielle

Volpe Alexandra

Elève Fantome

# Explication du projet:
Le programme consiste à créer un terrain d'eau et de terre de façon aléatoire où se déplace un personnage (un carré vert), "fp".
L'eau est représentée par le bleu, la terre par le rouge.
Fp ne se déplace que sur les cases de terre.

# Séquençage du projet:

-auteur

-import des modules

-constantes

-variables globales

-fonctions

-programme principal_1

-création des widgets

-placement des widgets

-programme principal_2

# Fonctionnement:
Au début, vous devez dans le terminal écrire deux valeurs (hauteur et longueur). Nous vous conseillons du 500*500.
Afin de générer un terrain, vous pouvez appuyer sur le bouton "génération de terrain"
Puis, afin de générer le robot, cliquez sur une parcelle de terre.
Pour le faire bouger, vous pouvez utiliser les flèches directionnelles de votre clavier.
Si vous voulez supprimer FP, vous pouvez appuyer sur le bouton "supprimer fp!"
Vous pouvez sauvegarder un terrain en cliquant sur "sauvegarder le terrain", puis lorsque vous générez de nouveau un terrain,
en appuyant sur "charger le terrain" vous revenez sur le terrain précédemment sauvegardé.

# Explication des différentes fonctions:

quadrillage:
Le quadrillage est dessiné dans le canevas avec des carrés de côté variable "COTE" par l'intermédiaire d'une double boucle while.

xy_to_ij:
On retourne la colonne et la ligne correspondant au point du canevas de coordonnées (x,y) 

change_carre:
On définit deux sortes de carré, les bleus pour l'eau et les rouges pour la terre dans une double boucle for, comprenant un "if-else". 
Les carrés sont définis selon une variable "COTE" et sont générés aléatoirement par l'intermédiaire de la bibliothèque Random.

trouver_cases_bleus:
On recherche les coordonnées des cases bleus dans le tableau [i,j].
On utilise une double boucle for, et un if.

nb_vivant:
On retourner le nombre de cases voisines vivantes de la case de coordonnées (i, j) afin de voir ce qu'il y a autour de nos cases,
cela fait en sorte qu'à partir d'une certaine variable, la case ne peut plus se générer. 
Un voisin dit "bon" se créer à 1/8 et à partir de 5/8 la case change. 

automate:
On créer le fait qu'une case soit bleu soit rouge.
On définit qu'une case est bleue ou rouge selon la fonction nb_vivant. 
Afin d'y parvenir, on utilise un double if - if+else dans les deux cas (bleu et rouge). Puis on retourne les fonctions. 

etape:
On fait appel à un tableau afin de faire une étape de la création du terrain.
Cela fait en sorte qu'une étape fait une génération, et une autre, une nouvelle génération.

fp_carre:
On créer notre robot "FP", qui est un carré de dimension x,y et de couleur "COULEUR_CARRE".

supp_fp:
On créer une simple fonction qui vas supprimer le canva créé précédemment.

deplacer:
A l'aide de fonction event.keysym (qui permette de repérer qu'elle touche est invoqué),
on définit que les touches du clavier "flèches directionnelles" amène à une étape, 
soit bouger d'un certain a ou b. 
Puis dans une triple "if+elif+else" on interdit les bordures bleu et les cotés du canva central.

charger:
Ici, on charge la grille/ le terrain définit dans la sauvegarde par l'intermédiaire du tableau. 
On utilise une double boucle for et un if+else afin d'y parvenir.

update_fp_position:
On actualise les positions de fp

sauvegarder:
On sauvegarde la grille vers le fichier sauvegarde.txt. 
Pour cela on créer un fichier savegarde.txt dans la variable fic, 
puis à l'aide d'une double boucle for et if+else on permet de sauvegarder le terrain. 

undo:
On annule le déplacement du dernier mouvement.
On utilise une double boucle "if+else" et "if+elif+elif+elif",
tout en actualisant les positions de fp.

parametre:
/!\ Cette partie n'est pas totalement fonctionnel. La fenêtre s'affiche, mais on ne peut pas régler les différents paramètres.
On affiche une nouvelle fenêtre pour paramétrer les variables.
Pour cela, on utilise un bouton menant à des zones de textes que l'on peut remplir avant de valider.

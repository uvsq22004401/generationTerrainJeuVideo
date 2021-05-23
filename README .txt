#########################################
# Informations liées au groupe :
# groupe LDDMP 1
# Nikita DE LA FOURNIERE
# Malek WALLIER
# Theotime MAMOU				
# Auguste MAJOU
# Gregoire DUNGLAS
# Keli xaviera DZOUOSSIA MOZIE
# URL de github : 
#########################################


Bienvenue sur le README de notre projet d'informatique : "Génération de terrain" 



Le principe du projet "Génération de terrain" est de faire bouger un personnage

sur un terrain composé de cases de différentes natures. 

Les cases peuvent être des cases de terre ou d'eau. 

Le personnage ne peut se déplacer que sur des cases de terres. 

Afin d'unifier le terrain et de le rendre plus réaliste,

un automate cellulaire est appliqué au terrain, permettant de regrouper 

les cases d'un même type entre elles en modifiant la nature de certaines cases, 

selon le voisinage des cases définies par les variables T et k. 






Vous trouverez ici les fonctionnements des variables , des boutons 
et des binds.

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---


	VARIABLES :

 - k : correspond à l'ordre du voisinage, c'est à dire la distance à laquelle les 
       cases compteront pour l'automate. 
       (Pour plus d'information, cherchez "Voisinage de Moore" sur Internet)

 - T : c'est la valeur du voisinage, c'est-à-dire combien de cases d'eau sont nécessaires 
       pour modifier la nature d'une case terre en case eau ou de laisser la nature 
       d'une case non modifiée (c'est-à-dire d'eau vers eau ou de terre vers terre)

	-> Explication : si une case est entouré d'un nombre T de cases d'eau,
		         la case devient une case d'eau ou le reste. 
		         Par contre, si ce nombre n'est pas atteint,
			 la nature de la case devient de terre.

 
 - p_eau : correspond à la propabilité d'une case du terrain soit composée d'eau
           lors de la génération initiale du terrain. 
           (avant que l'automate entre en action)

 - n : définit le nombre de fois que l'automate entre en action 
       et donc le nombre de fois que le terrain sera changé selon l'automate
       (la nature d'une case sera donc redéfini n fois)


--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---


	BOUTONS :

 -  Générer des terrains : Ce bouton vous permettera de créer un terrain
			   sur la grille au dessus de ce bouton, contenant des 
			   cases vertes (correspondant à la terre) et des 
			   cases bleues (correspondant à l'eau) 


 -  Sauvegarder le terrain : Ce bouton vous permettera de sauvegarder un seul terrain.
			     Si vous réutilisez ce bouton, le terrain précédement 
			     sauvegardé sera effacé pour pouvoir sauvegarder le 
			     nouveau terrain.


 -  Charger le terrain : Ce bouton vous permettera de recharger le terrain sauvegardé.

 
 -  Changer les paramètres : Ce bouton ouvrira une fenêtre "menu" vous permettant de 
			     faire varier les valeurs des variables: k , T , p_eau et n.

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
	

	BINDS :

 - 1 : Pour placer le personnage sur le terrain il suffit de cliquer sur une case terre.
	(une case noire apparaitera, représentant le personnage)

 - 2 : Pour déplacer le personnage vous pouvez utiliser ZQSD ou 
       les flèches directionnelles du clavier.

	- Z ou ↑ pour aller vers le haut

	- S ou ↓ pour aller vers le bas

	- Q ou ← pour aller vers la gauche

	- D ou → pour aller vers la droite

- 3 : Pour annuler un déplacement du personnage , appuyez sur "suppr".


- 4 : Pour enlever le personnage du terrain, re-cliquez dessus.


--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---


Pour finir , un des objectifs de ce projet était de voir comment les variables influaient 

sur la probabilité que le personnage puisse joindre les bouts du terrain, 

c'est-à-dire si les cases de terre sont suffisamment nombreuses pour lui permettre.


 - p_eau : Plus la probabilité originel qu'une case soit d'eau est élevée, 
           plus le personnage aura des difficultés à atteindre les bouts du terrain.

 - T : Si c'est le paramètre T qui est augmenté, il y aura moins de cases d'eau 
       car cela signifie qu'il faut plus de cases d'eau aux environs d'une case 
       pour la transformer ou la maintenir en eau. 
       Le personnage aura donc plus de facilités à joindre les bouts de la carte 
       avec T plus grand.

 - k : A l'inverse, si c'est le paramètre k qui est augmenté, le personnage aura plus 
       de difficulté à traverser le terrain, car comme plus de cases sont prises 
       en compte dans l'automate, il y a plus de chance de trouver T cases d'eau
       et donc que la case en question devienne/reste une case d'eau

 - n : La modification de n peut aider la traversée ou la rendre plus compliqué.
       En effet, ce paramètre dépend des autres car si les paramètres favorisant
       la traversée sont élevé (T),chaque augmentation de n rendra le passage plus facile.
       Mais si les paramètre entravant le trajet sont augmenté (p_eau et k) 
       chaque augmentation de n rendra le passage plus hardu et moins probable.



			
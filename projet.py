#########################################
# Informations liées au groupe :
# groupe LDDMP 1
# Nikita DE LA FOURNIERE
# Malek WALLIER
# Theotime MAMOU
# Auguste MAJOU
# Gregoire DUNGLAS
# Keli xaviera DZOUOSSIA MOZIE
#########################################



#########################################
#Import des librairies
import random as rd
import tkinter as tk
import pickle as pck
#########################################



#########################################
#DEFINITION DES CONSTANTES
LARGEUR = 500
HAUTEUR = 500
p_eau = 0.5
#########################################



#########################################
#DEFINITION DES VARIABLES GLOBALES
couleurInitiale=""
listeCases = []
save = [listeCases]
#########################################


#########################################
#DEFINITION DES FONCTIONS
def couleurTerrain() :
    global couleurInitiale, p_eau
    a=rd.randint(1,100)
    if a<=p_eau*100 :
        couleurInitiale="blue"
    elif a>1-p_eau*100 :
        couleurInitiale="green"

def generationTerrains () :
    global couleurInitiale, listeCases
    for i in range(0,LARGEUR,10) :
        for j in range(0,HAUTEUR,10) :
            couleurTerrain()
            canvas.create_rectangle((i,j), (i+10,j+10), outline = "black", fill=couleurInitiale)
            identitéCase= [couleurInitiale,i,j]
            listeCases.append(identitéCase)
    print(listeCases)

def sauvegarde ():
    with open('save.pkl','wb' ) as savepickle :
        pck.dump(save,savepickle)

def reload ():
    global listeCases
    with open('save.pkl', 'rb') as savepickle:
        données = pck.load(savepickle)
    données = données[0]
    listeCases = données
    for i in range(len(données)):
        case = données[i]
        x = case[1]
        y = case[2]
        couleur = case[0]
        canvas.create_rectangle((x,y), (x+10,y+10), outline = "black", fill=couleur)

#########################################

#########################################
#PROGRAMME PRINCIPAL 

racine = tk.Tk()

canvas = tk.Canvas(racine, bg="white", width = LARGEUR, height = HAUTEUR)
canvas.grid(column=0,row=0)
for i in range(0,LARGEUR,10) :
    for j in range(0,HAUTEUR,10) :
        canvas.create_rectangle((i,j), (i+10,j+10), outline = "black")
button = tk.Button(racine, text="générer des terrains", command = generationTerrains)
button.grid(column=0, row=1)

button2 = tk.Button(racine, text="SauvegarderTerrain", command =sauvegarde)
button2.grid(column=0, row=2)

button3 = tk.Button(racine, text="reload", command =reload)
button3.grid(column=0, row=3)

racine.mainloop()
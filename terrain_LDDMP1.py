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
from copy import deepcopy
#########################################



#########################################
#DEFINITION DES CONSTANTES
LARGEUR = 500
HAUTEUR = 500
p_eau = 0.5
k = 1
T = 5
n = 4 
#########################################



#########################################
#DEFINITION DES VARIABLES GLOBALES
couleurInitiale=""
listeCases = []
save = [listeCases]
Hist_mouv =[]
Pers = 1
Position = 0
#########################################



#########################################
#DEFINITION DES FONCTIONS

def couleurTerrain() : # fonction assignant à chaques cases une couleur et donc si il s'agit d'une case terre ou eau
    
    global couleurInitiale, p_eau
    
    a=rd.randint(1,100)
    
    if a<=p_eau*100 :
        couleurInitiale="blue"
    elif a>1-p_eau*100 :
        couleurInitiale="green"


def automate(): # fonction définissant l'automate cellulaire 
    
    global listeCases , k , T
    
    listeBis = deepcopy(listeCases)
    voisin = [0]
    voisin2 = [0]
    
    for a in range(1, k+1):
        voisin.insert(0, a*(-1))
        voisin.append(a)
        voisin2.insert(0, a*(-50))
        voisin2.append(50*a)
    for i in range(len(listeCases)):
        VAL = 0
        for x in range(len(voisin2)):
            v2 = voisin2[x]
            for v in range(len(voisin)):
                v1 = voisin[v]
                b = i + v1 + v2
                if b >= 0 and b <= 2499 and b != i:
                    c = listeCases[b][0]
                    if c == 'blue':
                        VAL = VAL + 1
        if VAL >= T :
            listeBis[i][0] = 'blue'
        else :
            listeBis[i][0] = 'green'
    for i in range(len(listeBis)):
        case = listeBis[i]
        x = case[1]
        y = case[2]
        couleur = case[0]
        canvas.create_rectangle((x,y), (x+10,y+10), outline = "black", fill=couleur)
    listeCases = deepcopy(listeBis)


def generationTerrains () : # permet de créer le terrain en assignant à chacune des cases une identité (coordonées et couleur) contenue dans une liste
    
    global couleurInitiale, listeCases , n, Pers, Position, Hist_mouv , LARGEUR , HAUTEUR
    
    listeCases = []
   
    for i in range(0,LARGEUR,10) :
        for j in range(0,HAUTEUR,10) :
            couleurTerrain()
            canvas.create_rectangle((i,j), (i+10,j+10), outline = "black", fill=couleurInitiale)
            identitéCase= [couleurInitiale,i,j]
            listeCases.append(identitéCase)
    for i in range(n):
        automate()
    Pers = 1
    Position = 0
    Hist_mouv = []



def sauvegarde (): # permet de sauvegarder le terrain en sauvegardant la liste du terrain sur un fichier pickle
    with open('save.pkl','wb' ) as savepickle :
        pck.dump(listeCases,savepickle)
        pck.dump(Position,savepickle)


def reload (): # permet de recharger le terrain depuis le fichier pickle 
    
    global listeCases, Position, Hist_mouv
    
    with open('save.pkl', 'rb') as savepickle:
        données = pck.load(savepickle)
        Position = pck.load(savepickle)
    listeCases = données
    for i in range(len(données)):
        case = données[i]
        x = case[1]
        y = case[2]
        couleur = case[0]
        canvas.create_rectangle((x,y), (x+10,y+10), outline = "black", fill=couleur)
    Hist_mouv = []


def pers_position(event): # permet de placer le personage sur le terrain 
    
    global listeCases, Pers, Position
    
    x = event.x
    y = event.y
    c1 = 0
    c2 = 0
    colonne = -1
    ligne = -1
    
    while c1 <= x:
        c1+=10
        colonne+=1
    while c2 <= y:
        c2+=10
        ligne+=1
    statut = listeCases[int((500/10)*int(colonne)+int(ligne))]
    couleur = statut[0]
    if couleur == "green" and Pers == 1:
        statut[0] = "black"
        Pers = 0
        Position = [colonne, ligne, c1, c2]
    if couleur == "black":
        statut[0] = "green"
        Pers = 1
        Position = 0
    canvas.create_rectangle((c1,c2), (c1-10,c2-10), outline = "black", fill= statut[0])


def mouvement(a, b, c, d): # permet au personage de se déplacer sur les cases de terre
    
    global Position, listeCases
    
    if Position != 0:
        if Position[a] != b:
            case1 = listeCases[int((500/10)*int(Position[0])+int(Position[1]))]
            case2 = listeCases[int((500/10)*int(Position[0]+c)+int(Position[1]+d))]
            if case2[0] == "green":
                c1, c2 = Position[2], Position[3]
                canvas.create_rectangle((c1,c2), (c1-10,c2-10),
                 outline = "black", fill= "green")
                if d == 0 :
                    c1 = c1 + 10*c
                    Position[0] += c
                    Position[2] += 10*c
                if c == 0 :
                    c2 = c2 + 10*d
                    Position[1] += d
                    Position[3] += 10*d
                canvas.create_rectangle((c1,c2), (c1-10,c2-10),
                 outline = "black", fill= "black")
                case2[0] = "black"
                case1[0] = "green"
            else:
                print("Le personnage ne peut pas aller sur l'eau")
        else:
            print("Le personnage doit rester sur le terrain")
    else:
        print("Le personnage n'est pas positionné ")

#################### SOUS FONCTION DE MOUVEMENT #################### DEBUT

def mouv_haut(event): # permet de déplacer le personage en haut
    global Hist_mouv
    mouvement(1, 0, 0, -1)
    Hist_mouv.append("Up")


def mouv_bas(event): # permet de déplacer le personage en bas
    global Hist_mouv
    mouvement(1, 49, 0, 1)
    Hist_mouv.append("Down")


def mouv_gauche(event): # permet de déplacer le personage à gauche
    global Hist_mouv
    mouvement(0, 0, -1, 0)
    Hist_mouv.append("Left")


def mouv_droite(event): # permet de déplacer le personage à droite
    global Hist_mouv
    mouvement(0, 49, 1, 0)
    Hist_mouv.append("Right")



def Annul_mouv(event): # permet d'annuler les mouvements du personage 
    global Hist_mouv
    if Hist_mouv[-1] == "Up":
        mouvement(1, 49, 0, 1)
    if Hist_mouv[-1] == "Down":
        mouvement(1, 0, 0, -1)
    if Hist_mouv[-1] == "Left":
        mouvement(0, 49, 1, 0)
    if Hist_mouv[-1] == "Right":
        mouvement(0, 0, -1, 0)
    del Hist_mouv[-1]

#################### SOUS FONCTION DE MOUVEMENT #################### FIN



def Paramètre():   # fonction qui créée une nouvelle fenêtre permettant de choisir les valeurs de toutes les variables
    
    menu = tk.Tk()

    BuK1 = tk.Button(menu, text="<" , command = baiK)
    BuK1.grid(column=0, row=0)

    BuK2 = tk.Button(menu, text=">", command =  augK)
    BuK2.grid(column=2, row=0)

    BuK3 = tk.Button(menu, text="k")
    BuK3.grid(column=1, row=0)

    But1 = tk.Button(menu, text="<" , command = baiT)
    But1.grid(column=0, row=1)

    But2 = tk.Button(menu, text=">", command =  augT)
    But2.grid(column=2, row=1)

    But3 = tk.Button(menu, text="T")
    But3.grid(column=1, row=1)

    Bup1 = tk.Button(menu, text="<" , command = baip_eau)
    Bup1.grid(column=0, row=2)

    Bup2 = tk.Button(menu, text=">", command =  augp_eau)
    Bup2.grid(column=2, row=2)

    Bup3 = tk.Button(menu, text="p_eau")
    Bup3.grid(column=1, row=2)

    Bun1 = tk.Button(menu, text="<" , command = bain)
    Bun1.grid(column=0, row=3)

    Bun2 = tk.Button(menu, text=">", command =  augn)
    Bun2.grid(column=2, row=3)

    Bun3 = tk.Button(menu, text="n")
    Bun3.grid(column=1, row=3)




#################### SOUS FONCTION DE PARAMETRE #################### DEBUT


def augK ():      # Sert à augmenter la valeur de la variable K

    global k
    
    k += 1
    print ("L'ordre du voisinage vaut : " , k)
    labelk['text'] = "k =" + str(k)

def baiK ():     # Sert à baisser la valeur de la variable K 
    
    global k
   
    if k > 1 :
        k -= 1
        print ("L'ordre du voisinage vaut : " , k)

    else : 
        print ("Erreur, l'ordre du voisinage vaut 1 , il ne peut donc plus baisser")
    labelk['text'] = "k =" + str(k)

def augT ():     # Sert à augmenter la valeur de la variable T
    
    global T
    
    T += 1
    print ("Le nombre de cases d'eau necéssaire dans le voisinage d'une case pour la transmormer en eau est : " , T)
    
    labelT['text'] = "T =" + str(T)

def baiT ():     # Sert à baisser la valeur de la variable T
    
    global T
    
    if T > 1 :
        T -= 1
        print ("Le nombre de cases d'eau necéssaire dans le voisinage d'une case pour la transmormer en eau vaut : " , T)

    else : 
        print ("Erreur, le nombre de cases d'eau necéssaire dans le voisinage d'une case pour la transmormer en eau est 1 , il ne peut donc plus baisser")
    
    labelT['text'] = "T =" + str(T)



def augp_eau ():     # Sert à augmenter la valeur de la variable p_eau , ici nous passons par "clone" pour éviter d'avoir à faire aux float, qui ne laisse pas de valeurs exactes dans le label
    
    global p_eau
    clone = p_eau*10

    if clone < 10 :
        clone += 1
        p_eau = clone/10
        print ("p_eau vaut : " , p_eau)
    
    else : 
        print ("Erreur, la probabilité de l'eau vaut 1 , elle ne peut donc plus augmenter")

    labelp['text'] = "p_eau =" + str(p_eau)

def baip_eau ():     # Sert à baisser la valeur de la variable p_eau , ici nous passons par "clone" pour éviter d'avoir à faire aux float, qui ne laisse pas de valeurs exactes dans le label
    
    global p_eau
    clone = p_eau*10
    
    if clone > 0 :
        clone -= 1
        p_eau = clone/10
        print ("La probabilité qu'une case soit une case d'eau vaut : " , p_eau)

    else : 
        print ("Erreur, la probabilité qu'une case soit une case d'eau vaut 0 , elle ne peut donc plus baisser")
    
    labelp['text'] = " p_eau =" + str(p_eau)



def augn ():     # Sert à augmenter la valeur de la variable n
    
    global n
    
    n += 1
    print ("l'automate passe " , n, 'fois')
    
    labeln['text'] = "n =" + str(n)

def bain ():     # Sert à baisser la valeur de la variable n
    
    global n
    
    if n > 0 :
        n -= 1
        print ("l'automate passe " , n, 'fois')
    
    else : 
        print ("Erreur, l'automate passe deja 0 fois , il ne peut donc plus baisser")

    labeln['text'] = "n =" + str(n)


#################### SOUS FONCTION DE PARAMETRE #################### FIN

def EasterEgg():
    import webbrowser

    webbrowser.open('http://youtube.com/watch?v=dQw4w9WgXcQ')




#########################################


#########################################
#PROGRAMME PRINCIPAL 

racine = tk.Tk()

# CANVAS

canvas = tk.Canvas(racine, bg="white", width = LARGEUR, height = HAUTEUR)
canvas.grid(column=0,row=0, columnspan=2)
for i in range(0,LARGEUR,10) :
    for j in range(0,HAUTEUR,10) :
        canvas.create_rectangle((i,j), (i+10,j+10), outline = "black")

# BIND

canvas.bind("<Button-1>", pers_position)

canvas.focus_set()
canvas.bind("z", mouv_haut)
canvas.bind("s", mouv_bas)
canvas.bind("q", mouv_gauche)
canvas.bind("d", mouv_droite)
canvas.bind("<Up>", mouv_haut)
canvas.bind("<Down>", mouv_bas)
canvas.bind("<Left>", mouv_gauche)
canvas.bind("<Right>", mouv_droite)
canvas.bind("<Delete>", Annul_mouv)

# BUTTON

button = tk.Button(racine, text="Générer des terrains", command = generationTerrains)
button.grid(column=0, row=1)

button2 = tk.Button(racine, text="Sauvegarder le terrain", command =sauvegarde)
button2.grid(column=0, row=2)

button3 = tk.Button(racine, text="Charger le terrain", command =reload)
button3.grid(column=0, row=3)

button4 = tk.Button(racine, text="Changer les paramètres", command =Paramètre)
button4.grid(column=0, row=4)

buttonRick = tk.Button(racine, text="", command =EasterEgg)
buttonRick.grid(column=2, row=4)

# LABEL

labelk = tk.Label(racine, text= "k =" + str(k))
labelk.grid(column = 1, row = 1)

labelT = tk.Label(racine, text= "T =" + str(T))
labelT.grid(column = 1, row = 2)

labelp = tk.Label(racine, text= "p_eau =" + str(p_eau))
labelp.grid(column = 1, row = 3)

labeln = tk.Label(racine, text= "n =" + str(n))
labeln.grid(column = 1, row = 4)



racine.mainloop()	

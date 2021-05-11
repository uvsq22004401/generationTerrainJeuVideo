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
k = 1
T = 5
n = 4 
#########################################



#########################################
#DEFINITION DES VARIABLES GLOBALES
couleurInitiale=""
listeCases = []
save = [listeCases]
Pers = 1
Position = 0
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

def Paramètre():
    global k
    
    menu = tk.Tk()

    Buv1 = tk.Button(menu, text="<" , command = baiK)
    Buv1.grid(column=0, row=0)

    Buv2 = tk.Button(menu, text=">", command =  augK)
    Buv2.grid(column=2, row=0)

    Buv3 = tk.Button(menu, text="Voisinage")
    Buv3.grid(column=1, row=0)

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


def generationTerrains () :
    global couleurInitiale, listeCases , n, Pers
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

def sauvegarde ():
    with open('save.pkl','wb' ) as savepickle :
        pck.dump(listeCases,savepickle)
        pck.dump(Position,savepickle)

def reload ():
    global listeCases, Position
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

def automate():
    global listeCases , k , T
    listeBis = list(listeCases)
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
                if b > 0 and b < 2500 :
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
    listeCases = listeBis





def augK ():
    global k
    
    k += 1
    print ("Le voisinage vaut : " , k)
    labelk['text'] = "k =" + str(k)


def baiK ():
    global k
    if k > 1 :
        k -= 1
        print ("Le voisinage vaut : " , k)

    else : 
        print ("Erreur, le voisinage vaut 1 , il ne peut donc plus baisser")
    labelk['text'] = "k =" + str(k)


def augT ():
    global T
    
    T += 1
    print ("T vaut : " , T)
    labelT['text'] = "T =" + str(T)


def baiT ():
    global T
    if T > 1 :
        T -= 1
        print ("T vaut : " , T)

    else : 
        print ("Erreur, le voisinage vaut 1 , il ne peut donc plus baisser")
    labelT['text'] = "T =" + str(T)

def augp_eau ():
    global p_eau
    clone = p_eau*10

    
    if clone < 10 :
        clone += 1
        p_eau = clone/10
        print ("p_eau vaut : " , p_eau)
    
    else : 
        print ("Erreur, la probabilité de l'eau vaut 1 , elle ne peut donc plus augmenter")

    labelp['text'] = "p_eau =" + str(p_eau)


def baip_eau ():
    global p_eau
    clone = p_eau*10
    if clone > 0 :
        clone -= 1
        p_eau = clone/10
        print ("La probabilité de l'eau vaut : " , p_eau)

    else : 
        print ("Erreur, la probabilité de l'eau vaut 0 , elle ne peut donc plus baisser")
    labelp['text'] = " p_eau =" + str(p_eau)


def augn ():
    global n
    
    n += 1
    print ("l'automate passe " , n, 'fois')
    labeln['text'] = "n =" + str(n)


def bain ():
    global n
    if n > 0 :
        n -= 1
        print ("l'automate passe " , n, 'fois')
    else : 
        print ("Erreur, l'automate passe deja 0 fois , il ne peut donc plus baisser")

    labeln['text'] = "n =" + str(n)


def pers_position(event):
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


def mouv_haut(event):
    global Position, listeCases
    if Position != 0 and Position[1] != 0:
        case1 = listeCases[int((500/10)*int(Position[0])+int(Position[1]))]
        case2 = listeCases[int((500/10)*int(Position[0])+int(Position[1])-1)]
        if case2[0] == "green":
            c1, c2 = Position[2], Position[3]
            canvas.create_rectangle((c1,c2), (c1-10,c2-10),
             outline = "black", fill= "green")
            c2 = c2 - 10
            canvas.create_rectangle((c1,c2), (c1-10,c2-10),
             outline = "black", fill= "black")
            case2[0] = "black"
            case1[0] = "green"
            Position[1] += -1
            Position[3] += - 10
        else:
            print("Le personnage ne peut pas aller sur l'eau")
    else:
        print("Le personnage n'est pas positionné ou sa position ne permet pas le deplacement demandé")

def mouv_bas(event):
    global Position, listeCases
    if Position != 0 and Position[1] != 49:
        case1 = listeCases[int((500/10)*int(Position[0])+int(Position[1]))]
        case2 = listeCases[int((500/10)*int(Position[0])+int(Position[1])+1)]
        if case2[0] == "green":
            c1, c2 = Position[2], Position[3]
            canvas.create_rectangle((c1,c2), (c1-10,c2-10),
             outline = "black", fill= "green")
            c2 = c2 + 10
            canvas.create_rectangle((c1,c2), (c1-10,c2-10),
             outline = "black", fill= "black")
            case2[0] = "black"
            case1[0] = "green"
            Position[1] += 1
            Position[3] += 10
        else:
            print("Le personnage ne peut pas aller sur l'eau")
    else:
        print("Le personnage n'est pas positionné ou sa position ne permet pas le deplacement demandé")

def mouv_gauche(event):
    global Position, listeCases
    if Position != 0 and Position[0] != 0 :
        case1 = listeCases[int((500/10)*int(Position[0])+int(Position[1]))]
        case2 = listeCases[int((500/10)*int(Position[0]-1)+int(Position[1]))]
        if case2[0] == "green":
            c1, c2 = Position[2], Position[3]
            canvas.create_rectangle((c1,c2), (c1-10,c2-10),
             outline = "black", fill= "green")
            c1 = c1 - 10
            canvas.create_rectangle((c1,c2), (c1-10,c2-10),
             outline = "black", fill= "black")
            case2[0] = "black"
            case1[0] = "green"
            Position[0] += -1
            Position[2] += - 10
        else:
            print("Le personnage ne peut pas aller sur l'eau")
    else:
        print("Le personnage n'est pas positionné ou sa position ne permet pas le deplacement demandé")

def mouv_droite(event):
    global Position, listeCases
    if Position != 0 and Position[0] != 49:
        case1 = listeCases[int((500/10)*int(Position[0])+int(Position[1]))]
        case2 = listeCases[int((500/10)*int(Position[0]+1)+int(Position[1]))]
        if case2[0] == "green":
            c1, c2 = Position[2], Position[3]
            canvas.create_rectangle((c1,c2), (c1-10,c2-10),
             outline = "black", fill= "green")
            c1 = c1 + 10
            canvas.create_rectangle((c1,c2), (c1-10,c2-10),
             outline = "black", fill= "black")
            case2[0] = "black"
            case1[0] = "green"
            Position[0] += 1
            Position[2] += 10
        else:
            print("Le personnage ne peut pas aller sur l'eau")
    else:
        print("Le personnage n'est pas positionné ou sa position ne permet pas le deplacement demandé")

#########################################


#########################################
#PROGRAMME PRINCIPAL 

racine = tk.Tk()

canvas = tk.Canvas(racine, bg="white", width = LARGEUR, height = HAUTEUR)
canvas.grid(column=0,row=0, columnspan=2)
for i in range(0,LARGEUR,10) :
    for j in range(0,HAUTEUR,10) :
        canvas.create_rectangle((i,j), (i+10,j+10), outline = "black")

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

button = tk.Button(racine, text="générer des terrains", command = generationTerrains)
button.grid(column=0, row=1)

button2 = tk.Button(racine, text="SauvegarderTerrain", command =sauvegarde)
button2.grid(column=0, row=2)

button3 = tk.Button(racine, text="reload", command =reload)
button3.grid(column=0, row=3)

button4 = tk.Button(racine, text="changerParamètre", command =Paramètre)
button4.grid(column=0, row=4)

labelk = tk.Label(racine, text= "k =" + str(k))
labelk.grid(column = 1, row = 1)

labelT = tk.Label(racine, text= "T =" + str(T))
labelT.grid(column = 1, row = 2)

labelp = tk.Label(racine, text= "p_eau =" + str(p_eau))
labelp.grid(column = 1, row = 3)

labeln = tk.Label(racine, text= "n =" + str(n))
labeln.grid(column = 1, row = 4)


racine.mainloop()

from turtle import *
speed(0)
#On trace les axes de coordonnnés
penup()
goto(-300,0)
pendown()
goto(300,0)#axe des abscisses
penup()
goto(0,-300)
pendown()
goto(0,300)#axe des ordonnées


class Point:
    couleur="red"
    def __init__(self,nom,abscisse,ordonnee):
        self.nom=nom
        self.x=abscisse
        self.y=ordonnee

    def dessine(self):
        penup()
        goto(self.x,self.y)
        pendown()
        dot(Point.couleur)
        write(self.nom,align="right")

class Carre:
    #Le sommet de coordonnées (X,Y) est le coin en bas à gauche du carré
    #Cote est la longueur du côté du carré
    def __init__(self,X,Y,Cote):
        self.x=X
        self.y=Y
        self.cote=Cote

    def dessine(self):
        penup()
        goto(self.x,self.y)
        pendown()
        pencolor("blue")
        #Question 1 : Compléter cette méthode qui doit tracer le carré
        # code pour tracer le carré
        left(90)
        forward(self.cote)
        right(90)
        forward(self.cote)
        right(90)
        forward(self.cote)
        right(90)
        forward(self.cote)
        
    def aire(self):
        aireC = self.cote * self.cote
        return aireC
        #Question 2 : Après avoir supprimé l'instruction pass, compléter cette méthode qui doit retourner l'aire du carré
        
        # code pour calculer l'air du carré
        

    def contientpoint(self,point):
        pass

Origine=Point("O",0,0)
Origine.dessine()

A=Point("A",25,75)
A.dessine()

B=Point("B",200,100)
B.dessine()

#Question 3
#Créer et dessiner les points C et D de coordonnées C(150,100) et D(-200,0)
# Creation des points C et D 
C=Point("C",150,100)
C.dessine()

D=Point("D",-200,0)
D.dessine()

#Question 4
#Créer et dessiner le carré appelé carre1 qui aura pour coin en bas à gauche le point A et pour côté 100 pixels

#on dessine carre1
carre1=Carre(25,75,100)
carre1.dessine()

#Question 5
#Faire afficher dans la console l'aire du carré carre1 ; on fera une phrase !
# Aire du carre1
Acarre1 = carre1.aire()
print("L'aire du carre1 est de", Acarre1)

#Question 6 : Dans la classe Carre, après avoir supprimé l'instruction pass, compléter la méthode contientpoint qui doit retourner True si le point (qui est un objet de la classe Point) est dans le carré, et False sinon

#Question 7
#En utilisant la méthode contientpoint, faire afficher dans la console True ou False suivant que la phrase "Le point C est dans le carré carre1" est vraie ou fausse

penup()
goto(200,100)
pendown()
pencolor("black")
forward(10)
left(90)
forward(10)
left(90)
forward(10)
left(90)
forward(10)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)

#Question 8
#En utilisant une boucle for et la classe Carre, dessiner, en partant du point D, une figure identique à celle présente à l'écran (les 5 carrés imbriqués les uns dans les autres en partant du point B)

#Question 9
#Ajouter un attribut couleur à la classe Carre. Cet attribut pourra être choisi par l'utilisateur lors de la création d'un nouvel objet, et il sera initialisé par défaut à "black") . NE PAS OUBLIER DE TESTER et MODIFIER VOTRE PROGRAMME POUR VERIFIER QUE CE NOUVEL ATTRIBUT EST BIEN PRIS EN COMPTE LORS DU DESSIN D'UN CARRE.

#Question 10
#En utilisant une boucle for et la classe Carre, dessiner la figure symétrique par rapport à l'axe des abscisses de celle présente à l'écran (les 5 carrés imbriqués les uns dans les autres en partant du point B)


exitonclick()


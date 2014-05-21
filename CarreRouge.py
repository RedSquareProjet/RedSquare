from tkinter import *


class Partie:
    def __init__(self):
        self.ListeRectangles = list()
        self.carreR = CarreRouge(self,0,0,0,0,0,1,1)
        # ajouter les 4 rectangles dans la liste ListeRectangles
        for i in range(0,4):
            self.ListeRectangles.append(Rectangle(self,0,0,0,0,0,1,1))
        
        print("Nombre d'elements dans self.ListeRectangles : " + str(len(self.ListeRectangles)))   
        self.Temps = 0.00
        print("partie cree")
    
    def demarrerChrono(self):
        pass
    
    def arreterChrono(self):
        pass
    
class CarreRouge():
    def __init__(self, parent, posXMin, posYMin, posXMax, posYMax, vitesse, dirX, dirY):
        self.parent = parent
        self.posXMin = posXMin
        self.posYMin = posYMin
        self.posXMax = posXMax
        self.posYMax = posYMax
        self.vitesse = vitesse
        self.dirX = dirX
        self.dirY = dirY
        print("carre cree")
    
    
class Rectangle:
    def __init__(self, parent,xMin, xMax, yMin, yMax, v, dirX, dirY):
        self.parent = parent
        self.posXMin = xMin
        self.posYMin = yMin
        self.posXMax = yMin
        self.posYMax = yMax
        self.vitesse = v
        self.directionX = dirX
        self.directionY = dirY

class Modele:
    def __init__(self, parent):
        self.parent = parent
        self.partie = Partie()
        self.ListePointage = list()
        print("modele cree")
        
    def ouvrirFichierTextePointage(self, modeLecture):
        if(modeLecture == 'a'):
            print("mode Append")
        elif (modeLecture == 'r'):
            print("mode Lecture")
            
        pass
    
    def demanderDemarrerNouvellePartie(self):
        pass
    
    def bougerRectangle(self):
        pass
    
    def demanderDemarrerChrono(self):
        pass
    
    def detecterCollision(self):
        pass
    
    def demanderArreterChrono(self):
        pass

class Vue:
    
    def __init__(self, parent):
        self.parent = parent
        self.root=Tk()
        self.canevas=Canvas(self.root,width=550,height=550,bg="green")
        self.canevas.pack()
        print("vue cree")
    
    def AfficherMenuPrincipal(self) :
        print("\n\n\n\n\n\n")
        print("Voici les options : ")
        print("1. Demarrer une nouvelle partie")
        print("2. Afficher les meilleurs pointages")
        print("3. Quitter")
    
    def afficherAireJeu(self):
        # test pour savoir si l'affichage initiale se fait bien : 
        #self.canevas.create_rectangle(j.x1,j.y1,j.x2,j.y2,fill="yellow", tags=("carre"))
        self.canevas.create_rectangle(10,10,110,110,fill="blue", tags=("rectangle"))
        self.canevas.create_rectangle(10,310,110,410,fill="blue", tags=("rectangle"))
        self.canevas.create_rectangle(310,10,410,110,fill="blue", tags=("rectangle"))
        self.canevas.create_rectangle(310,310,410,410,fill="blue", tags=("rectangle"))
    
    def afficherMenuJeu(self):
        pass   

    def detectionClique(self):
        pass
    
    def detectionDrag(self):
        pass
    
    def afficherFenetreFinPartie(self):
        pass
    
    def afficherPointages(self, listePointage):
        print("Nom, Pointage : ")
        for i in listePointage:
            print(i)

class Controleur:
    
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self)
        print("controleur cree")
        self.demanderAfficheAireJeu() # a mettre avant le mainloop
        self.vue.afficherAireJeu()
        self.vue.root.mainloop()
    
    def demanderOuvrirFichier(self):
        pass  
    
    def demanderAfficherMenuJeu(self):
        pass
    
    def demanderAfficheAireJeu(self):
        self.vue.afficherAireJeu()
    
    def demanderBougerRectangle(self):
        pass
    
    def demanderSiCollision(self):
        pass
    
    def demanderAfficherFinPartie(self):
        pass
    
    def demanderAfficherPointages(self):
        pass

    
if __name__ == "__main__" : 
    c = Controleur()
    































































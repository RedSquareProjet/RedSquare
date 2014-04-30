

class Modele:
    
    def __init__(self, parent):
        self.parent = parent
        print("modele cree")

class Vue:
    
    def __init__(self, parent):
        self.parent = parent
        print("vue cree")
    
    def AfficherMenuPrincipal(self) :
        print("\n\n\n\n\n\n")
        print("Voici les options : ")
        print("1. Demarrer une nouvelle partie")
        print("2. Afficher les meilleurs pointages")
        print("3. Quitter")
        

class Controleur:
    
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self)
        print("controleur cree")
        self.vue.AfficherMenuPrincipal()
        

    





if __name__ == "__main__" : 
    c = Controleur()































































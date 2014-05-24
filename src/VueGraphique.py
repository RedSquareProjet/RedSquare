from tkinter import *

class VueGraphique():
    def __init__(self):
        self.master = Tk()
        #self.parent = parent
        self.afficherMenu()

    ###################################### Centrer la fenêtre ########################################
    def centerWindows(self, width, height, window):
        w= width
        h= height

        sw= window.winfo_screenwidth()
        sh= window.winfo_screenheight()

        x= (sw - w)/2
        y= (sh - h)/2

        window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #################################################################################################
    #                                         Fenêtre Menu                                          #
    #################################################################################################

    ##################### Définition de fonctionnement des boutons pour le menu #####################
    def bouton_NouvellePartie(self):
        self.fenetreMenu.grid_forget()
        self.initialiserImage()
        self.afficherAireDeJeu()
        print("*** Nouvelle partie ***")
    #conexion au controleur

    def bouton_AfficherScore(self):
        self.fenetreMenu.grid_forget()
        self.afficherPointages()
        print("*** Scores ***")
    #conexion au controleur

    ######################################## Afficher Menu ##########################################
    def afficherMenu(self):
        self.master.title("Red Squar - Menu")

        self.fenetreMenu = Frame(self.master)
        self.fenetreMenu.grid()

        self.canevas = Canvas(self.fenetreMenu, width= 550, height= 550, bg= "gray10", bd= -2)
        self.canevas.grid()

        self.imgMenu = PhotoImage(file= "images/MenuImage.gif")
        self.canevas.create_image(0, 80, image =  self.imgMenu, anchor = NW)

        bouton_nouvellePartie = Button(self.fenetreMenu, text= "Nouvelle Partie", bg="red", fg="white", width= 30, height= 2, command= self.bouton_NouvellePartie)
        self.canevas.create_window(165, 300, anchor='nw', window= bouton_nouvellePartie)

        bouton_afficherScore = Button(self.fenetreMenu, text= "Afficher Score", bg="red", fg="white", width= 30, height= 2, command= self.bouton_AfficherScore)
        self.canevas.create_window(165, 360, anchor='nw', window= bouton_afficherScore)

        bouton_quitter = Button(self.fenetreMenu, text= "Quitter", bg="red", fg="white", width= 30, height= 2, command= self.master.destroy)
        self.canevas.create_window(165, 420, anchor='nw', window= bouton_quitter)

        self.centerWindows(550, 550, self.master)

    #################################################################################################
    #                                          Fenêtre Jeu                                          #
    #################################################################################################

    ################################ Initialiser les images du jeu ##################################
    def initialiserImage(self):
        self.imgRec60x60 = PhotoImage(file= "images/BleuRec60x60.gif")
        self.imgRec60x50 = PhotoImage(file= "images/BleuRec60x50.gif")
        self.imgRec30x60 = PhotoImage(file= "images/BleuRec30x60.gif")
        self.imgRec100x20 = PhotoImage(file= "images/BleuRec100x20.gif")
        self.imgCarreVivant = PhotoImage(file= "images/SquareAlive.gif")
        self.imgCarreMort = PhotoImage(file= "images/SquareDead.gif")
        print("*** Initialser Images Done... ***")

    #################################### Afficher Aire De Jeu #######################################
    def afficherAireDeJeu(self):
        self.master.title("Red Squar - Jeu")

        self.fenetreJeu = Frame(self.master)
        self.fenetreJeu.grid()

        self.canevas = Canvas(self.fenetreJeu, width= 550, height= 550, bg= "gray15")
        self.canevas.grid()

        """Bordure"""
        self.canevas.create_rectangle(0, 0, 550, 50, fill= "black")
        self.canevas.create_rectangle(0, 0, 50, 550, fill= "black")
        self.canevas.create_rectangle(0, 500, 550, 550, fill= "black")
        self.canevas.create_rectangle(500, 0, 550, 550, fill= "black")

        self.canevas.bind('<Button-1>', self.detectionClique)
        self.canevas.bind('<B1-Motion>', self.detectionDrag)

        self.afficherPartie(250, 250, 100, 100, 300, 85, 85, 350, 355, 340)

    ####################################### Afficher Partie #########################################
    def afficherPartie(self, CarreX, CarreY, Rec1x, Rec1y, Rec2x, Rec2y, Rec3x, Rec3y, Rec4x, Rec4y):
        self.CarreX = CarreX
        self.CarreY = CarreY

        self.Carre = self.canevas.create_image(CarreX, CarreY, image= self.imgCarreVivant, anchor= NW)
        self.Rec1 = self.canevas.create_image(Rec1x, Rec1y, image= self.imgRec60x60, anchor= NW)
        self.Rec2 = self.canevas.create_image(Rec2x, Rec2y, image= self.imgRec60x50, anchor= NW)
        self.Rec3 = self.canevas.create_image(Rec3x, Rec3y, image= self.imgRec30x60, anchor= NW)
        self.Rec4 = self.canevas.create_image(Rec4x, Rec4y, image= self.imgRec100x20, anchor= NW)

    #################################### Detection du clic ##########################################
    def detectionClique(self, event):
        global DETECTION_CLIC_SUR_CARRE_ROUGE

        # position du pointeur de la souris
        X = event.x
        Y = event.y
        print("Position du clic -> ", X, Y)

        # coordonnées du carré rouge
        xmin = self.CarreX
        ymin = self.CarreY
        xmax = self.CarreX + 40
        ymax = self.CarreY + 40
        print("Position objet -> ", xmin, ymin, xmax, ymax)

        if xmin <= X <= xmax and ymin <= Y <= ymax:
            DETECTION_CLIC_SUR_CARRE_ROUGE = True
        else:
            DETECTION_CLIC_SUR_CARRE_ROUGE = False

        print(DETECTION_CLIC_SUR_CARRE_ROUGE)

    ###################################### Detection du drag ########################################
    def detectionDrag(self, event):
        X = event.x
        Y = event.y

        if DETECTION_CLIC_SUR_CARRE_ROUGE:
            # limite de la zone du déplacement du carré
            if X < 50 : X = 50
            if X > 460 : X = 460
            if Y < 50 : Y = 50
            if Y > 460 : Y = 460
            self.CarreX = X
            self.CarreY = Y

            self.canevas.delete(self.Carre)
            self.canevas.delete(self.Rec1)
            self.canevas.delete(self.Rec2)
            self.canevas.delete(self.Rec3)
            self.canevas.delete(self.Rec4)
            self.afficherPartie(self.CarreX, self.CarreY, 100, 100, 300, 85, 85, 350, 355, 340)

    #################################################################################################
    #                                      Fenêtre Pointages                                        #
    #################################################################################################

     ################## Définition de fonctionnement ddubouton pour le menu score ###################
    def bouton_RetournerMenu(self):
        self.fenetrePointages.grid_forget()
        self.afficherMenu()

    ###################################### Afficher Pointages #######################################
    def afficherPointages(self):
        self.master.title("Red Squar - Pointages")

        self.fenetrePointages = Frame(self.master)
        self.fenetrePointages.grid()

        self.canevas = Canvas(self.fenetrePointages, width= 550, height= 550, bg= "gray10", bd= -2)
        self.canevas.grid()

        self.imgScores = PhotoImage(file= "images/ScoresImage.gif")
        self.canevas.create_image(0, 0, image =  self.imgScores, anchor = NW)

        bouton_retourneMenu = Button(self.fenetrePointages, text= "Retourner au menu", bg="red", fg="white", width= 30, height= 2, command= self.bouton_RetournerMenu)
        self.canevas.create_window(165, 480, anchor='nw', window= bouton_retourneMenu)

if __name__ == '__main__':
    v = VueGraphique()
    v.master.mainloop()
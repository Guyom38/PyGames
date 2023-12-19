import pygame

import Commun.variables as VAR
import Jeux.Serpent.variables as V_JEU

from Commun.fonctions import *
from Commun.constantes import *

class CSerpent:
    def __init__(self, moteur):
        self.MOTEUR = moteur
        
        self.corps = []
        self.corps.append( (10, 10) )
        
        self.longueur = 4
        self.en_mouvement = True
        self.direction = ENUM_DIR.DROITE
    
        self.RYTHME = CRythme(0.01)
        
    def get_longueur_serpent(self):
        return ( len(self.corps) )
    
    def controle_croissance(self):
        taille_corps = self.get_longueur_serpent()
        for _ in range ( taille_corps, self.longueur ):
            self.corps.append( (self.corps[taille_corps -1])) 
            
    def deplacement(self):       
        if not self.RYTHME.cycle():
            return 
        
        if self.direction == ENUM_DIR.GAUCHE: dx, dy = -1, 0
        elif self.direction == ENUM_DIR.DROITE: dx, dy = 1, 0
        elif self.direction == ENUM_DIR.HAUT: dx, dy = 0, -1
        elif self.direction == ENUM_DIR.BAS: dx, dy = 0, 1
        
        tete_x, tete_y = self.corps[0][0] + dx, self.corps[0][1] + dy        
        nouvelle_tete = (tete_x, tete_y)
        self.corps.insert(0, nouvelle_tete)
        self.corps.pop()
    
        self.controle_sortie_ecran()
        
    def position_tete(self):
        return self.corps[0][0], self.corps[0][1]
    
    def controle_sortie_ecran(self):
        dehors = False
        x, y = self.position_tete()
        dimx = VAR.resolution_x // V_JEU.cellule
        dimy = VAR.resolution_y // V_JEU.cellule
        
        if x < 0 : 
            x = dimx-1
            dehors = True
        if x > dimx -1: 
            x = 0
            dehors = True
        if y < 0 : 
            y = dimy -1
            dehors = True
        if y > dimy : 
            y = 0
            dehors = True
        
        if dehors:
            self.corps[0] = (x, y)
          
    def afficher(self):
        self.controle_croissance()
        self.deplacement()
        
        for index, bout_du_corps in enumerate(self.corps):
            x, y = bout_du_corps
            if index == 0:
                pygame.draw.rect(VAR.fenetre, (255, 0, 0), (x * V_JEU.cellule, y * V_JEU.cellule, V_JEU.cellule, V_JEU.cellule), 0)
            else:
                pygame.draw.rect(VAR.fenetre, (128, 0, 0), (x * V_JEU.cellule, y * V_JEU.cellule, V_JEU.cellule, V_JEU.cellule), 0)

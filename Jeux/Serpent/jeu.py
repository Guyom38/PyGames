import pygame
import Commun.variables as VAR

from Commun.base_jeu import *

import Jeux.Serpent.serpent as CS
import random

class Jeu(Base_Jeu):
    def __init__(self, moteur):
        self.MOTEUR = moteur
    
    def demarrer(self):
        self.serpent = CS.CSerpent(self.MOTEUR)
        
        self.boucle()
        
    
 
        
    def boucle(self):
        VAR.boucle = True   
        while VAR.boucle:
            VAR.fenetre.fill( (0, 0, 0 ))
            self.serpent.afficher()
            
            pygame.display.update()

        
    
    
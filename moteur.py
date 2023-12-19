# --- importation des librairies Pygame 
import pygame
from pygame.locals import *

import Commun.variables as VAR
import Commun.fonctions as FCT

from Commun.base_jeu import *

class CMoteur():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        
        VAR.fenetre = pygame.display.set_mode((VAR.resolution_x, VAR.resolution_y), pygame.FULLSCREEN     , 32)
        pygame.display.set_caption(VAR.titre)
        self.horloge = pygame.time.Clock()        
        
    def demarrer(self):     
        VAR.boucle = True   
        while VAR.boucle:
            
            jeu = charger_jeu(self, "Jeux.Serpent.jeu")
            jeu.demarrer()
            
            pygame.display.update()
            self.horloge.tick( VAR.fps_max )         
        pygame.quit() 
        
        
                

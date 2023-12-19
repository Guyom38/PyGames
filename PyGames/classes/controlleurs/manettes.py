import pygame
from pygame.locals import *

import time, random

import Commun.variables as VAR
from moteur.fonctions import *

from moteur.constantes import *


class CManettes():
    def __init__(self, controlleurs):
        self.MOTEUR = controlleurs.MOTEUR
        self.CONTROLLEURS = controlleurs
    
    def joueur_derriere_manette(self, id_manette):        
        if id_manette not in self.CONTROLLEURS.ASSOC_MANETTE_JOUEUR: 
            nouveau_joueur = CJoueur(self.MOTEUR, id_manette, 13.0 + random.randint(0, 1), 40.0 + random.randint(0, 1), "DINSI #"+str(id_manette), False)
            
            self.PERSONNAGES.JOUEURS.append(nouveau_joueur)
            self.CONTROLLEURS.ASSOC_MANETTE_JOUEUR[id_manette] = nouveau_joueur   
                 
        return id_manette, self.CONTROLLEURS.ASSOC_MANETTE_JOUEUR[id_manette]  
      
      
      
    def gestion_des_evenements(self, event):
        joueur_zero_bouge = 0
        
        id_manette, joueur = self.joueur_derriere_manette(event.joy)

        if VAR.PAUSE:
            return joueur_zero_bouge
        
        if event.type == pygame.JOYAXISMOTION:  
            if ENUM_DEMO.WEBSOCKET in VAR.demo:
                print("EVENEMENT CAPTURE : " + str(event))   
                   
            if event.axis == 0:
                if event.value < -0.5: 
                    joueur.direction, joueur.en_mouvement = ENUM_DIR.GAUCHE, True
                elif event.value > 0.5:                     
                    joueur.direction, joueur.en_mouvement = ENUM_DIR.DROITE, True
                else:
                    joueur.en_mouvement = False
                    
            if event.axis == 1:  
                if event.value > 0.5: 
                    joueur.direction, joueur.en_mouvement = ENUM_DIR.BAS, True
                elif event.value < -0.5 :                     
                    joueur.direction, joueur.en_mouvement = ENUM_DIR.HAUT, True
                else:
                    joueur.en_mouvement = False
            
            if event.axis == 2:
                if event.value == 1: joueur.direction, joueur.en_mouvement = ENUM_DIR.DIAGONAL1, True
                elif event.value == 2: joueur.direction, joueur.en_mouvement = ENUM_DIR.BAS, True
                elif event.value == 3: joueur.direction, joueur.en_mouvement = ENUM_DIR.DIAGONAL3, True
                elif event.value == 4: joueur.direction, joueur.en_mouvement = ENUM_DIR.GAUCHE, True                
                elif event.value == 6: joueur.direction, joueur.en_mouvement = ENUM_DIR.DROITE, True
                elif event.value == 7: joueur.direction, joueur.en_mouvement = ENUM_DIR.DIAGONAL7, True
                elif event.value == 8: joueur.direction, joueur.en_mouvement = ENUM_DIR.HAUT, True
                elif event.value == 9: joueur.direction, joueur.en_mouvement = ENUM_DIR.DIAGONAL9, True
                else: joueur.en_mouvement = False
                      
        elif event.type == pygame.JOYBUTTONDOWN :                    
            if event.button == ENUM_PAD.B_A:  pass  
            if event.button == ENUM_PAD.B_B:  pass
            if event.button == ENUM_PAD.B_X:  pass
            if event.button == ENUM_PAD.B_Y:  pass
            if event.button == ENUM_PAD.B_START:  pass
            if event.button == ENUM_PAD.B_SELECT: pass
 
        elif event.type == pygame.JOYBUTTONUP:      
            if event.button == ENUM_PAD.B_A:  
                if not joueur.MECANIQUE_OBJET == None:
                    joueur.MECANIQUE_OBJET.demarrer()
                
                self.PERSONNAGES.contact_avec_autres_personnes(joueur)
                    
            if event.button == ENUM_PAD.B_B:  
                joueur.MECANIQUE_ACTION.initialiser(CCourir(joueur))
                joueur.MECANIQUE_ACTION.demarrer()
                
            if event.button == ENUM_PAD.B_X: pass
            if event.button == ENUM_PAD.B_Y: pass                
                
            if event.button == ENUM_PAD.B_START:   pass
            if event.button == ENUM_PAD.B_SELECT:  pass

        if id_manette == 0 and joueur.en_mouvement:
            joueur_zero_bouge += 1
            
        return joueur_zero_bouge
    
    
        
            

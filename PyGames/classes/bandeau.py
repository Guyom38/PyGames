import pygame

import Commun.variables as VAR
from moteur.fonctions import *
from moteur.constantes import *

class CBandeau:
    def __init__(self, moteur):
        self.MOTEUR = moteur
        self.RYTHME = None
        
        
        self.pas = 64      
        self.etape = ENUM_PROGRESSION_ETAT.SE_DECHARGE
        
        self.frequence_animation = 0.01
        

        self.messages = []
         
        self.couleur_fond = (32,32,32, 200)
        self.cadre = None
        self.limite_largeur = 0
        self.mega = False
        
    def information(self, nom, equipe, texte):
        self.messages.append( (nom, equipe, texte, False) )
        
    def chapitre(self, texte):
        self.messages.append( ("", "", texte, True) )
       
    def preparation(self):
        if len(self.messages) > 0:
            
            texte = self.messages[0]
            self.mega = texte[3]
            del self.messages[0] 
                  
            if not self.mega:
                self.hauteur = 64
                self.x, self.y = VAR.resolution_x, VAR.resolution_y - self.hauteur - 16
                self.hauteurDiv2 = self.hauteur // 2
                self.hauteurMul2 = self.hauteur * 2
                self.pause = 2
                ecart_texte = self.hauteurMul2
            else:
                self.hauteur = 256
                self.x, self.y = VAR.resolution_x, 500
                self.hauteurDiv2 = self.hauteur // 2
                self.hauteurMul2 = self.hauteur * 2
                self.pause = 4
                ecart_texte = self.hauteur
            
             
            self.etape = ENUM_PROGRESSION_ETAT.SE_RECHARGE
                        
            self.cadre = pygame.Surface( (VAR.resolution_x, self.hauteur) ).convert_alpha()
            pygame.draw.rect(self.cadre, self.couleur_fond, (self.hauteurDiv2, 0, VAR.resolution_x - self.hauteurDiv2, self.hauteur))
            pygame.draw.circle(self.cadre, self.couleur_fond, (self.hauteurDiv2, self.hauteurDiv2), self.hauteurDiv2, 0)
            
            if not self.mega:
                pygame.draw.circle(self.cadre, VAR.couleurs_equipes[texte[1]], (self.hauteurDiv2, self.hauteurDiv2), 20, 0)
                image_texte = VAR.ECRITURES[30].render( texte[0] + ", "+ texte[2] , True, (255,255,255))  
                self.cadre.blit(image_texte, (ecart_texte, (self.hauteur - image_texte.get_height()) //2 ) )
                largeur_texte = image_texte.get_width()
                
            else:
                image_texte1 = VAR.ECRITURES[50].render( texte[2][0] , True, (255,255,255)) 
                image_texte2 = VAR.ECRITURES[30].render( texte[2][1] , True, (255,255,255))   
                
                hauteur_centre = ( self.hauteur - (image_texte1.get_height() + 16 + image_texte2.get_height() )) //2
                self.cadre.blit(image_texte1, (ecart_texte, hauteur_centre))
                self.cadre.blit(image_texte2, (ecart_texte, hauteur_centre + image_texte1.get_height()))

                largeur1 = image_texte1.get_width()
                largeur2 = image_texte2.get_width()
                largeur_texte = largeur1 if ( largeur1 > largeur2 ) else largeur2
            
            self.cadre.set_colorkey((0,0,0))            
            self.RYTHME = CRythme(self.frequence_animation)  
            
            self.limite_largeur = VAR.resolution_x - largeur_texte - (self.hauteurMul2)
            
        else:
            self.etape = ENUM_PROGRESSION_ETAT.AUCUN    
    
    def cycle(self):
        
        if self.cadre == None:
            self.preparation()
    
         # pas de bandeau, plus de message 
        if self.etape == ENUM_PROGRESSION_ETAT.AUCUN:
            return 
           
        if self.RYTHME.cycle():
            if self.etape == ENUM_PROGRESSION_ETAT.SE_RECHARGE:
                
                self.apparition()
            
            elif self.etape == ENUM_PROGRESSION_ETAT.PAUSE:
                self.apres_la_pause()
                        
            elif self.etape == ENUM_PROGRESSION_ETAT.SE_DECHARGE:
                if self.mega:
                    VAR.PAUSE = False     
                self.disparition()    
                        
        
        if not self.cadre == None:
            VAR.fenetre.blit(self.cadre, (self.x, self.y))
        
    
    def apres_la_pause(self):
        self.etape = ENUM_PROGRESSION_ETAT.SE_DECHARGE  
        self.RYTHME = CRythme(self.frequence_animation)   
        
    def disparition(self):
        self.x += (self.pas * 1.5)
        if self.x > VAR.resolution_x:
            self.cadre = None                  
            
    def apparition(self):
        self.x -= self.pas
        if self.x < self.limite_largeur:  
            self.RYTHME = CRythme(self.pause)   
            self.etape = ENUM_PROGRESSION_ETAT.PAUSE       
            
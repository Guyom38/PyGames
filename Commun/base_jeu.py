
import importlib
import os

class Base_Jeu:
    def demarrer(self):
        raise NotImplementedError   
    
         

def charger_jeu(moteur, jeu_nom):
    module = importlib.import_module(jeu_nom)
    jeu_class = getattr(module, 'Jeu')
    return jeu_class(moteur)
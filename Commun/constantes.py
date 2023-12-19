from enum import *

# --- Joueurs
class ENUM_DIR:    
    GAUCHE = 0
    DIAGONAL7 = 45
    HAUT = 90
    DIAGONAL9 = 135
    DROITE = 180
    DIAGONAL3 = 225
    BAS = 270
    DIAGONAL1 = 315    
    AUCUN = None

class ENUM_PAD:
    B_X = 0
    B_A = 1
    B_B = 2
    B_Y = 3
    B_L = 4
    B_R = 5
    B_START = 9
    B_SELECT = 8
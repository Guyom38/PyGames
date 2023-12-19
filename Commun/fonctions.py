import string
import random, math
import pygame
import os
import time

perfs = {}
def Performance(key, timer, couleur = (255,0,0)):
    valeur = (time.time() - timer)
    if valeur == 0:
        valeur = 0.000001
    if not key in perfs:
        perfs[key] = valeur, 0, 0, 0, couleur
    _ , maximum, somme, compteur, _ = perfs[key]
    
    if valeur > maximum:
        maximum = valeur
        
    perfs[key] = valeur, maximum, (somme + valeur), compteur+1, couleur
    
    return perfs

import math

# Exemple d'utilisation
# point1 = (1, 2)
# point2 = (4, 6)
# distance = calculer_distance(point1, point2)
# print("La distance est :", distance)

def calculer_distance(coord1, coord2):
    """
    Calcule la distance euclidienne entre deux points.

    :param coord1: Un tuple (x, y) représentant les coordonnées du premier point.
    :param coord2: Un tuple (x, y) représentant les coordonnées du deuxième point.
    :return: La distance euclidienne entre les deux points.
    """
    return math.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)


def GenereMat2D(dimX, dimY, valeurDefaut):
    return [[valeurDefaut for x in range(dimY)] for i in range(dimX)]

def generate_short_id(length=6):
    characters = string.ascii_uppercase + string.digits
    short_id = ''.join(random.choice(characters) for _ in range(length))
    return short_id


def contientDans(objet, objet_conteneur):
    xC, yC, dxC, dyC = objet_conteneur
    x, y, dx, dy = objet
    
    return (xC < x < xC + dxC and xC < x + dx < xC + dxC and
            yC < y < yC + dyC and yC < y + dy < yC + dyC)
    
def collision(objet1, objet2):
    x1, y1, dx1, dy1 = objet1
    x2, y2, dx2, dy2 = objet2
    
    if ((x2 >= x1 + dx1) 
            or (x2 + dx2 <= x1) 
            or (y2 >= y1 + dy1)
            or (y2 + dy2 <= y1)):

        return False
    else:
        return True

def split_list(lst):
    """
    Divise une liste en deux moitiés. Si la liste a un nombre impair d'éléments,
    la première moitié aura un élément de plus que la seconde.
    """
    # Calcul du point médian
    mid = len(lst) // 2 + len(lst) % 2

    # Division de la liste en deux moitiés
    first_half = lst[:mid]
    second_half = lst[mid:]

    return first_half, second_half
   
def existe_fichier(chemin):
    return (os.path.isfile(chemin))

def get_angle(x, y):
    angle_radians = math.atan2(y, x)
    angle_degrees = math.degrees(angle_radians)
    adjusted_angle = angle_degrees + 90
    if adjusted_angle < 0:
        adjusted_angle += 360
    return adjusted_angle

class CRythme:
    def __init__(self, frequence = 0.1, pas = 1, boucle = True):
        self.tempoTimer = time.time()
        self.tempo = 0
        self.frequence = frequence
        self.pas = pas 
        self.boucle = boucle
        
    def cycle(self):
        if self.frequence == -1:
            return True
        
        if time.time() - self.tempoTimer > self.frequence: 
            if self.boucle:
                self.tempo += self.pas
                self.tempoTimer = time.time()
            return True
        return False


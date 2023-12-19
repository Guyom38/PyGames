from Commun.fonctions import *
from Commun.constantes import *

titre = "PyGames"
joueur_clavier = False
fps_max = 25
resolution_x = 1920
resolution_y = 1080

websocket_name = "noEscape"
web_socket_id_partie = generate_short_id()
urlQrCode = "https://gamepad.ladnet.net/joystick.html?type=gamepad&gameId=" + web_socket_id_partie
urlWss = "wss://ws.ladnet.net?type=game&gameId=" + web_socket_id_partie
web_socket = False


fenetre = None
boucle = True

JOUEURS_WEBSOCKET = {}
DICO_NAMES_WEBSOCKET = {}

# --- joystiques
nombre_manettes = 0
dico_manettes = {}


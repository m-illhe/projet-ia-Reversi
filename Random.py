import Reversi
import random 

def randomMoove(plateau):
    list_of_moovs = plateau.legal_moves()
    return random.choice(list_of_moovs)
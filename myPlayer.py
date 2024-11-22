from Reversi import Board
from MiniMax import minimax
from AlphaBeta import alpha_beta
from Random import randomMoove
import time

class ReversiAI:
    def __init__(self, joueur, profondeur=3, algo=True, type=True):
        self.joueur = joueur
        self.profondeur = profondeur
        self.algo = algo
        self.type = type

    def choisir_coup(self, plateau):
        coups_legaux = plateau.legal_moves()

        meilleur_coup = coups_legaux[0]
        meilleure_valeur = float('-inf')

        for coup in coups_legaux:
            plateau.push(coup)
            if self.algo : 
                eval = alpha_beta(self, plateau, self.profondeur - 1, float('-inf'), float('inf'), False,float("inf"),0 )
            else :
                eval = minimax(self, plateau, self.profondeur - 1, False, float("inf"), 0)
            
            plateau.pop()
            
            if eval > meilleure_valeur:
                meilleure_valeur = eval
                meilleur_coup = coup
           
        if meilleur_coup == None :
            print("MEILLEUR COUP = NONE") 
            print(plateau)
        return meilleur_coup
    
    def choisir_coup2(self, plateau, reflexion):
        start_time2 = time.time()
        coups_legaux = plateau.legal_moves()
        meilleur_coup = coups_legaux[0]
        meilleure_valeur = float('-inf')
        
        for profondeur in range(2, 15):
            for coups in coups_legaux : 
                if time.time() - start_time2 >= reflexion:
                    #print(time.time() - start_time2)
                    #print("le temps a couper l'algo dans choisir coup 2")
                    #print(profondeur)
                    print("profondeur = ", profondeur)
                    return meilleur_coup
                else:
                    plateau.push(coups)
                    if(self.algo):
                        eval = alpha_beta(self, plateau, profondeur - 1, float('-inf'), float('inf'), False, reflexion, start_time2 )
                    else:
                        eval = minimax(self, plateau, profondeur - 1, False, reflexion, start_time2)
                    plateau.pop()
                    if eval > meilleure_valeur:
                        meilleure_valeur = eval
                        meilleur_coup = coups
                        if eval == 1000:
                            print("I will Win in few rounds")
                            return meilleur_coup
            #print(profondeur)
        return meilleur_coup


def afficherVainqueur(joueur, lvljoueur, color):
    if(joueur == 1):
        print(" Le vainqueur est Minmax a profondeur", lvljoueur, "qui joue en", color)
    elif(joueur == 2):
        print(" Le vainqueur est Minmax en temps donnés", lvljoueur, " qui joue en", color)
    elif(joueur == 3):
        print(" Le vainqueur est AlphaBeta en profondeur", lvljoueur, "qui joue en", color)
    elif(joueur == 4):
        print(" Le vainqueur est AlphaBeta en temps donnés", lvljoueur, "qui joue en", color)
    else :
        print(color, "random  WIN")     
        
              
def createGame(player1, player1lvl, player2, player2lvl):
    # Créer un plateau Reversi
    if player1 in [1,2]:
        joueur1 = ReversiAI(Board._BLACK, profondeur=player1lvl, algo=False)
    else:
        joueur1 = ReversiAI(Board._BLACK, profondeur=player1lvl, algo=True)
    
    if player2 in [3,4]:
        joueur2 = ReversiAI(Board._WHITE, profondeur=player2lvl, algo=True)
    else:
        joueur2 = ReversiAI(Board._WHITE, profondeur=player2lvl, algo=False) 
        
    start_time = time.time()
    plateau = Board(boardsize=10)

    while not plateau.is_game_over():
        if plateau._nextPlayer == Board._BLACK:
            if player1 == 5:
                coup = randomMoove(plateau)
            elif player1 in [2,4]:
                coup = joueur1.choisir_coup2(plateau, player1lvl)
            elif player1 in [1,3] :
                coup = joueur1.choisir_coup(plateau)
            else : 
                print("probleme")
            plateau.push(coup)
            print(plateau)
            
        else:
            if player2 == 5:
                coup = randomMoove(plateau)
            elif player2 in [2,4]:
                coup = joueur2.choisir_coup2(plateau, player2lvl)
            elif player2 in [1,3]:
                coup = joueur2.choisir_coup(plateau)
            else : 
                print(joueur)
                print("probleme")
            plateau.push(coup)
            print(plateau)
            
    
    white, black = plateau.get_nb_pieces()
    print (plateau)
    print("joueur 1 : ", black)
    print("joueur 2 : ", white)
    if black > white:
        afficherVainqueur(player1, player1lvl, "Black")
    elif black < white:
        afficherVainqueur(player2, player2lvl, "WHITE")
    else :
        print("DRAW")
    end_time = time.time()
    execution_time = end_time - start_time
    print("Temps d'exécution total : {:.4f} secondes".format(execution_time))
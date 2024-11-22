

def heuristique(self, player=None):
    if player is None:
        player = self._nextPlayer

    coin_weight = 25
    mobility_weight = 10
    edge_weight = 5

    nb_black = self._nbBLACK
    nb_white = self._nbWHITE

    corners = [(0, 0), (0, -1), (-1, 0), (-1, -1)]
    corner_count = sum(1 for corner in corners if self._board[corner[0]][corner[1]] == player)

    legal_moves_player = len(self.legal_moves())

    # Compter les pions sur les bords
    edge_count_player = sum(1 for i in range(self._boardsize) for j in range(self._boardsize) if i in [0, -1] or j in [0, -1] and self._board[i][j] == player)

    # Vérifier si le joueur actuel peut gagner
    if self.is_winner(player):
        return 1000  # Valeur très élevée si le joueur peut gagner

    # Calcul de l'heuristique
    heuristic_value = (nb_white - nb_black) + corner_count * coin_weight + (legal_moves_player) * mobility_weight + edge_count_player * edge_weight

    return heuristic_value



def is_winner(board, player):
        
    nb_black, nb_white = board.get_nb_pieces()

    # Si le nombre de pièces du joueur est supérieur à l'adversaire, le joueur gagne
    if player == board._BLACK and nb_black > nb_white and board.is_game_over():
        #print("je passa laaaaaaaa ")
        return True
    elif player == board._WHITE and nb_white > nb_black and board.is_game_over():
        #print("je passa la ")
        return True
    else:
        assert player == board._nextPlayer
        return False
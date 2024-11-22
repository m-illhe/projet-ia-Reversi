import time

def minimax(self, plateau, profondeur, joueur_maximise, reflexion_time, time_of_begining):
        if profondeur <= 0 or plateau.is_game_over() or (time.time() - time_of_begining >= reflexion_time):
            return plateau.heuristique(self.joueur)

        coups_legaux = plateau.legal_moves()

        if joueur_maximise:
            eval_max = float('-inf')
            for coup in coups_legaux:
                plateau.push(coup)
                eval =  minimax(self, plateau, profondeur - 1, False,  reflexion_time, time_of_begining)
                eval_max = max(eval_max, eval)
                plateau.pop()
            return eval_max
        else:
            eval_min = float('inf')
            for coup in coups_legaux:
                plateau.push(coup)
                eval = minimax(self, plateau, profondeur - 1, True, reflexion_time, time_of_begining)
                eval_min = min(eval_min, eval)
                plateau.pop()
            return eval_min
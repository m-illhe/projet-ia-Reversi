import time

def alpha_beta(self, plateau, profondeur, alpha, beta, joueur_maximise, reflexion_time, time_of_begining):
        if profondeur <= 0 or plateau.is_game_over() or (time.time() - time_of_begining >= reflexion_time) :
            return plateau.heuristique( self.joueur)

        coups_legaux = plateau.legal_moves()

        if joueur_maximise:
            eval_max = float('-inf')
            for coup in coups_legaux:
                plateau.push(coup)
                eval = alpha_beta(self, plateau, profondeur - 1, alpha, beta, False, reflexion_time, time_of_begining)
                eval_max = max(eval_max, eval)
                alpha = max(alpha, eval_max)
                plateau.pop()
                if beta <= alpha:
                    break
            return eval_max
        else:
            eval_min = float('inf')
            for coup in coups_legaux:
                plateau.push(coup)
                eval = alpha_beta(self, plateau, profondeur - 1, alpha, beta, True, reflexion_time, time_of_begining)
                eval_min = min(eval_min, eval)
                beta = min(beta, eval_min)
                plateau.pop()
                if beta <= alpha:
                    break
            return eval_min
 
# Fonction pas utilisé lors des programmes, mais m'a servis dans mes tests.       
def alpha_beta_with_time(self, plateau, profondeur, alpha, beta, joueur_maximise, reflexion_time, time_of_begining):
    #start_time3 = time.time()
        
    if profondeur <= 0 or plateau.is_game_over() or (time.time() - time_of_begining >= reflexion_time):
        return plateau.heuristique(self.joueur)

    coups_legaux = plateau.legal_moves()

    if joueur_maximise:
        eval_max = float('-inf')
        for coup in coups_legaux:
            plateau.push(coup)
            eval = self.alpha_beta_with_time(plateau, profondeur - 1, alpha, beta, False, reflexion_time, time_of_begining)
            eval_max = max(eval_max, eval)
            alpha = max(alpha, eval)
            plateau.pop()
            if beta <= alpha:
                break
        return eval_max
    else:
        eval_min = float('inf')
        for coup in coups_legaux:
            plateau.push(coup)
            eval = self.alpha_beta_with_time(plateau, profondeur - 1, alpha, beta, True, reflexion_time, time_of_begining)
            eval_min = min(eval_min, eval)
            beta = min(beta, eval)
            plateau.pop()
            if beta <= alpha:
                break
        return eval_min
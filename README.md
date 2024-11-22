# IA Reversi by Martin Illhé
Projet Intelligence Artificiel pour le Master 1 informatique de l'Université de Bordeaux

# Choix d'implémentation : 
- Création de deux fonctions "choisir_coup" qui en fonction des parametres lanceront l'algorithme voulue et renverra le meilleur coup trouvé.
- Coup aléatoire : renvoi un coup aléatoire sur les coups possibles.
- Implémentation de Minimax qui renvoi la meilleur évaluation de l'heuristique en fonction de la profondeur souhaité.
- Implémenatation d'Alphabeta qui renvoi la meilleur évaluation de l'heuristique en fonction de la profondeur souhaité.
- Implémenatation d'Alphabeta qui renvoi la meilleur évaluation de l'heuristique en un temps donnés (IAIterativeDeepening).

# Fonctionnement : 
- Une partie est une boucle while(plateau.game_is_over())
- Regarde le joueur qui doit jouer
- Le joueur appel la fonction choisir_coup(plateau) et joue le coup retourner.

# Affrontement des IA : 
- Pour se faire affronter les IA lancer la commande python3 Main.py qui vous fera choisir parmis les 5 IAs.
- En comptant le temps l'IA alphabeta en un temps données est la meilleure IA de ce projet.

# Non implémenté :
- Le joueur humain.
- Une nouvelle heuristique. Tentative d'implémentation d'un heuristic dans le fichier heuritique.py
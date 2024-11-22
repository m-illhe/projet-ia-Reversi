from myPlayer import createGame

def choixPlayer1():
    print("Choisir IA pour le joueur 1")
    print("1) Minimax en profondeur")
    print("2) MiniMax en temps donnée")
    print("3) Alphabeta en profondeur")
    print("4) Alphabeta en temps donnée")
    print("5) Random")
    rep = int(input("Joueur 1 : "))
    return rep

def choixPlayer2():
    print("Choisir IA pour le joueur 2")
    print("1) Minimax en profondeur")
    print("2) MiniMax en temps donnée")
    print("3) Alphabeta en profondeur")
    print("4) Alphabeta en temps donnée")
    print("5) Random")
    rep = int(input("Joueur 2 : "))
    return rep

def main (): 
    print("Projet IA 2023 de Martin Illhé")
    while(True):
        player1 = choixPlayer1()
        player2 = choixPlayer2()
        player1level = 0
        player2level = 0
        if player1 != 5 :
            print("Entrez le niveau de profondeur ou le temps de recherche en seconde du joueur 1")
            player1level = int(input() or player1level)
        if player2 != 5 :
            print("Entrez le niveau de profondeur ou le temps de recherche en seconde du joueur 2")
            player2level = int(input() or player1level)
        createGame(player1, player1level, player2, player2level)
main()
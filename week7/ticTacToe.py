from game import Game
from collections import namedtuple

GameState = namedtuple('GameState','to_move, utility, board, moves')

class TicTacToe(Game):
    """"""

    def __init__(self, h=3, v=3, k=3):
        self.h = h  #Sorok száma
        self.v = v  #Oszlopok száma

        #Hány egymás követő X-re/O-ra van szükség a winhez:
        self.k = k

        #A kezdőállapotból elérhető összes lehetséges mozgás
        moves = [(x,y) for x in range(1, h+1) for y in range(1, v+1)]

        #Kezdő állapot beállítása
        self.initial = GameState(to_move='X', utility=0, board={}, moves=moves)

    def actions(self, state):
        """A lehetséges lépések. Valójában minden olyan mező amit még nem foglaltak el."""
        return state.moves
    
    def result(self, state, move):
        if move not in state.moves:
            return state #Mert illegális lépést nem thetünk
        
        #Készítünk egy másolatot a táblára
        board = state.board.copy()

        #Beállítjuk az új lépést
        board[move] = state.to_move

        #Frissítsük a lehetségs lépéseket
        moves = list(state.moves)
        moves.remove(move)

        #Állítsuk elő az új állapotot
        return GameState(to_move=('O' if state.to_move == 'X' else 'X'),
                         utility=self.compute_utility(board, move, state.to_move),
                         board=board, moves=moves)
    
    
    def utility(self, state, player):
        """Visszaadja az értéket: 1, -1, 0"""
        return state.utility if player == 'X' else -state.utility
    
    def terminal_test(self, state):
        """Nincs több mozgás, !=0 val az eredmény"""
        return state.utility != 0 or len(state.moves) == 0

    def display(self, state):
        #Kérjük le a táblát
        board = state.board

        for x in range(1, self.h+1):
            for y in range(1, self.v+1):
                print(board.get((x,y), '.'), end=' ')
            print()

    def compute_utility(self, board, move, player):
        """Ha 'X' nyer ezzel a lépéssel, adjon vissza 1-et; ha 'O' akkor -1; különben 0"""
        if (self.k_in_row(board, move, player, (0,1)) or  #Oszlop
            self.k_in_row(board, move, player, (1,0)) or  #Sor
            self.k_in_row(board, move, player, (1,-1)) or #/ Átló
            self.k_in_row(board, move, player, (1,1))):   #\ Átló
            return +1 if player == 'X' else -1
        else:
            return 0
    
    def k_in_row(self, board, move, player, delta_x_y):
        """vissaad egy True értéket, ha az adott irányba a játkos kigyűjtötte a megfelelő mennyiségű értéket.""" 

        (delta_x, delta_y) = delta_x_y
        x, y = move
        n = 0 #A lehetséges lépések száma a sorban 

        while board.get((x,y)) == player:
            n += 1
            x, y = x + delta_x, y + delta_y
        x, y = move

        while board.get((x,y)) == player:
            n += 1
            x, y = x - delta_x, y - delta_y
        n -= 1 #Mert magát a mozgást kétszer számoltuk

        return n >= self.k


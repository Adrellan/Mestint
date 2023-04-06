class Game:
    """Hasonló a probléma osztályhoz"""

    def actions(self,state):
        """visszaadja a megengedett mozgások listáját."""
        raise NotImplementedError

    def result(self, state, move):
        """Visszaadja azt az állapotot, amely efy állapotból való elmozdulás eredménye."""
        raise NotImplementedError
    
    def utility(self, state, player):
        """A végső állapotnak az eredményét adja vissza a játékosoknak."""
        raise NotImplementedError
    
    def terminal_test(self, state):
        """True értéker ad vissza, ha ez a játék végső állapota."""
        return not self.actions(state)

    def to_move(self, state):
        """Adja vissza azt a játékost, akinek a lépése ebben az állapotban van."""
        return state.to_move

    def display(self, state):
        """Jelenítse meg az adott állapotot."""
        print(state)
    
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    def play_game(self, *players):
        """N-személyes játék játszás."""
        
        #Kezdő állapot
        state = self.initial

        #Amíg végső állapotba nem érünk
        while(True):
            
            #Veszünk egy játékost
            for player in players:
                #Adjon egy lépést a választott játékos
                move = player(self, state)

                #Kérjük vissza anak eredményét, hogy hogyan módosul a játék
                #játékos lépést elvégezzük
                state = self.result(state, move)
                if self.terminal_test(state):
                    #Ha a játékos lépésével előál egy végső állapot, akkor azt kiiratjuk és vissza adjuk ki nyert
                    self.display(state)
                    return self.utility(state, self.to_move(self.initial))
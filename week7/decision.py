def minmax(state, game):

    player = game.to_move(state)

    def max_value(state):
        if game.terminal_test(state):
            return game.utility(state, player)
        
        v = -np.inf


        
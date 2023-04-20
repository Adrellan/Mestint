def minmax(state, game):

    player = game.to_move(state)

    def max_value(state):
        if game.terminal_test(state):
            return game.utility(state, player)
        
        v = -np.inf

        #Visszaadjuk a minimum értékek közül a legnagyobbat
        for a in game.actions(state):
            v = max(v, min_value(game.result(state,a)))
        return v
    
    def min_value(state):
        #Ha játék végállás akkor visszaadjuk az eredményt
        if game.terminal_test(state):
            return game.utility(state, player)
        
        v = np.inf

        for a in game.actions(state):
            v = min(v, max_value(game.result(state,a)))
        return v
    
    return max(game.actions(state),
               key=lambda a: min_value(game.resul(state,a)))

def alpha_beta_search(state, game):
    player = game.to_move(state)

    def max_value(state, alpha, beta):
        if game.terminal_test(state):
            return game.utility(state, player)
        
        v = -np.inf

         #Lehetséges lépések alkalmazása
        for a in game.actions(state):
            #Max meghatározása
            v = max(v, min_value(game.result(state,a),alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v
    
    def min_value(state, alpha, beta):
        if game.terminal_test(state):
            return game.utility(state, player)
        
        v = np.inf

        #Lehetséges lépések alkalmazása
        for a in game.actions(state):
            #Max meghatározása
            v = min(v, max_value(game.result(state,a),alpha, beta))
            if v <= alpha:
                return v
            beta = max(beta, v)
        return v
    
    # Alfa béta keresés
    # Legjobb eredmény 
    best_score = -np.inf

    # Béta értéke
    beta = np.inf

    best_action = None

    for a in game.actions(state):
        v = min_value(game.result(state, a), best_score, beta)
        if v > best_score:
            best_score = v
            best_action = a
    return best_action

    


from problem import Problem

class NQueens(Problem):
    def __init__(self, N):
        super().__init__(tuple([-1]*N))
        self.N = N
    
    def actions(self,state):
        """A bal szélső üres oszlopban próbálja ki az összes nem ütköző sort."""
        if state[-1] != 1:
            return []
        else:
            col = state.index(-1)
            return [row for row in range(self.N)
                    if not self.conflicted(state, row, col)]
    
    def result(self, state, row):
        """Helyezze a következő kiráényőt a megadott sorba."""
        col = state.index(-1)
        new = list(state[:])
        new[col] = row
        return tuple(new)
    
    def conflicted(self, state, row, col):
        """Egy királynő elhelyezése (sor, oszlop) ütközik? """
        return any(self.conflict(row,col,state[c],c)
                   for c in range(col))
    
    def conflict(self, row1, col1, row2, col2):
        """Összeütközésbe kerölbe két királynő elehlyezése (sor1, oszlop1) és (sor2, oszlop2)?"""
        return (row1 == row2 or               # Ugyanabban a sorban
                col1 == col2 or               # Ugyanabban az oszlopban
                col1 - row1 == col2 - row2 or # Ugynabban az átlóban, irány: \
                col1 + row1 == col2 + row2)   # Ugynabban az átlóban, irány: /
    
    def goal_test(self, state):
        """Ellenőrizze, hogy minden oszlop megtelte-e és nincs ütközés"""
        if state[-1] == -1:
            return False
        return not any(self.conflicted(state, state[col], col)
                       for col in range(len(state)))
    
        
    
import numpy as np



from node import Node
from problem import Problem
from collections import deque


def trial_error(problem: Problem):


    state = Node(problem.initial)

    while True:
        if problem.goal_test(state.state):
            print("[+] Got it")
            return state


        # lehetésges megoldások
        successor = state.expand(problem)
        if len(successor) == 0:
            return "[-] Unsolvable!"
        state = successor[np.random.randint(0, len(successor))]
        print(state)

def hill_climbin_for_cup3(problem: Problem,heuristic):


    state = Node(problem.initial)

    while True:
        if problem.goal_test(state.state):
            print("[+] Got it")
            return state


        # lehetésges megoldások
        successor = state.expand(problem)
       
        test_successor = []
        for s_test in successor:
            if heuristic(state.state,) >= heuristic(s_test.state):
                test_successor.append(s_test)

        if len(test_successor) == 0:
            return " [-] Unsolvable"
        state = test_successor[np.random.randint(0, len(test_successor))]
        print(state)

def heuristic(State):
    if State == (4,0,1) or State == (4,1,0):
        return 0
    c = 0
    for s in State:
        if s == 0:
            c+=1
    return c

#Szélességi keresés
def breadt_first_tree_search(problem):
    # Kezdő állapot kiolvasása és FIFO sorba helyezése
    frontier = deque([Node(problem.initial)])

    # Amíg nem értük el a határt
    while frontier:
        # Legszélsőbb elem kiemelése
        node = frontier.popleft()

        # Ha cél állapotban vagyunk akkor vége
        if problem.goal_test(node.state):
            return node
        
        # A kiemelt elemből az összes új állapot legyártása az operátorok segítségével
        frontier.extend(node.expand(problem))

#Mélységi keresés
def depth_first_graph_search(problem):
    # Kezdő erem verembe helyezése
    frontier = [(Node(problem.initial))]

    # Halmaz deklarálás a már bejárt elemekhez
    explored = set()

    # Amíg tudunk mélyebbre menni
    while frontier:
        # Legfelső elem kiemelése a veremből
        node = frontier.pop()

        # Ha cél állapotban vagyunk vége
        if problem.goal_test(node.state):
            return node
        
        # Állapot feljegyzése hogy tudjuk hogy már jártunk itt
        explored.add(node.state)

        # Verem bővítése amíg benem járt elemekkel
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and child not in frontier)

def best_first_graph_search(problem, f):

    # kezdő állapot létrehozása
    node = Node(problem.initial)

    # prioritásos (vmilyen heurisztika szerint rendezett) or létrehozása
    frontier = []

    # kezdő állapot felvétele a prioritásos sorba
    frontier.append(node)

    # halmaz létrehzása a már megvizsgált elemekhez
    explored = set()

    # amíg találunk elemet
    while frontier:
        # elem kivétele a verem tetejéről
        node = frontier.pop()

        # ha cél állapotban vagyunk akkor kész
        if problem.goal_test(node.state):
            return node
        
        # feldolgozott elemek bővítése
        explored.add(node.state)

        # operátorral legártott gyermek elemek bejárása
        for child in node.expand(problem):
            # ha még nem dolgoztuk fel
            if child.state not in explored and child not in frontier:
                frontier.append(child)
        
        # rendezzük a listát (sort) a heurisztikának megfelelően
        frontier = f(frontier)
        print(node.state)



def astar_search(problem, f=None):
    """
    h*(n): az n ből valamel célcsúcsba jutás optimális költsége
    g*(n): a startcsúcsból n-be jutás optimális költsége
    f*(n):=g*(n)+h*(n): a startcsúcsból n-en keresztül valamely célcsúcsba
    """

    return best_first_graph_search(problem, f)
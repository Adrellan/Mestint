from mt_utils import *


class Fruits(Problem):

    def __init__(self):
        # Complete the implementation of initial function by calling
        # the parent constructor and initialize with the initial state
        # Write your code below this line!
        pass
        # Write your code above this line! Delete the 'pass' keyword!

    def actions(self, state):
        # Complete the implementation of possible operators.
        # The function should return all next possible actions from the input state.
        acts = []
        # Write your code below this line!

        # Write your code above this line!
        return acts

    def result(self, state, action):
        # Fill in the missing parts of the transition function. Return the new state as the result.
        i, j = action
        # Write your code below this line!

        # Write your code above this line!

    def goal_test(self, state):
        # Write a logic here to test if the state is a goal state. Return True if it is a goal state, False if not
        # Write your code below this line!
        pass
        # Write your code above this line! Delete the 'pass' keyword.


def depth_first_graph_search(problem):
    # Fill out the function to perform a Depth first graph search on a given problem
    # Write your code below this line!
    pass
    # Write your code above this line! Delete the 'pass' keyword.


def main():

    # 1. Exercise: Fill in the missing parts of init function and print out the initial state result (1 point)
    # Write your code below this line!
    pass
    # Write your code above this line! Delete the 'pass' keyword.

    # 2. Exercise: Fill out the goal_test function and test if it works correctly (1 point)
    # (test for (49, 0, 0) and (5, 6, 6))
    # Write your code below this line!

    # Write your code above this line!
    # 3. Exercise: Fill out the actions function and test if it works correctly (3 points)
    # (test using the initial state)
    # Write your code below this line!

    # Write your code above this line!
    # 4. Exercise: Fill out the result function and test if it works correctly (2 points)
    # (use the initial state and (2, 3) as the action when testing)
    # Write your code below this line!

    # Write your code above this line!
    # 5. Fill out the depth_first_graph_search function and solve the problem using it (2 points)
    # Write your code below this line!

    # Write your code above this line!


if __name__ == '__main__':
    main()


from search import *

class WolfGoatCabbage(Problem):
  
  #initial = frozenset({'F','G','W','C'})
  #goal = frozenset()
  #Problem.path_cost=0
  #goal = frozenset({})
  

  def __init__(self, initial, goal):
    #super().__init__(initial, goal)
    self.initial = initial
    self.goal = goal

  def actions(self, state):
    current_state = set(state)
   
    possible_actions = []
    if current_state == {'F','G','W','C'}:
      possible_actions=[{'F','G'}]

    elif current_state == {'W','C'}:
      possible_actions = [{'F'}]

    elif current_state == {'F','W','C'}:
      possible_actions = [{'F','C'},{'F','W'}]

    elif current_state == {'W'}:
      possible_actions = [{'F','G'}]

    elif current_state == {'C'}:
      possible_actions = [{'F','G'}]

    elif current_state == {'F','G','W'}:
      possible_actions = [{'F','W'}]

    elif current_state == {'F','G','C'}:
      possible_actions = [{'F','C'}]

    elif current_state == {'G'}:
      possible_actions = [{'F'}]

    elif current_state == {'F','G'}:
      possible_actions = [{'F','G'}]

    else:
      pass
    return possible_actions



  def result(self, state, action):
    newState = set(state)
    if newState.intersection(action):
      newState = newState - action 
    else:
      newState.update(action)
    
    newState = frozenset(newState)
    return newState

  def goal_test(self, state):
    return state == self.goal


if __name__ == '__main__':
    #istate = frozenset({'F','G','W','C'})
    #goal_state = frozenset({})
    initial = frozenset({'F','G','W','C'})
    goal =  frozenset({})
    wgc = WolfGoatCabbage(initial, goal)
    #print(wgc.actions({'F','G','W','C'}))
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
    
    exit()

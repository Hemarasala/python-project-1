
#vaccume cleaner
from locale import currency
import numpy as np

states = [[1, 0, 0, 0],
          [0, 1, 0, 0],
          [1, 0, 1, 0],
          [0, 1, 1, 0],
          [1, 0, 0, 1],
          [0, 1, 0, 1],
          [1, 0, 1, 1],
          [0, 1, 1, 1]]

goal_state = [0, 1]

tt = [[0, 1, 0],
      [0, 1, 1],
      [2, 3, 0],
      [2, 3, 3],
      [4, 5, 4],
      [4, 5, 1],
      [6, 7, 4],
      [6, 7, 3]]

duration = 5
seq_of_actions = [np.random.randint(0, 3, duration) for _ in range(11)]
print(seq_of_actions)

try:
    current_state1 = int(input("Enter the current state (0-7): "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit(1)

if current_state1 < 0 or current_state1 >= len(states):
    print("Current state out of bounds. Please enter a number between 0 and 7.")
    exit(1)

for i, seq in enumerate(seq_of_actions):
    t = 0
    path_cost = 0
    current_state = current_state1

    while t < duration:
        action = seq[t]
        if current_state < len(tt) and action < len(tt[current_state]):
            next_state = tt[currency]
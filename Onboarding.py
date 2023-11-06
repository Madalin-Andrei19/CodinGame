import sys
import math

# CodinGame planet is being attacked by slimy insectoid aliens.
# <---
# Hint:To protect the planet, you can implement the pseudo-code provided in the statement, below the player.

# game loop
while True:
    enemy1 = input()
    dist1 = int(input())

    enemy2 = input()
    dist2 = int(input())

    print(enemy1 if dist1 < dist2 else enemy2)
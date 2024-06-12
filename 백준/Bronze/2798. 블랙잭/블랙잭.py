from itertools import combinations
import sys

cards, goal = map(int, input().split())

list = sorted(list(map(sum,combinations(map(int, sys.stdin.readline().split()), 3))),reverse=True)

for i in list:
    if i <= goal:
        print(i)
        break
import sys

count = int(input())
total_score = []
run_score, trick_score = [], []

for i in range(count):
    max_trick_score = 0

    score = list(map(int,sys.stdin.readline().split()))
    max_run_score = max(score[0:2])

    trick_score = score[2:]
    for _ in range(2):
        max_trick_score += max(trick_score)
        trick_score.remove(max(trick_score))

    total_score.append(max_run_score + max_trick_score)

print(max(total_score))
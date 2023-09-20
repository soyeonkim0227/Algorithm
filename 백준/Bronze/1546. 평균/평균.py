import sys

num = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
print((sum(score) / max(score) * 100) / num)
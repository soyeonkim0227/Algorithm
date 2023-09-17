import sys

list = []
num = int(input())
for _ in range(num):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
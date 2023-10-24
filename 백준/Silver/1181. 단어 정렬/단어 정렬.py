N = int(input())
word = []

for _ in range(N):
    word.append(input())

word = set(word)
word = list(word)

word.sort()
word.sort(key=len)

for s in word:
    print(s)
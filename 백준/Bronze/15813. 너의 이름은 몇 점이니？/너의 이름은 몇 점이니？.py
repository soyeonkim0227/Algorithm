import sys

strLen = int(sys.stdin.readline())
name = sys.stdin.readline()
name = name.strip()

cnt = 0
dict = {}
english = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i, alp in enumerate(english, 1):
  dict[alp] = i

for s in name:
  cnt += dict[s]

print(cnt)
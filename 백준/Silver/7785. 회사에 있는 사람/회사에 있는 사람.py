n = int(input())
dict = {}
result = []

for _ in range(n):
  name, status = input().split()
  dict[name] = status

for key in dict:
  if dict[key] == 'enter':
    result.append(key)

result.sort(reverse=True)

for s in result:
  print(s)
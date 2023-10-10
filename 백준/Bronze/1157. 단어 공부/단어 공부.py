word = input().upper()
wordList = list(set(word))

lst = [ 0 for _ in range(len(wordList))]

for i in range(len(wordList)):
    lst[i] = word.count(wordList[i])

print('?') if lst.count(max(lst)) > 1 else print(wordList[lst.index(max(lst))])
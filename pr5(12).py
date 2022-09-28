s=input().split()
words = []
i = 0
while i < len(s) and s[i] != ':':
    word = ''
    while i < len(s) and s[i] != ';' and s[i] != ':':
        word += s[i]
        i =  i + 1
    words.append(word)
    i = i + 1
k = 0
for word in words:
    if word[len(word)-1] == 'я':
        k = k + 1
print(k)
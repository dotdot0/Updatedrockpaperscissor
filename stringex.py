word = input('Enter a word: ')

length = len(word)

#To write a word in reverse order using => for loop --- for i in range(-1, (-len(word) - 1), -1)
i = 0

for j in range(-1, (-length -1), -1):
    print(word[i], word[j])
    i += 1

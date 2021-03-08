word = input('Enter a word: ')

findword = input('Enter a word: ')

count = 0

revword = word[:: -1]

print(revword)

#Printing each letter of the word
'''for i in range(0, len(word)):
    print(word[i])
    print('-----')'''

#Printing the word in reverse order

'''for i in range(len(word), 1, -1):
    print(word[i : 1: -1])
    print('*****')'''

for i in range(0, len(word)):
    if word[i] == findword:
        count += 1


print('The word has repeated ', count, ' times')
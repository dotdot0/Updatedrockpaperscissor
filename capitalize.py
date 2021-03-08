line = input('Enter a line: ')
newLine = ''
a = 0
while a < len(line):
    if a == 0:
        newLine += line[a].upper()
    
    if line[a] == '' and line[a + 1] != '':
        newLine += line[a]
        newLine += line[a + 1].upper()

    newLine += line[a]

    a += 1

print(newLine)

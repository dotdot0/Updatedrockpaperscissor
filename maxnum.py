#Program to find the maximum and minmium number in a list
lis = list(input('Enter the number you want in your list: '))
max = lis[0]
min = lis[0]

for i in lis:
    if (i > max):
        max = i

    if (i < min):
        min = i

print(max)
print(min)
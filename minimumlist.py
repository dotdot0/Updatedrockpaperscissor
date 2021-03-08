lis = eval(input('Enter the numbers: '))

min = lis[0]

for i in lis:
    if min > i:
        min = i

print(min)
print(lis.index(min))
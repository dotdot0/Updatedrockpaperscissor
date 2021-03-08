num = int(input('Enter a number: '))
n1 = 1
n2 = 1
nth = 0
for i in range(0, num):
    if (n1 == 1 and n2 == 1):
        print(n1, end=' ')
    nth = (n1 * n2 + nth)
    n2 = n1
    n2 = nth
    print(nth, end= ' ')
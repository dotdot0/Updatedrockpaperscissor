N = int(input('Enter the number upto which you want fibonacci: '))
n1 = 0
n2 = 1
nth = 0
for i in range(0, N+1):
    if nth == 0:
        print(nth, end= ' ')

    nth = n1 + n2
    print(nth, end=' ')
    n1 = n2
    n2 = nth
    

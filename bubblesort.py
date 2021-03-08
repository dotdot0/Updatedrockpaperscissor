size = int(input('Enter the size of the list: '))
a = []
for i in range(0, size):
    element = int(input('Enter the elements of the list: '))
    a.append(element)

#Bubble Sort Algorithm => Remember
for i in range(size):#Max no. of steps to sort the list is equal to the no. of elements of the list
    for j in range(size - i - 1):
        if a[j] > a[j + 1]:
            t = a[j]
            a[j] = a[j + 1]
            a[j + 1] = t

print(a)

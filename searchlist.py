print('Enter the elements in the sequence [el1, el2, el3]')
lis = eval(input('Enter the elements: '))

item = eval(input('Enter the item you want to search for: '))

for i in lis:
    if i == item:
        print('The item is found at ', lis.index(i))
        break

else:
    print('The element is not found in the list')

    


#017-555-1212
number = input('Enter the number')
valid = True

if(len(number) != 12):
    valid = False

if (number[3] == '-' or number[7] == '-'):
    valid = False

for i in range(0, 12):
    if(i == 3 or i == 7):
        continue
    
    if (number[i].isdigit()):
        valid = True


print(valid)
    

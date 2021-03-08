password = input('Enter your password: ')

valid = True

if (not(password[0].isdigit())):
    valid = False

elif (not(len(password) >= 6)):
    valid = False

if(valid == True):
    print('Password is accepted.')

else:
    print('Password is not a valid one')

while True:
	option = int(input('Press 1 to get ordinal value or 2 for character: '))

	if option == 1:
		ch = input('Enter a character:')
		print(ord(ch))

	elif option == 2:
		orde = int(input('Enter a valid ordinal number: '))
		print(chr(orde))

	else:
		print('Please enter valid option')
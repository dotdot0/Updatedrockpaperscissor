num = int(input('Enter a number: '))
for i in range(2, num):
	if num % i == 0:
		print('This is not a prime number')
		break

else:
	print('It is a prime number')
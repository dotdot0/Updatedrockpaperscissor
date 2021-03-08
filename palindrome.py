#To get the reverse of a string we use A[::-1] => It simply start from last and will print the digits in reverse

#Palindrome => 'ABCBA' == 'ABCBA'

str1 = input('Enter a word: ')
str2 = str1[::-1]
if str1 == str2:
    print('Its a palindrome')

else:
    print('It is not a palindrome')
a = input('Enter a string: ')
u = l = a1 = d = 0

for i in range(0, len(a)):
    if a[i].isupper():
        u += 1

    if a[i].islower():
        l += 1

    if a[i].isalpha():
        a1 += 1

    if a[i].isdigit():
        d += 1

print(u, l, a1, d)
# 3(b) WAP in python to print pyramid pattern.

n = 5
alph = 65
for i in range(0, n):
    print(" " * (n-i), end=" ")
    for j in range(0, i+1):
        print(chr(alph), end=" ")
        alph += 1
    alph = 65
    print()


# 3(b) WAP in python to print right angle triangle.
for i in range(6):
   print('*' * i)
   
# 1(a) WAP in python to add elements of list.

n=int(input("Enter the total length of list:"))
list1=[]

for i in range(n):
    num=float(input("Enter a number:"))
    list1.append(num)
print(list1)

sum=0
for i in list1:
    sum+=i
print("Sum of elements of list = :", sum)


# 1(b)Write a Python program to multiply all the items.

n=int(input("Enter the total length of list:"))
list1=[]

for i in range(n):
    num=float(input("Enter a number:"))
    list1.append(num)
print(list1)

product=1
for i in list1:
    product*=i
print("Multiplication of elements of list = :", product)


# 1(c) Write a Python program to get the largest number from a list.

input_string = input("Enter numbers separated by spaces: ")
numbers = [float(num) for num in input_string.split()]

if len(numbers) == 0:
    print("The list is empty.")
else:
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number

    print("The largest number in the list is:", largest)


# 1(d) Write a Python program to get the smallest number from a list.

input_string = input("Enter numbers separated by spaces: ")
numbers = [float(num) for num in input_string.split()]

if len(numbers) == 0:
    print("The list is empty.")
else:
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number

    print("The smallest number in the list is:", smallest)
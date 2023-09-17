# Python program to interchange first and last elements in a list.

#def elements(list):
#    get = list[-1], list[0]
#    list[0], list[-1] = get
#    return list
#newList = [12, 35, 9, 56, 24]
#print(elements(newList))

# Python program to find smallest number in a list.

#a = [12, 35, 9, 56, 24]
#print("Smallest element is:", min(a))

# Write a python program to print even numbers in a list.

#a =  [12, 35, 9, 56, 24, 10]
#for num in a:
#    if num % 2 == 0:
#        print(num, end=" ")

# Write a python program to print odd numbers in a list.

#a = [12, 35, 9, 56, 24, 10]
#for num in a:
#    if num % 2 != 0:
#        print(num, end=" ")

# Write a python program to print positive numbers in a list.

#a = [-10, 21, -4, -45, -66, 93]
#num = 0
#while (num < len(a)):
#    if a[num] >= 0:
#        print(a[num], end=" ")
#    num += 1

# Write a python program to print negative numbers in a list.

#a = [-10, 21, -4, -45, -66, 93]
#for num in a:
#    if num < 0:
#        print(num, end=" ")

# Write a python program to covert Fahrenheit to Celsius.

#fahrenheit = float(input("Enter temperature in fahrenheit: "))
#celsius = (fahrenheit - 32)/1.8
#print(str(fahrenheit )+ " degree Fahrenheit is equal to " + str(celsius ) + " degree Celsius." )

# Write a python program to print maximum and minimum number in a tuple.

#a = [2, 3, 4, 16, 9, 18, 10, 9]
#max_a=a[0]
#min_a=a[0]
#for i in a:
#    if i>max_a:
#        max_a=i
#    elif i<min_a:
#        min_a
#print("Maximum number is:",max_a)
#print("Minimum number is:",min_a)

# Write a python program to convert a list into a tuple.

#def convert(list):
#    return tuple(i for i in list)
#list = [1, 2, 3, 4]
#print(convert(list))

# Write a python program to create a list and use the following functions- append() and extend(), len()

#a = ['I', 'Love', 'Kozhikode']
#print(a)
#a.append('Kannur')
#print(a)
#b = ['10, 20, 30']
#a.extend(b)
#print(a)
#print("length of list is:",len(a))
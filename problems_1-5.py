from functools import reduce 

# Problem 1: Sum of Digits
# Objective: Write a Python program that uses a lambda function 
# to compute the sum of the digits of a given number.
num = 1234
digits = [int(i) for i in str(num)]
s = lambda x,y: x + y
sum_digits = reduce(s,digits)
print('Problem 1:', sum_digits)

# Problem 2: Custom Sort Order
# Objective: Given a list of strings, use a lambda function to 
# sort the list in ascending order based on the length of the 
# strings. In case of a tie, sort the strings alphabetically.
lst = ['dog', 'puppy', 'doggo','woof']
sorted_lst = sorted(lst, key=lambda s: (len(s), s))
print('Problem 2:' , sorted_lst)

# Problem 3: Find Maximum
# Objective: Implement a function that takes a list of numbers 
# and a lambda function as arguments. The lambda function should 
# compare two numbers and return the greater of the two. Use this 
# lambda function to find the maximum number in the list without 
# using the built-in max() function.
numbers = [22,75,11,9,100]
compare = lambda x,y: x if x > y else y
maximum = reduce(compare, numbers)
print('Problem 3:', maximum)

# Problem 4: Intersection of Two Lists
# Objective: Write a Python program that finds the intersection of 
# two lists using a lambda function and the filter() function. The 
# program should return a list of elements that are present in both 
# lists.
list_1 = [1,3,5,7,9]
list_2 = [2,3,4,5,6,8]
intersection = list(filter(lambda x: x in list_1, list_2))
print('Problem 4:', intersection)

# Problem 5: Exponential Mapping
# Objective: Given a list of numbers and a constant value n, use 
# a lambda function with map() to raise each number in the list to 
# the power of n.
num_list = [2,3,4]
n = 2
power = list(map(lambda x: x ** n, num_list))
print('Problem 5:', power)
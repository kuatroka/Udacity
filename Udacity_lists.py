# Given the variable,
"""
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.


def how_many_days(month_number):

    return days_in_month[month_number - 1]


print how_many_days(1)
#>>> 31

print how_many_days(9)
#>>> 30

# append lists

p = [1, 2]
q = [3, 4]
p.append(q)
print p

s = 0.4 * 1000000000
sp = s * 299792458
print sp

#-------------
# while loop on lists

def print_all_elements(p):
    j = 0
    while j < len(p):
        print p[j]
        j += 1

p = ['q', 'w', 'e', 'r']

print_all_elements(p)

# for loop in lists


def print_all_elements2(q):
    for e in q:
        print e

q = [1, 2, 3, [4, 5], [6, 7, 8]]

print_all_elements2(q)


# summing with for loop

def sum_list(p):
    summ = 0
    for i in p:
        summ += i

    return summ

p = [1, 7, 4]
print sum_list(p)

# Measure Udacity


def measure_udacity(list1):
    result = 0
    for i in list1:
        if i[0] == 'U':
            result += 1
    return result


list1 = ['Dave', 'Sebastian', 'Katy']
list1 = ['Umika','Umberto']
print measure_udacity(list1)
"""

# Find element 'b' in a list 'a'. Return the index of the list 'a' where the 'b' is found. If nothing is found then \
# return -1
# with while loop
"""
def find_element(a, b):
    index = 0
    while index < len(a):
        if a[index] == b:
            return index
        index += 1

    return -1


#a = ['tr', 'yu', 'op']
#b = 'yu'
a = ['rt', 'yu', 'jk']
b = 'yu'
print find_element(a, b)



# with for loop
def find_element1(a, b):
    index = 0
    for element in a:
        if element == b:
            return index
        index += 1

    return -1

a = [1, 2, 3]
b = 3
print find_element1(a, b)
"""

# find element in with 'in' and index()
def find_element(a, b):
    if b in a:
        return a.index(b)
    return -1


a = ['rt', 'yu', 'jk']
b = 'yu'

print find_element(a, b)


# with 'not in'

def find_element1(a, b):
    if b not in a:
        return -1
    return a.index(b)

a = ['rt', 'yu', 'jk']
b = 'y'

print find_element1(a, b)

# calculates the product of elements in a list
def product_list(list_of_numbers):
    prod = 1
    for i in list_of_numbers:
        prod *= i

    return prod

print product_list([1,2,3,4])

# the greatest number in a list
def greatest(list_of_numbers):
    while list_of_numbers:
        return max(list_of_numbers)
    return 0


print greatest([4, 23, 1])





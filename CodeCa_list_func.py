""" Iterations with :range()" and for loop
two methods:
1.
for item in list:
    print item

2.
for i in range(len(list)):
    print list[i]

In the 1st method it's impossible to modify the list, but in the 2nd it is.
"""


# With numbers

n = [3, 5, 7]


def total(numbers):
    result = 0
    for i in range(len(numbers)):
        result += numbers[i]
    return result


print total(n)

# With strings

n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for item in words:
        result += item
    return result


print join_strings(n)


# list of lists in a function

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here


def flatten(lists):
    results = []
    for numbers in lists:
        for number in numbers:
            results.append(number)
    return results


print flatten(n)
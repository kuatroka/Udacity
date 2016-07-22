# lists and for loops

ls1 = ["e", "t", "y", "b", "r", "u"]


def sample(any_list):
    res = []
    for i in ls1:
        res.append(i + "tu-")
    return res

print sample(ls1)

# ---------------------

letters = ['a', 'b', 'c', 'd']
print " ".join(letters)
print "---".join(letters)

# -----------

word = "Marble"
for char in word:
    print char,
print ''

#---
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

print is_even(6)


# this one sums up all the digits from which the argument consists of. The parameter is int, not string.


def digit_sum(n):
    result = 0
    for i in str(n):
        result += int(i)
    return result


n = 1234
print digit_sum(n)


# Factorial ###############


def factorial(x):
    result = 1
    print range(1, x + 1)
    for i in range(1, x + 1):

        result *= i

    return result

x = 4
print factorial(x)


#


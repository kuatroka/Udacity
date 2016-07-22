"""
def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x == 0 or x == 1 or x < 0:
        return False
    else:
        print range(3, x)
        for n in range(3, x):
            print x, '%', n, 'mod = ', x % n

            if x % n == 0 or x % 2 == 0:
                print 'nor prime'
                return False

        return True

print is_prime(4)
"""


def is_prime(x):
    if x < 2:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
    return True


print is_prime(7)
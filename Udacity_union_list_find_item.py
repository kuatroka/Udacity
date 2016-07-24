# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no
# repeated elements
# To test, uncomment all lines
# below except those beginning with >>>.

def union(a, b):
    for i in b:
        if i not in a:
            a.append(i)
    return a



a = [1,2,3,4]
b = [2,4,6,7,7,8,8,9,10]
union(a,b)
print a
#>>> [1,2,3,4,6]
print b
#>>> [2,4,6]

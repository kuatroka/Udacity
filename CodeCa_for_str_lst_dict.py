phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
    if char == 'A' or char == 'a':
        char = 'X'
        print char,
    else:
        print char,

# Don't delete this print statement!
print

numbers = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
    print num
print "---"
# Add your loop below!
for num in numbers:
    print num ** 2


d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code her
    print key + " " + d[key]


#----------------
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index + 1, item

#----------------

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Add your code here!
    print max(a, b)

#---------------
# for else

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    print 'A', f
    if f == 'tomato':
        print 'A tomato is not a fruit!'  # (It actually is.)

else:
    print 'A fine selection of fruits!'


#-------
for i in 'Tennis':
    print i,
else:
    print 'What a game!'

print 'Now printing a bit lower'

# cfreates an empty list and fills it with hobbies based on user inputs
hobbies = []

# Add your code below!
"""
for i in range(3):
    hobby = raw_input("What is your hobby?")
    hobbies.append(hobby)

print hobbies
"""

# counter with for loop in a list and an object needed to be counted

def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count

# remove certain elements from list. Important point - if iterate from left to right, not all the elements will be
# found and removed. When removing or deleting elements from the list we need to go backwards, from right to left.

def purify(list):
    for n in range(len(list), 0, -1):  # here we loop from the end of the list, but we put it as start
                                       #  - len(list), then we indicate the end - 0 and afterwards indicate the step "-1"
                                       # so it goes backward in decrementing steps.
            if list[n - 1] % 2 != 0:
                list.remove(list[n - 1])
    return list


print purify([4, 5, 5, 4])

# removing duplicates from a list
list = [4, 5, 5, 4]


def remove_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print remove_duplicates([4, 5, 5, 4])

# median

list = [1,1,2]
def median(list):
    list = sorted(list)
    if len(list) % 2 == 0:
        return (list[(len(list) / 2) - 1] + list[(len(list) / 2)]) / 2.0
    return list[(len(list) / 2)]

print median(list)






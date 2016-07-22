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

numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
    print num

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

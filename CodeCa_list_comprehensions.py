evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50


####
new_list = [x for x in range(1,6)]
print new_list

### creates numbers from 1 to 5 and each number multiplied by 2 and then checkes if it can be evenly devised by 4
doubles_by_3 = [x*2 for x in range(1,6) if (x*2)%3 == 0]
print doubles_by_3

# creates a list of even squares
even_squares = [x**2 for x in range(1,11) if x % 2 == 0]

print even_squares

###
c = ['C' for x in range(5) if x < 3]
print c

####
cubes_by_four = [ x**3 for x in range(1, 11) if (x**3) % 4 == 0]
print cubes_by_four

# slicing
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print l
print l[2:9:2]

####
to_five = ['A', 'B', 'C', 'D', 'E']
print to_five[0::2]

### prints every odd number from start to beginning of the list
my_list = range(1, 11) # List of numbers 1 - 10
print my_list[::2]

# every even number in the list
print my_list[1::2]


###
threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]
print threes_and_fives





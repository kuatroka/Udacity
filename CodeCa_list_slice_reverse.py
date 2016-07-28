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

# reversing

letters = ['A', 'B', 'C', 'D', 'E']
print letters[::-1]

my_list = range(1, 11)

backwards = my_list[::-1]
print backwards

# backwards by strides of 10
to_one_hundred = range(101)
# Add your code below!
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

####
to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[7:14]

print to_21
print odds
print middle_third

###
str = "ABCDEFGHIJ"
start, end, stride = 1, 6, 2
print str[start:end:stride]
print str

###
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[:0:-1]
print message
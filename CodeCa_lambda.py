def by_three(x):
    return x % 3 == 0

print by_three(1)

##
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

## this lambda filters out everything except "Python"
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)

## creates list of squares and filter through lambda on those that are out of 30 to 70 window
squares = [x**2 for x in range(1,11)]
print filter(lambda x: x >= 30 and x <= 70, squares)

###
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda x: x != "X", garbled)
print message
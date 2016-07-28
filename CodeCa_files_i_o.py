# writing to the file

my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "r+")

# Add your code below!
for i in my_list:
    my_file.write(str(i) + "\n")

my_file.close()

# Reading from file

my_file = open("output.txt", "r")
print my_file.read()
my_file.close()


# reading lines
my_file = open("text.txt","r")

print my_file.readline()
print my_file.readline()
print my_file.readline()

my_file.close()

# creating file open command different way so I don't need to add close() after working with files all the time

with open("text.txt", "w") as textfile:
	textfile.write("Success!")

with open("text.txt", "r") as textfile:
	textfile.read()

# checking if file is closed and if not, closing it

with open("text.txt", "w") as my_file:
    my_file.write("tu ru ru")
if not my_file.closed:
    my_file.close()

print my_file.closed



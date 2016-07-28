d = {
    "Name": "Guido",
    "Age": 56,
    "BDFL": True
}
#print d.items()
#print d

#-----
my_dict = {
    01: "Blue",
    02: "Red",
    03: "Yellow",
    04: "White Stripes"
}
print my_dict.items()
print my_dict.keys()
print my_dict.values()

for number in range(5):
    print number,

d = { "name": "Eric", "age": 26, "gender": "male" }
for key in d:
    print key, d[key],



for letter in "Eric":
    print letter,
    print "-----"

# iterating through list's key and values. one point that codecademy says is that dictionaries show tuples in no
# particular order
my_dict = {
    01: "Blue",
    02: "Red",
    03: "Yellow",
    04: "White Stripes"
}

for key in my_dict:
    print key, my_dict[key]
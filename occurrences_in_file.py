# count occurrences of all words in file. It count exact, individual word... 'fuck' and 'fucking' are different words as
# well as 'Fuck'

from collections import Counter;
cnt = Counter();

for line in open('zed2.txt', 'r'):
    for word in line.split():
        cnt[word] += 1

print cnt['fucking']
# print cnt - to print all the stats of al the words and corresponding occurrences


# printing file into Python console and counting number of occurrences of a certain term in a file


def main():
    my_file = open('zed2.txt', 'r').read()
    print my_file
    term = raw_input("Enter team name: ")
    count = my_file.count(term)
    count_c = my_file.count(term.capitalize())

    print count + count_c

main()
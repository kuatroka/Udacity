choice = raw_input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")


count = 0

while True:
    print count
    count += 2
    if count >= 20:
        break



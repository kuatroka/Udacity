

def split_line(text, word):
    new = ''
    lenght_term = len(term)
    new_term = '*' * lenght_term
    # split the text
    text = text.split()
    #print text

    # for each word in the line:
    for item in text:
        if item == word:
            item = new_term
            #print item
            new += (new_term + " ")

        else:
            new += (item + " ")
    return new[:len(new) - 1]


text = "hey hey hey"
term = "hey"

print split_line(text, term)
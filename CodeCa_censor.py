

def censor(text, word):
    new = ''
    lenght_term = len(term)
    new_term = '*' * lenght_term
    # split the text
    text = text.split()
    print text

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

print censor(text, term)


# another version that passed on codecademy portal. it uses 'replace' function
def censor(text, word):
    word_old = word
    for letter in word:
        word = word.replace(letter, '*')
    while word_old in text:
        if word_old in text:
            text = text.replace(word_old, word)

    return text


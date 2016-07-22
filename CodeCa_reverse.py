def reverse(x):
    n = len(x)
    for i in range(0, n):
        letter = x[n - 1]
        print letter
        n -= 1


x = 'Python!'
reverse(x)

# another way to reverse - much shorter

def reverse(x):
    print x[::-1]
    print reversed(x)


x = 'Python!'
reverse(x)

# anti vowel - removing vowels from string and printing only consonants


def anti_vowel(text):
    no_vowel = ''
    for i in text:
        if i not in 'aeiouAEIOU':
            no_vowel += i
    return no_vowel

text = "Hey look Words!"

print anti_vowel(text)


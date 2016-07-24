def find_last(string, search_term):

    last_pos = -1
    while True:
        pos = string.find(search_term, last_pos + 1)
        if pos == -1:
            return last_pos
        last_pos = pos

print find_last('rtdrrdrtdd', 'd')


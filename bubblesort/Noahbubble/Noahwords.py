def split(word):
    return list(word)

def switch(list):
    change_count = 0
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            saved_char = list[i]
            list[i] = list[i + 1]
            list[i + 1] = saved_char
            change_count += 1
    return list, change_count

def alphabetize(word):
    list = (split(word.lower()))
    change_count = 1
    while change_count > 0:
        list, change_count = switch(list)
    return (list)

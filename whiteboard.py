# Write a function that takes in a string of one or more words,
#  and returns the same string, 
# but with all five or more letter words reversed.
#  Strings passed in will consist of only letters and spaces.
#  Spaces will be included only when more than one word is present.


def solution(string):
    str_lst = string.split()
    reverse_lst = []
    for word in str_lst:
        if len(word) >= 5:
            reverse_lst.append(word[::-1])
        else:
            reverse_lst.append(word)
    
    return ' '.join(reverse_lst)


def solution(string):
    return ' '.join([word[::-1] if len(word) >= 5 else word for word in string.split()])
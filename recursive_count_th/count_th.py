'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # Base case, 2 character word cannot work
    if len(word) < 2:
        return 0
    # If the first 2 letters are "th"
    elif word[0:2] == "th":
        # Recursive call of count_th 
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])
    

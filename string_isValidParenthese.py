def isValid (input):
    """
    input: string input
    return: boolean
    """
    # write your solution here
    par = []
    i = 0
    pair = {')': '(', ']': '[', '}': '{'}
    while i < len(input):
        if input[i] in pair:
            if not par or par[-1] != pair[input[i]]: return False
            par.pop()
        else:
            par.append(input[i])
        i += 1
    return True

isValid("[]")
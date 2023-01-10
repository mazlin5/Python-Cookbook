# Given string and array return the matching letters

s = 'abcdeccf'
arr = ['c', 'a', 'b', 'g', 'f']
csv = "a, b, c, c, d, g, b,f"

def matchLetters(s, arr, csv):
    # Write your code here.
    # store visited somewhere
    visted = []
    final = ''
    
    for letter in s:
        for item in arr:
            if letter == item:
                visted.append(letter)

    for rest in csv:
        if rest in visted:
            visted.append(rest)

    for values in visted:
        if values in final:
            pass
        else:
            final += values


    return final
    # return -1

print(matchLetters(s, arr, csv))
 
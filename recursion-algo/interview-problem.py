# Problem 1
# Write a recursive function that takes an int and computes the cumulative sum of 0 to that int

# for example, if n ==4, return 4+3+2+1+0 which is 10

def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

# print(sum(4))


# Problem 2 
# Given an int, create func that return sum of all individual digits in that int
# for example, if n = 4321, return 4+3+2+1


def sum2(n):
    if len(str(n)) == 1:
        return n
    return n%10 + sum2(n/10)

# print(sum2(4321))

# Problem 3
# create function that takes string and set list of words
# determine if words from list of wrods can make the word
# using only list of words

# phrase = "ilovedogs"
# list_of_words = ['dog','me','love']

# def wordFind(phrase, list_of_words, output = None):
#     index = 0
#     if output is None:
#         output = []

#     for word in list_of_words:
#         if phrase[index] == len(list_of_words):
#             output.append(word)
#             # recursivley call func on remaining phrase
#             return wordFind( phrase[len(word):], list_of_words, output)
#     return output


# Recursive Python3 program to find if a given pattern is
# present in a text

text = "ilovedogs"
pat = ['dog','me','love']

def exactMatch(text, pat, text_index, pat_index):
    # if you reach end of text and not end of words index then no match
	if text_index == len(text) and pat_index != len(pat):
		return False

	# Else If last character of pattern reaches
	if pat_index == len(pat):
		return True

    # if values match at each index then you have a match - incremental 
	if text[text_index] == pat[pat_index]:
		return exactMatch(text, pat, text_index+1, pat_index+1)

	return False


# This function returns true if 'text' contain 'pat'
def contains(text, pat, text_index, pat_index):
	# If last character of text reaches
	if text_index == len(text):
		return False

	# If current characters of pat and text match
	if text[text_index] == pat[pat_index]:
		if exactMatch(text, pat, text_index, pat_index):
			return True
		else:
			return contains(text, pat, text_index+1, pat_index)

	# If current characters of pat and tex don't match
	return contains(text , pat, text_index+1, pat_index)

# Driver program to test the above function

print(contains("ethbtcltc", "eth", 0, 0))
print(contains("malikiscool", "coolm", 0, 0))
print(contains("bullshitforonce", "shit", 0, 0))



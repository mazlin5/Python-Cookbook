friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]

def findItem(n):

    for i in range(len(friends)):
        if n == friends[i]:
            return friends[i]

print(findItem("Zoe"))

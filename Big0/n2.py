# O(n^2) - less efficient 
# n * n items printed - n^3
# simplifys to O(n^2)

# drop non-dominants
def print_items(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                print(i,j)

print_items(3)
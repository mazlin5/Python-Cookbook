# def reverseArray(a):
    # Write your code here
    # [1, 2, 3 4] 0-3
    # emptyList = []
    
   
# print(reverseArray(a)) #expect [2, 5, 4, 3, 1]

# [1, 2, 3, 4, 5] 
# def reverse(array):
#     for i in range(0, int(len(array)/2)):
#         other = len(array) -i - 1
#         temp = array[i]
#         array[i] = array[other]
#         array[other] = temp
#     print(array)

a = [1, 2, 3, 4, 5, 6, 7, 8]
# reverse(a)
# print(int(len(a)/2))

for i in range(0,int(len(a)/2)): # 8/2 = 4 -> [0,1,2]
    other = len(a) -i -1
    # print(other) # 8-0-1 = 7 -> 8-1-1 = 6 -> 8-2-1 = 5 -> 8-3-1 = 4
    temp = a[i] #index values for half the list
    a[i] = a[other]
    a[other] = temp
print(a)


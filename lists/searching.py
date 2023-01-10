# Searching for an element in the List
myList = [10,20,30,40,50,60,70,80,90]

if 20 in myList:
    print(myList.index(20))  # o(n)
else:
    print('Value does not exist')

# linear search
def search(list, value):
    for i in list:
        if i == value:
            return list.index(value)

print(search(myList,20))


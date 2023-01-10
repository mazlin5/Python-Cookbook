# always start with second item in list 
# compare to item before and drop into correct index
# worst o(n^2)
# sorted data = o(n)

my_list = [24,2,16,95,11,53]

def insertSort(my_list):

    # range of list - start at second value
    for i in range(1, len(my_list)):
        
        # var to hold second item in list
        start = my_list[i]
        # compare to item before it
        j = i -1
        while start < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = start
            # compare values until j is < start
            j -= 1

    print(my_list)

m = insertSort(my_list)

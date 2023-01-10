# need indexes for selection sort
# look at first item where min[index] min_index = 0
# compare: is this [n] < or > then [n+1]
# for loop to check next index and compare values if it is replace the index position 
# use counter to start at next index and continue through 

my_list = [3,5,1,7,9,19, 11, 8, 20, 90, 4, 100, 106, 89, 17]

def selectSort(my_list):

    # range of list - 1
    for i in range(len(my_list) - 1):
        min_index = i
        # comparing everything after min_index, go to end value
        for j in range(i+1, len(my_list)):
            
            # if j is > you want to switch indexes
            # compare first to second value
            if my_list[min_index] > my_list[j]:
                min_index = j
        if i != min_index:
             # temp = first item
            temp = my_list[i]
            # if first item is greater.. move to next index
            my_list[i] = my_list[min_index]
            # move next index to prev index
            my_list[min_index] = temp

    print(my_list)

m = selectSort(my_list)



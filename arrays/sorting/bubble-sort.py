# o(n) w/ n-1 comparisons

my_list = [4,2,6,5,1,3]

def bubbleSort(my_list):

    # range of list - 1 to give 5 then go to 0 and decrement(-1) each time
    for i in range(len(my_list) - 1, 0, -1):

        # move forward through list - runs 4 times
        for j in range(i):

            # if j is > you want to switch indexes
            # compare first to second value
            if my_list[j] > my_list[j+1]:

                # temp = first item
                temp = my_list[j]
                # if first item is greater.. move to next index
                my_list[j] = my_list[j+1]
                # move next index to prev index
                my_list[j+1] = temp

    print(my_list)

m = bubbleSort(my_list)


# create head and set to nested set dictionaries

# How to traverse?
# start at head then 'next' then 'next' again then 'value'
head = {
            "value": 11,
            "next": {
                    "value": 3,
                    "next": {
                            "value": 23,
                            "next": {
                                    "value": 7,
                                    "next": None
                            }
                    }
            }
}

print(head['next']['next']['value'])

# will only run with linked list
print(linked_list.head.next.next.value)

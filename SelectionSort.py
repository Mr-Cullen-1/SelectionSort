llist = [29, 10, 14, 37, 13]

def selection_sort(unsorted_list):
    sorted_list = []
    while unsorted_list:
        max_val = unsorted_list[0]
        for item in unsorted_list:
            if item > max_val:
                max_val = item
    
        sorted_list.append(max_val)
        unsorted_list.remove(max_val)
    return sorted_list

print(selection_sort(llist))
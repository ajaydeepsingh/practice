def bubble_sort(a_list):
    
    if len(a_list) == 0:
        return []
    
    for i in range(len(a_list)):
        for j in range(0,len(a_list)-i-1):
            if (a_list[j] > a_list[j+1]):
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]

    return a_list

# driver code

print(bubble_sort([5, 4, 3]))
def smaller_indices(list1, list2):
    new_list = []
    for i in range(len(list1)):
        if list1[i] < list2[i]:
            new_list.append(i)
    return new_list

list1 = [40, 50, 10, 90, 100, 70]
list2 = [60, 20, 19, 95, 30, 20]
result = smaller_indices(list1, list2)
print(result)

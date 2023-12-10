def pairwise_product(list1, list2):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i] * list2[i])
    return new_list

# Example usage:
list1 = [40, 50, 10, 90]
list2 = [6, 2, 2, 5]
result = pairwise_product(list1, list2)
print(result)

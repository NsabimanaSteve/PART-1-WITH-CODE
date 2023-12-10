def min_index(numbers):
    if not numbers:
        return None
    return numbers.index(min(numbers))
list_num=["m"]
result=min_index(list_num)
print(result)
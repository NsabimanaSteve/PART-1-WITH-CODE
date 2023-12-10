def max_index(numbers):
    if not numbers:
        return None
    return numbers.index(max(numbers))
list_num=[40, 50, 10, 90, 100, 70]
result=max_index(list_num)
print(result)
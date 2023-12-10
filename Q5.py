def pairwise_ratio(list1,list2):
    new_list=[]
    for i in range(len(list1)):
        new_list.append(list1[i]/list2[i])
    return new_list
list1=[40, 50, 10, 90] 
list2=[60, 20, 19, 95]
result=pairwise_ratio(list1,list2)
print(result)
def partition_list(list,pivot):
    less_than=[x for x in list if x<pivot]
    equal_than=[x for x in list if x==pivot]
    greater_than=[x for x in list if x>pivot]
    return less_than+equal_than+greater_than
    




list=[3,1,4,1,5,9,2,6,5]
p_v=4
print("partitioned list:",partition_list(list,p_v))
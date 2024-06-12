origin_tuple=(1,2,3,4,5)
filtered_tuple=tuple(filter(lambda x:x%2==0,origin_tuple))
print("filtered value",filtered_tuple)
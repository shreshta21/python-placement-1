my_tuple=(1,2,3)
another_tuple=tuple([4,5,6])
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:3])
combined_tuple=my_tuple+ another_tuple
print(combined_tuple)
repeated_tuple=my_tuple*3
print(repeated_tuple)
print(2 in my_tuple)
print(4 not in my_tuple)
print(len(my_tuple))
for item in my_tuple:
    print(item)
string_to_tuple=tuple("helllo")
print(string_to_tuple)
list_to_tuple=tuple([1,2,3])
print(list_to_tuple)
print(my_tuple.count(2))
print(my_tuple.index(3))


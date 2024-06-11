tuple_of_tuples=((1,'apple'),(3,'orange'),(2,'banana'))
sorted_tuples=sorted(tuple_of_tuples,key=lambda x:x[1])
print("sorted tuple:",sorted_tuples)


#tuple comprehension
square_tuple=tuple(x**2 for x in range(1,6))
print("squares tuple:",square_tuple)

#ziping
l1=[1,2,3]
l2=['a','b','c']

zipped_tuple=tuple(zip(l1,l2))
print("zipped tuple:",zipped_tuple)
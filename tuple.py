def create_tuples():
    tuple1=(1,2,3,4,5)
    tuple2=('a','b','c','d','e')
    tuple3=("apple","banana","cherry")
    
    return tuple1,tuple2,tuple3

def access_tuple_items(tuple1,tuple2):
    print("Tuple1:",tuple1)
    print("First elment of tuple 1:",tuple1[0])
    print("Last element of tuple 1:",tuple1[-1])
    print("Tuple 2:",tuple2)
    print("second element of tuple 2:",tuple2[1])
    print("second element of tuple 2:",tuple2[-2])
    print(tuple[0:5])
    
def unpacking_tuple1(tuple3):
    (green,yellow,red)=tuple3
    print(green)
    print(yellow)
    print(red)
    
def unpacking_tuple2(fruits):
    fruits=("apple","banana","cherry","strawberry","raspberry")
    
    (green,yellow,*red)=fruits
    print(green)
    print(yellow)
    print(red)
    
def change_tuples(tuple1,tuple2):
    list1=list(tuple1)
    list2=list(tuple2)
    list1.append(6)
    list2.remove('c')
    tuple1=tuple(list1)
    tuple2=tuple(list2)
    return tuple1,tuple2

def loop_through_tuple(tuple1):
    print("looping through tuple 1 using for loop:")
    for item in tuple1:
        print(item)
        
    print("\n looping using while loop and index numbers:")
    index=0
    while index<len(tuple1):
        print(tuple[index])
        index+=1



tuple1,tuple2,tuple3=create_tuples()
access_tuple_items(tuple1,tuple2)
print()

unpacking_tuple1(tuple3)
print()

fruits=("apple","banana","cherry","strawberry","raspberry")
unpacking_tuple2(fruits)
print()

tuple1,tuple2=change_tuples(tuple1,tuple2)
print("after making changes:")
access_tuple_items(tuple1,tuple2)
print()

tupl
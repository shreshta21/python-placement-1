set={"apple","banana","cherry"}
set.add("orange")
print(set)


set1={"apple","banana","cherry"}
tropical={"pineapple","mango","papaya"}
set1.update(tropical)
print(set1)

#join list
set1={"apple","banana","cherry"}
list=["kiwi","papaya"]
set1.update(list)
print(set1)

set1={"apple","banana","cherry"}
set1.remove("apple")
print(set1)

set1={"apple","banana","cherry"}
set1.discard("apple")
print(set1)


set1={"apple","banana","cherry"}
x=set1.pop()
print(x)
print(set1)

set1={"apple","banana","cherry"}
set1.clear()
print(set1)

set1={"apple","banana","cherry"}
del set1
print(set1)
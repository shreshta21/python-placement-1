set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)


set1={"a","b","c"}
set2={1,2,3}
set3=set1|set2
print(set3)

set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set3=set1.intersection(set2)
print(set3)

set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set3=set1&set2
print(set3)

set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set1.intersection_update(set2)
print(set1)

set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set1.difference_update(set2)
print(set1)

set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set1.symmetric_difference(set2)
print(set1)
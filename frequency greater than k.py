li=[8,9,8,9,8,8,5,4,5,5]
k=2
newlist=[]
for i in li:
    freq=li.count(i)
    if(freq>2)and(i not in newlist):
        newlist.append(i)
print(newlist)

   
li=[10,20,30,40,40,33,50,40,33]
un=[]
count=0
for i in li:
    if i not in un:
        count+=1
        un.append(i)
print(count)    
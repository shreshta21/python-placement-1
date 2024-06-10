def swap(list,pos1,pos2):
    temp=list[pos1]
    list[pos1]=list[pos2]
    list[pos2]=temp
    return list
list=[23,56,17,78,2]
pos1,pos2=1,3
print(swap(list,pos1-1,pos2-1))

#sum and average

list=[23,56,17,78,2]
summ=0
for i in list:
    summ=summ+i
avg=summ/len(list)

print("sum=",summ)
print("average=",avg)
print(list[0])
print(list[len(list)-1])
    
    
#min and max in list

li=[23,56,17,78,2]
li.sort()
print(li[0])
print(li[-1])   
list=[4,5,6,7,3,9]
i,j=3,10
res=True
for x in list:
    if x<i or x>j :
        res=False
        break
print("does list contain all element in range"  + str(res))
        
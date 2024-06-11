def peak(lst):
    if not lst:
        return None
    l,r=0,len(lst)-1
    while(l<r):
        mid=l+(r-l)//2
        if(lst[mid]<lst[mid+1]):
            l=mid+1
        else:
            r=mid
    return lst[l]

lst=[1,1,2,3,5,6,4]
lst.sort()    #binary search has to be done in sorted list array hence it should be sorted before excuting
print("peak element :",peak(lst))
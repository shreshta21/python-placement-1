def binary(a,tar,l,r):
    if l>r:
        return -1
    mid=(l+r)//2
    
    if a[mid]==tar:
        return mid
    elif a[mid]<tar:
        return binary(a,tar,mid+1,r)
    else:
        return binary(a,tar,l,mid-1)
    
a=[1,2,3,4,5,6,7,8,9]
tar=5
result=binary(a,tar,0,len(a)-1)
    
if result!=1:
    print(f"element found at index {result}")
else:
     print("element not found in the array")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
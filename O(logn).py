#binary search
def binary(a,key):
    l=0
    r=len(a)-1
    while l<=r:
        mid=l+(r-l)//2
        if(a[mid]==key):
            return(mid)
        elif(a[mid]<key):
            l=mid+1
        else:
            r=mid-1
    return -1
    
a=[10,30,20,40,50,60]
key=20
result=binary(a,key)
print(result)
if(result!=-1):
    print(f"element found at index {result}")
else:
     print("element not found in the array")


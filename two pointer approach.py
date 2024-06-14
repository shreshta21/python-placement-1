def sum(a,n,x):
    a.sort()
    l=0
    r=n-1
    while l<r:
        if(a[l]+a[r]==x):
            return True
        elif(a[l]+a[r]>x):
            r=r-1
        elif(a[l]+a[r]<x):
            l=l+1
    return 0

a=[1,-1,1,0,5]
x=0
n=len(a)
if(sum(a,n,x)):
    print("True")
else:
    print("False")
    

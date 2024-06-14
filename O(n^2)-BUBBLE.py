def bubble(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
a=[8,3,3,1,7,3,7,9,4,2]
bubble(a)
print("sorted array:",a)
                

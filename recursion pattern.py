def print_pattern(n,m):
    if n==0:
        return
    for i in range(5,m-1,-1):
        print(i,end=" ")
    print()
    print_pattern(n-1,m+1)

n=5
print_pattern(n,1)
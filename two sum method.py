array=[1,-1,2,4,8]
x=int(input())
n=len(array)
def sum(array,x,n):
    for i in range(0,n):
        for j  in range(1,n):
            if(array[i]+array[j]==x)and (i!=j):
                return True

            return False
            
print(sum(array,x,n))
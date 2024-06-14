#def pow(N,P):
#   if P==0:
#        return 1
 #   return(N*pow(N,P-1))

#N=5
#P=3
#print(pow(N,P))

#time complexity
def pow(N,P):
    if(P==1):
        return N
    temp=pow(N,P/2)
    return temp*temp
N=2
P=4

print(int(pow(N,P)))

def power(N,P):
    if(P==1):
        return N
    temp=pow(N,P/2)
if(P%2!=0):
    return N*temp*temp
else:
   return temp*temp
N=2
P=5

print(int(power(N,P)))
def d_prod(res):
    prod=1
    for x in res:
        prod*=x
    return prod
        

li=[1,2,3,4,4,3,5,4,3]
res=[]
[res.append(x) for x in li if x not in res ]
product=d_prod(res)

print(d_prod(res))   
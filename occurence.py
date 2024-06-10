def cout_occc(li,x):
    count=0
    for i in li:
        if(i==x):
            count=count+1
    return count
li=[10,20,30,40,40,33,50,40]
x=40
print(cout_occc(li,x))
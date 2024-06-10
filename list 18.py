#write a program to swwap thr first and the last element in the list

def swap(list):
    size=len(list)
    temp=list[0]
    list[0]=list[size-1]
    list[size-1]=temp
    return list
list=[23,56,17,78,2]
print(swap(list))

#linear search

def linear(a,tar):
    for i in range(len(a)):
        if a[i]==tar:
            return i
        
    return -1

a=[3,4,2,5,7,6]
tar=6

result=linear(a,tar)

if result!=1:
    print(f"element is found at index {result}")
    
else:
    print("element not found in the array")
        
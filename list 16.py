#sorted based on how close a number is to 50
#customized sort
def fun(n):
    return abs(n-50)
list=[100,50,65,82,23]
list.sort(key=fun)
print(list)
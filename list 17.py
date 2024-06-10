#case sensitive
list=["banana","Orange","Kiwi","cherry"]
list.sort()
print(list)

list=["banana","Orange","Kiwi","cherry"]
list.sort(key=str.lower)
print(list)

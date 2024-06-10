
fruits=["apple","banana","cherry","kiwi","mango"]
#without using comprehension
#for x in fruits:
    #if "a" in x:
       # newlist.append(x)
       
       #using comprehension
newlist=[x for x in fruits if "a" in x]        
print(newlist)
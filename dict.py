thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}

thisdict2=dict(name="John",age=36,country="Norway")
print(thisdict2)

#creating an empty dictionary
my_dict={}

#adding key values to the dictionary
my_dict['name']='Alice'
my_dict['age']=30
my_dict['city']='New York'
print(my_dict)

print("Name:",my_dict['name'])
print("Age:",my_dict['age'])
x=my_dict.keys()
print(x)
y=my_dict.values()
print(y)
z=my_dict.items()
print(z)
m=my_dict.get("city")
print(m)

#for loop
for x in my_dict:
    print(x)
for x in my_dict:
    print(my_dict[x])
    
#iterating over keys

print("keys:")
for key in my_dict.keys():
    print(key)
    
 
#iterating over Values   
print("Values:")
for value in my_dict.values():
    print(value)
    
##iterating over key-Values pairss  
print("Key-value Pairs:")
for key,value in my_dict.items():
    print(key,":",value)
    
#checking if key exists   
if 'name' in my_dict:
    print("'name' exists in the dictionary")
else:
    print("'name' does not exists in the dictionary")
    
#modifying   
my_dict['age']=35
print("Modified Age:",my_dict['age'])

my_dict.update({"age":45})

#adding to dictionary
my_dict["color1"]="fair"
print(my_dict)
my_dict.update({"color2":"dark"})

#removing key-value pair
removed_value=my_dict.pop('city')
print(removed_value)
print(my_dict)

my_dict.popitem()
print(my_dict)

my_dict.clear()
print("Dictionary after clearing:",my_dict)

del my_dict
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


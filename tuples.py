#Adding values to tuples

#Tuples have to be converted to lists to add values, since they are unchangeable.
# They can be converted back to tuples afterwards
# For example:
colours= ("red", "yellow", "green")
x= list(colours) #converting to a list
x.append("blue") #adding a value
colours= tuple(x)#converting back to a tuple
print(colours)
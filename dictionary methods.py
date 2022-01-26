#dictionary methods
d= {"tree":"green", "sky":"blue", "sand":"brown"}
x= d.copy() #copy values in a dictionary
print(x)
x = d.items()#returns dictionary's key value pairs
print(x)
x=d.get("tree")#returns value of specified key
print(x)
x=d.keys()#returns dictionary's keys
print(x)
x=d.pop("sand")#removes an element from the dictionary
print(d)
x=d.popitem()#removes last inserted key pair
print(x)
x=d.setdefault("sky","purple")#returns value of specified key
print(x)
d.update({"clouds" : "white"})#add new elements to the dictionary
print(d)
x=d.values()#returns values
print(x)
x= d.clear()#clear dictionary
print(d)
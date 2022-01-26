#set methods
s= {1,2,3,5,7,11,13,17,19,23,29}
t= {2,4,6,8,10,12,14,16}
s.add(31) #adding an element to the set
print(s)
s.copy()#copy of the set
print(s)
#calculating difference between 2 sets
x= s.difference(t)
print(x)
s.difference_update(t)#removes items that exist in both sets
print(s)
s.discard(1)#removing an element from a set
print(s)
s.intersection(t)#intersection
print(s)
x=s.isdisjoint(t)#disjoint sets
print(x)
x=s.issubset(t)#subsets
print(x)
x=s.issuperset(t)#superset
print(x)
s.pop()#removes an element from a set
print(s)
s.remove(31) #removes specified element
print(s)
x=s.symmetric_difference(t) #combines elements from both sets
print(x)
x=s.symmetric_difference_update(t) #inserts symmetric difference
print(x)
x=s.union(t)#union of 2 sets
print(x)
x=s.update(t)#updating 2 sets
print(x)
s.clear()#clearing a set
t.clear()
print(s,t)

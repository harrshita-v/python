
# Program to make a simple calculator

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("1.Add")
print("2.subract")
print("3.Multiply")
print("4.divide")

a= float(input("Enter operation [1/2/3/4]: "))
x= float(input("Enter the first number:"))
y= float(input("Enter the second number:"))
if a==1:
        print(x,'+', y, '=', add(x,y))
elif a==2:
        print(x,'-', y, '=', sub(x,y))
elif a==3:
        print(x,'*', y, '=', multiply(x,y))
elif a==4:
        print(x,'/', y, '=', divide(x,y))




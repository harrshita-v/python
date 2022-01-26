#strings
x= "All that glitters is not gold"
y= x.capitalize()#Capitalize first letter of the string
print(y)
y= x.casefold()#Convert the string to lowercase
print(y)
y=x.center(150)#Center align the string
print(y)
y= x.encode()#Encodes the string
print(y)
y=x.endswith("e")#checking if string ends with the stated value
print(y)
y=x.find("t")#lists the number of times a character is present in a string
print(y)
y= x.index("gold")#index value
print(y)
y=x.isalnum()#Checking if all characters are alphanumeric
print(y)
y=x.isalpha()#Checking if all characters are alphabets
print(y)
y=x.isascii()#Checking if all characters are ascii characters
print(y)
y=x.isdecimal()#checking if all characters are decimals
print(y)
y=x.isdigit()#checking if all characters are decimals
print(y)
y=x.isidentifier()#checking if string is an identifier
print(y)
y=x.islower()#checking if all characters are in lower case
print(y)
y=x.isnumeric()#checking if all characters are numeric
print(y)
y=x.isprintable()#checking if all characters are printable
print(y)
y=x.isspace()#Checking if all characters have whitespaces
print(y)
y=x.istitle()#Checking if all functions follow rule of title
print(y)
y=x.isupper()#checking if the string is in uppercase
print(y)
y=x.lower()#Converting to lowercase
print(y)
y=x.swapcase()#Swapping upper and lower case
print(y)
y=x.title()#converting First letter of each letter into caps
print(y)
y=x.strip()#Calculating trimmed values
print(y)
y= x.startswith("z")#Checking if a string starts with a vertain value
print(y)
y=x.splitlines()#Splitting the string
print(y)
y=x.split("glitters")#Splitting a string based on the character specified
print(y)
y=x.partition("is")#splitting a string into 3
print(y)
y= x.replace("gold", "silver")#replace a set of characters with another
print(y)
y= x.rfind("not")#Finding a character in a string
print(y)
y=x.rindex("that")#Finding the index number of a character
print(y)
y= "#".join(x)#Adding special characters to a string at regular intervals
print(y)
y = x.ljust(20)#Left justified version
print(x, "is a good quote.")
y=x.lstrip()#centre justified version
print("Of all quotes,",y, "is my favourite")
y = x.maketrans("d", "f")#translation
print(x.translate(y))
y= x.rstrip()#right justified version
print("As a wise man once said",x)
y= x.zfill(1)#Add a specific number of zeros at the start of the string
print(y)
y=x.upper()# converting to uppercase
print(y)


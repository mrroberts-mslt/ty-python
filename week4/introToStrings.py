#How do we add a space between the strings?
string1 = "Hello"
string2 = "world"
string3 = string1 + string2 
print(string3)

#ans
string1 = "Hello"
string2 = "world"
string3 = string1 + " " + string2 
print(string3)

#multiplying a string
string1 = "Hello"
string2 = string1 * 3
print(string2)

#UpperCase
string1 = "Hello"
string2 = string1.upper()
print(string2)

#LowerCase
string1 = "Hello"
string2 = string1.lower()
print(string2)

#Length of String - why is the answer 16 and not 14?
string1 = "I like Elephants"
string2 = len(string1)
print(string2)


#Concatenation Why is there an error??
name = "Alan"
age = 31
output = "Hello " + name + "you are" + age + "years old."
print(output)

#ans wrap age in a str() to make it a str
name = "Alan"
age = 31
output = "Hello " + name + "you are" + str(age) + "years old."
print(output)

#Formatting Method
name = "Alan"
age = 31
output = "Hello {0} you are {1} years old".format(name,  age)
print(output)


#Types
name = "Ben Zeno"
type(name)
print(type(name))
age = 44
print("You are", name, "and you are " + str(age), "years old" )
#Math
password = "re3456"

print(len(password))
if len(password) < 8:
    print("Your password is too short")

text = """
Python is easy to learn.
Python is powerful.
Many people love python.
"""
print(text.count("Python"))
#Transformations
price = "1234,56"
print(price.replace(",","."))

phonenumber = "+49 (176) 123-4567"
print(phonenumber.replace("+","00").replace(" ","").replace("-","").replace("(","").replace(")",""))
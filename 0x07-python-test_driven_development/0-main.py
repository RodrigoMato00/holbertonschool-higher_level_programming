#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(4232, -324))
print(add_integer(8.4, 5))
print(add_integer(14, 4))
#print(add_integer(4, "Rodrigo"))
#print(add_integer("casa", 1234))
#print(add_integer("", ""))
print(add_integer(2*3, 4/2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

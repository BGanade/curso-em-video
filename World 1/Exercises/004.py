# Write a program that reads something from the keyboard and displays its primitive type and all possible information about it on the screen.
value = input("Type something: ")

print(f"The primitive type of this value is: {type(value)}")
print(f"Is it only spaces? {value.isspace()}")
print(f"Is it numeric? {value.isnumeric()}")
print(f"Is it alphabetic? {value.isalpha()}")
print(f"Is it alphanumeric? {value.isalnum()}")
print(f"Is it uppercase? {value.isupper()}")
print(f"Is it lowercase? {value.islower()}")
print(f"Is it capitalized? {value.istitle()}")

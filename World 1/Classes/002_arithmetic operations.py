first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))

sum = first_number + second_number
sub = first_number - second_number
mult = first_number * second_number
div = first_number / second_number
pow = first_number ** second_number
int_div = first_number // second_number
rem_div = first_number % second_number

print(f"The sum of {first_number} and {second_number} is {sum}")
print(f"The subtraction of {first_number} and {second_number} is {sub}")
print(f"The multiplication of {first_number} and {second_number} is {mult}")
print(f"The division of {first_number} and {second_number} is {div:.2f}")
print(f"The exponentiation of {first_number} and {second_number} is {pow}")
print(
    f"The integer division of {first_number} and {second_number} is {int_div}")
print(f"The remainder of {first_number} and {second_number} is {rem_div}")

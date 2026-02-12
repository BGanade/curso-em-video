first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))

sum_result = first_number + second_number
sub_result = first_number - second_number
mult_result = first_number * second_number
div_result = first_number / second_number
pow_result = first_number ** second_number
int_div_result = first_number // second_number
rem_div_result = first_number % second_number

print(f"The sum of {first_number} and {second_number} is {sum_result}")
print(
    f"The subtraction between {first_number} and {second_number} is {sub_result}")
print(
    f"The multiplication of {first_number} and {second_number} is {mult_result}")
print(
    f"The division of {first_number} and {second_number} is {div_result:.2f}")
print(
    f"The exponentiation of {first_number} and {second_number} is {pow_result}")
print(
    f"The integer division of {first_number} and {second_number} is {int_div_result}")
print(
    f"The remainder of {first_number} and {second_number} is {rem_div_result}")

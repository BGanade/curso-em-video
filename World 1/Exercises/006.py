# Create an algorithm that reads a number and displays its double, triple, and square root.
number = float(
    input('Write a number to show its double, triple and square root: '))
double = number * 2
triple = number * 3
square_root = number ** 0.5
print(
    f"The number is {number}, the double is {double}, the triple is {triple} and the square root is {square_root:.2f}")

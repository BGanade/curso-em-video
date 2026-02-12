# Write a program that reads an integer and displays its successor and predecessor on the scren
int_number = int(
    input('Enter a integer number to show it successor and predecessor: '))
successor = int_number + 1
predecessor = int_number - 1
print(
    f"For the number {int_number} the predecessor is {predecessor} and the successor is {successor}")

n = int(input("Enter the number of odd numbers to print: "))
odd_numbers = []  # Create an empty list to store odd numbers

i = 1
while len(odd_numbers) < n:  # Continue until we have 'n' odd numbers
    if i % 2 != 0:  # Check if the number is odd
        odd_numbers.append(i)  # Add odd number to the list
    i += 1

odd_numbers.sort(reverse=True)  # Sort the odd numbers in descending order

print("First", n, "odd numbers in descending order are:")
for num in odd_numbers:
    print(num, end=" ")

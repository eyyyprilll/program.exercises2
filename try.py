def process_numbers(input_file):
    # Open the source text file for reading
    with open(input_file, "r") as file:
        numbers = file.read().split()
    # Convert the strings to integers
    numbers = [int(num) for num in numbers]
    # Separate even and odd numbers
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    # Compute square of even numbers and cube of odd numbers
    squares = [num ** 2 for num in even_numbers]
    cubes = [num ** 3 for num in odd_numbers]
    # Write squares to double.txt
    with open("double.txt", "w") as double_file:
        for num in squares:
            double_file.write(str(num) + "\n")
    # Write cubes to triple.txt
    with open("triple.txt", "w") as triple_file:
        for num in cubes:
            triple_file.write(str(num) + "\n")
# Sample usage
process_numbers("integers.txt")

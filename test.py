### just creating a sample program file.

def add_numbers(input_file, output_file):
    # Open the input file for reading
    with open(input_file, 'r') as f:
        # Read the numbers from the input file
        numbers = f.readline().strip().split()
        
        # Convert the numbers from strings to integers
        num1 = int(numbers[0])
        num2 = int(numbers[1])

    # Perform addition
    result = num1 + num2

    # Open the output file for writing
    with open(output_file, 'w') as f:
        # Write the result to the output file
        f.write(str(result))

# File paths
input_file_path = 'input.txt'
output_file_path = 'output.txt'

# Perform addition and write result to output file
add_numbers(input_file_path, output_file_path)
print("Addition completed! Check 'output.txt' for the result.")

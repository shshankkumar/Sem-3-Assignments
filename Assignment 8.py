input_file = "input.txt"
output_file = "output.txt"

# Read the input file
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Count the total number of lines
line_count = len(lines)
print(f"Total number of lines: {line_count}")

# Extract the first two lines
first_two_lines = lines[:2]

# Write the extracted lines to a new file
with open(output_file, "w", encoding="utf-8") as file:
    file.writelines(first_two_lines)

print(f"First {len(first_two_lines)} line(s) written to '{output_file}'.")

''' 
(input.txt)
Rahul
Priya
Aman
Sneha
Karan

Output
Total number of lines: 5
First 2 line(s) written to 'output.txt'.
output.txt
Rahul
Priya   '''
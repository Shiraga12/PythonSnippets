# Define the patterns for each digit using LEDs
digits = [
    ["###", "# #", "# #", "# #", "###"],
    ["  #", "  #", "  #", "  #", "  #"],
    ["###", "  #", "###", "#  ", "###"],
    ["###", "  #", "###", "  #", "###"],
    ["# #", "# #", "###", "  #", "  #"],
    ["###", "#  ", "###", "  #", "###"],
    ["###", "#  ", "###", "# #", "###"],
    ["###", "  #", "  #", "  #", "  #"],
    ["###", "# #", "###", "# #", "###"],
    ["###", "# #", "###", "  #", "###"]
]

def display_number(number):
    lines = [""] * 5  # Initialize empty lines for each row
    
    # Convert the number to a list of digits
    digits_list = [int(digit) for digit in str(number)]
    
    # Build each line of the display by concatenating the LED patterns
    for digit in digits_list:
        for i, line in enumerate(digits[digit]):
            lines[i] += line + " "
    
    # Print the final display
    for line in lines:
        print(line)

# Get user input for the number to display
user_input = input("Enter a non-negative integer: ")

# Check if the input is a valid non-negative integer
if user_input.isdigit():
    number_to_display = int(user_input)
    display_number(number_to_display)
else:
    print("Invalid input. Please enter a non-negative integer.")

def input_integer_within_range(prompt, low_limit, high_limit):
    while True:
        try:
            user_input = input(prompt)
            value = int(user_input)

            if low_limit <= value <= high_limit:
                return value
            else:
                print(f"Error: the value is not within permitted range ({low_limit}..{high_limit})")
        except ValueError:
            print("Error: wrong input")

# Test the function
result = input_integer_within_range("Enter a number from -10 to 10: ", -10, 10)
print(f"The number is: {result}")

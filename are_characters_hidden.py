def are_characters_hidden(word, combination):
    current_position = 0

    # Iterate through each character in the word
    for char in word:
        # Find the position of the current character in the combination string
        position = combination.find(char, current_position)

        # If the character is not found, return "No"
        if position == -1:
            return "No"

        # Update the current position for the next iteration
        current_position = position + 1

    # If all characters are found, return "Yes"
    return "Yes"

# Test cases
print(are_characters_hidden("donor", "Nabucodonosor"))
print(are_characters_hidden("donut", "Nabucodonosor"))

def decode(message_file):
    # Read the contents of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Initialize an empty list to store the chosen words with their numbers
    chosen_words = []

    # Iterate over the lines in the file
    for line in lines:
        number, word = line.strip().split(' ')
        # Convert number to integer
        number = int(number)
        # Append the word with its number to the chosen_words list
        chosen_words.append((number, word))

    # Sort the chosen_words list based on the numbers
    chosen_words.sort(key=lambda x: x[0])

    # Determine the number of rows in the pyramid
    num_rows = int((-1 + (1 + 8 * len(chosen_words)) ** 0.5) / 2)

    # Print only the words on the right side of the pyramid
    current_index = 0
    for i in range(num_rows):
        number, word = chosen_words[current_index + i * (i + 1) // 2 + i]
        print(word, end=' ')

# Test the function with the provided file
decode('coding_qual_input.txt')

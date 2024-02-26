def replace_words(input_file, word_to_replace, replacement_word):
    try:
        with open(input_file, 'r') as file:
            data = file.read()

        modified_data = data.replace(word_to_replace, replacement_word)

        with open(input_file, 'w') as file:
            file.write(modified_data)

        print("Replacement successful. Modified data saved to", input_file)

    except FileNotFoundError:
        print("Error: Input file not found.")

    except PermissionError:
        print("Error: Permission denied to access the file.")
        
    except Exception as e:
        print("An error occurred:", str(e))


def main():
    print("Welcome to the Text Replacement Program!")
    print("----------------------------------------")

    input_file = input("Enter the path of the input file: ")
    word_to_replace = input("Enter the word to replace: ")
    replacement_word = input("Enter the replacement word: ")

    replace_words(input_file, word_to_replace, replacement_word)


if __name__ == "__main__":
    main()
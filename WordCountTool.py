def analyze_text(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("File not found.")
        return
    word_count = len(text.split())
    line_count = text.count('\n') + 1
    char_count = len(text)

    words = text.split()
    word_freq = {}
    for word in words:
        word = word.strip(".,!?;:\"'()[]")
        word_freq[word] = word_freq.get(word, 0) + 1

    print("Analysis Results:")
    print(f"Number of words: {word_count}")
    print(f"Number of lines: {line_count}")
    print(f"Number of characters: {char_count}")
    print("\nWord Frequency Analysis:")
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"'{word}': {freq} times")

def main():
    file_path = input("Enter the path to the text file: ")
    analyze_text(file_path)
if __name__ == "__main__":
    main()
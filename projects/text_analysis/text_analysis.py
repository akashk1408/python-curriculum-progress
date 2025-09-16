def text_analysis():
    text = input("Enter a sentence: ")
    words = text.split()
    print("Word Count:", len(words))
    print("Character Count:", len(text))
    print("Unique Words:", len(set(words)))

if __name__ == "__main__":
    text_analysis()

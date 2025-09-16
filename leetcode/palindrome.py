def palindrome():
    s = input("Enter a word: ")
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")

if __name__ == "__main__":
    palindrome()

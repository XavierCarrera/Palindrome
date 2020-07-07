def run():
    word = str(input("Hi, I'm the palindrome guesser. Write a word: ")).replace(' ', '').lower()
    if word[::] == word[::-1]:
        print("It's palindrome")
    else:
        print("It's not a palindrome")


if __name__ == '__main__':
    run()
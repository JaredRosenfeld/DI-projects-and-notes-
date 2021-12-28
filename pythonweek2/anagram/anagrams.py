from Anagramchecker import AnagramChecker

def menu():
        user_choice = input("Main menu: \n"
                            "(y) Anagram checker \n"
                            "(x) Exit: ")
        return user_choice
def main():
    while True:
        choice = menu()
        if choice == "y":
            user_word = input("Please enter a word: ")
            results = AnagramChecker.get_anagrams(user_word)
            if len(results) == 1:
                print(f"There are no anagrams for {user_word} in the list")
            else:
                results_str = ', '.join(results)
                print(f"The anagrams for {user_word} are: {results_str}")
        elif choice == "x":
            print("Good bye")
            break
        else:
            print("Please enter in a valid input")
main()

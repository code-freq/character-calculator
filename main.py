from tkinter import filedialog

# FUNCTIONS

# Count each character and print them in sorted way.
def count_characters(txt, print_opt = True) -> dict:
    # count the characters
    char_dict = {}
    for char in txt:
        if char == " ":
            char = "space"
        elif char == "\n":
            char = "new line"
        if char in char_dict.keys():
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    # sort and print the dict
    sorted_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    if print_opt:
        print("----------- Numbers of Characters -----------")
        [print(i,"-",k) for i, k in sorted_dict.items()]
        print()
    return sorted_dict

# Count the spaces
def count_spaces(txt) -> None:
    counter = 0
    for char in txt:
        if char == " ":
            counter += 1
    print(f"{counter} many spaces found in the text.")

# Count words
def count_words(txt) -> None:
    # read char by char and count the connected letters
    word_list = []
    words_dict = {}
    for char in txt:
        if char.isalpha():
            word_list.append(char)
        else:
            if word_list:
                word = "".join(word_list)
                if word in words_dict.keys():
                    words_dict[word] += 1
                else:
                    words_dict[word] = 1
                word_list.clear()

    # sort and print the dict
    sorted_dict = dict(sorted(words_dict.items(), key=lambda item: item[1], reverse=True))
    [print(i, "-", k) for i, k in sorted_dict.items()]
    print()

# Count chosen letters
def count_chosen_letters(txt) -> None:
    letters = None
    # get letters from user, error handle loop
    print("Enter letters you want to choose ",end="")
    while True:
        selected_letters = input("(e.g. a,b,c,d,k,f): ")
        # check if all elements are alphabetic and have 1 length, separated by commas
        if all([len(i) == 1 and i.isalpha() for i in selected_letters.replace(" ","").split(",")]):
            letters = selected_letters.replace(" ","").split(",")
            break
        else:
            print("Invalid input")
            continue

    # get all character dict
    all_chars_dict = count_characters(txt, print_opt=False)

    # get and print selected letters among all characters in sorted way
    sorted_dict = dict(sorted(all_chars_dict.items(), key=lambda item: item[1], reverse=True))
    [print(i,"-",k) for i,k in sorted_dict.items() if i in letters]
    print()

# Get user preference and input text, error handle loop
def get_text() -> str:
    print("Would you like to type now, or load a .txt file? ", end="")
    while True:
        type_or_load = input("(type/load): ")
        # Get user input and return if 'type' selected
        if type_or_load.lower() == "type":
            txt = input("Your text: ")
            return txt
        # Get selected file with filedialog, read and return if 'load' selected
        elif type_or_load.lower() == "load":
            file_path = filedialog.askopenfilename(
                title="Select a .txt file",
                filetypes=[("Text files", "*.txt")]
            )
            # Read file if a file selected
            if file_path:
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        txt = file.read()
                        return txt
                except FileNotFoundError:
                    print("File not found. Please check the path and try again.")
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                print("No file selected.")
        else:
            print("Invalid input")
            continue


# MAIN

print("---------------- Simple Character Calculator ----------------")

text = get_text()

print("Count Characters (1)\n"
      "Count Spaces (2)\n"
      "Count Words (3)\n"
      "Count Chosen Letters (4)\n"
      "Type/Load New Text (5)\n"
      "Exit Application (exit)\n")

# Main program
while True:
    process_choice = input("Choose Process: ")
    if process_choice == "exit":
        print("Exiting the application..")
        break
    elif process_choice == "1":
        count_characters(text)
        continue
    elif process_choice == "2":
        count_spaces(text)
        continue
    elif process_choice == "3":
        count_words(text)
        continue
    elif process_choice == "4":
        count_chosen_letters(text)
        continue
    elif process_choice == "5":
        text = get_text()
        continue
    else:
        print("Invalid input")
        continue

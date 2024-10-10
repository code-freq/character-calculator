from tkinter import filedialog
import pyperclip


# FUNCTIONS

# Count each character and print them in sorted way.
def count_characters(txt: str, print_opt: bool = True) -> (dict, float):
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

    # Count total letters
    counter = 0
    for num in sorted_dict.values():
        counter += num

    if print_opt:
        print()
        [print(i,"-",k,f"| Freq: {round(k * 100 / counter, 2)}%") for i, k in sorted_dict.items()]
        print(f"Total {counter} characters found.")
        print()
        print("(Numbers of Characters)\n")
    return sorted_dict, counter

# Count the spaces
def count_spaces(txt: str) -> (str,int):
    counter = 0
    for char in txt:
        if char == " ":
            counter += 1
    result_ = f"{counter} many spaces found in the text."

    # Count total words
    counter2 = 0
    char_dict, tot = count_characters(txt, print_opt=False)
    for num in char_dict.values():
        counter2 += num

    print()
    print(result_)
    percent_ = round(100 * counter / counter2, 2)
    print(f"Space Freq: {percent_}%")
    print("\n(Numbers of Spaces)\n")
    return result_, percent_

# Count words
def count_words(txt: str) -> (dict, int):
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

    # Count total words
    counter = 0
    for num in sorted_dict.values():
        counter += num

    print()
    [print(i, "-", k, f"| Freq: {round(k * 100 / counter, 2)}%") for i, k in sorted_dict.items()]
    print()
    print("(Numbers of Words)\n")
    return sorted_dict, counter

# Count chosen letters
def count_chosen_letters(txt: str) -> (dict, int, int):
    letters = None
    all_opt = False
    # get letters from user, error handle loop
    print("Enter letters you want to choose ",end="")
    while True:
        selected_letters = input("(e.g. a,b,c,d,k,f): ")
        # check if all elements are alphabetic and have 1 length, separated by commas
        if all([len(i) == 1 and i.isalpha() for i in selected_letters.replace(" ","").split(",")]):
            letters = selected_letters.replace(" ","").split(",")
            break
        elif selected_letters.strip().lower() == "all":
            all_opt = True
        else:
            print("Invalid input")
            continue

    # get all character dict
    all_chars_dict, tot = count_characters(txt, print_opt=False)

    # get and print selected letters among all characters in sorted way
    sorted_dict = dict(sorted(all_chars_dict.items(), key=lambda item: item[1], reverse=True))

    # Filter letters or not
    filtered_dict = {}
    if all_opt:
        filtered_dict = sorted_dict
    else:
        [filtered_dict.update({j: m}) for j, m in sorted_dict.items() if j in letters]

    # Count total chosen letters
    counter = 0
    for num in filtered_dict.values():
        counter += num

    print()
    # Get percentage based on all characters
    [print(i, "-", k, f"| Freq: {round(k * 100 / tot, 2)}%") for i, k in filtered_dict.items()]
    print(f"Total {counter} chosen letters found.")
    print()
    print("(Numbers of Chosen Letters)\n")
    return filtered_dict, counter, tot

# Get user preference and input text, error handle loop
def get_text() -> str:
    print("Would you like to type now, or load a .txt file? ", end="")
    while True:
        type_or_load = input("(type/load): ")
        # Get user input and return if 'type' selected
        if type_or_load.lower().strip() == "type":
            txt = input("Your text: ")
            return txt
        # Get selected file with filedialog, read and return if 'load' selected
        elif type_or_load.lower().strip() == "load":
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

# Convert and return sentence case
def sentence_case(txt: str) -> str:
    # read char by char and capitalize first letter of the sentence
    sentence_list, sentences = [],[]
    indx = 0
    for char in txt:
        if char in "?!." or indx == len(txt) -1:
            sentence_list.append(char)
            sentences.append("".join(sentence_list).capitalize())
            sentence_list.clear()
        elif char == " " and not sentence_list:
            sentences.append(char)
        else:
            sentence_list.append(char)
        indx += 1
    out = "".join(sentences)
    print()
    print(out)
    print("(Sentence Case)\n")
    return out

# Alternating case (indx = 0 for alternate and indx = 1 for inverse case. Default -> 0)
def alternate_case(txt: str, indx:int = 0) -> str:
    out_list = []
    print_word = "Alternate" if indx == 0 else "Inverse"
    for char in txt:
        if char.isalpha():
            if indx % 2 == 0:
                out_list.append(char.lower())
            else:
                out_list.append(char.upper())
            indx += 1
        else:
            out_list.append(char)

    out = "".join(out_list)
    print()
    print(out)
    print(f"({print_word} Case)\n")
    return out

# Title case
def title_case(txt: str) -> str:
    # (APA Style Title Case)
    # (Spaces more than one will be ignored)
    prefix_list = ["anti","bi","co","contra","counter","de","extra","infra","inter","intra","micro","mid","multi",
                   "non","over","peri","post","pre","pro","proto","pseudo","re","semi","sub","super","supra","trans",
                   "tri","ultra","un","under","whole"]

    words = txt.split()
    out_list = []
    non_alpha_char_first, non_alpha_char_last = "",""
    for word in words:
        # Exclude non-alphabetic characters at the beginning and end
        if words.index(word) == -1:
            if word[-1] in "'\"-_*]]}~>":
                non_alpha_char_last = word[-1]
                word = word[:-1]
        elif words.index(word) == 0:
            if word[0] in "'\"-_*([{~<":
                non_alpha_char_first = word[0]
                word = word[1:]

        # Capitalize all words of four letters or more.
        if len(word) < 4:
            out_list.append(word.lower())

        # Handle hyphenated prefixes
        elif word.count("-") == 1:
            prefix = word.split("-")[0]
            after_prefix = word.split("-")[1]

            # Lowercase the second word after a hyphenated prefix (e.g., Mid-, Anti-, Super-, etc.) in
            # compound modifiers (e.g., Mid-year, Anti-hero, etc.).
            if prefix.lower() in prefix_list:
                after_prefix = after_prefix.lower()

            # Capitalize all major words (nouns, verbs including phrasal verbs such as "play with",
            # adjectives, adverbs, and pronouns) in the title/heading, including the second part of
            # hyphenated major words (e.g., Self-Report not Self-report)
            else:
                after_prefix = after_prefix.capitalize()

            out_list.append(prefix.capitalize() + "-" + after_prefix)
        else:
            out_list.append(word.capitalize())

    # Capitalize the first word of the title/heading and of any subtitle/subheading
    out_list[0] = out_list[0].capitalize()
    out = " ".join(out_list)
    # Add first and last characters to the output if there is any
    out = non_alpha_char_first + out + non_alpha_char_last
    print()
    print(out)
    print("(Title Case)\n")
    return out

# Download text
def download_text() -> None:
    # Open file dialog to save the file
    global text
    global output
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(output)
            print("File saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")
    else:
        print("Download canceled.")

# Copy to clipboard
def copy() -> None:
    global text
    global output
    pyperclip.copy(output)
    print("Text and output copied to clipboard.")

# Clear
def clear() -> (str, str):
    global text
    global output
    text = ""
    output = ""
    print("Text and output cleared.")
    return text, output

# MAIN

print("---------------- Character Calculator & Converter ----------------")

# Define global variables
text = get_text()
output = f"Text:\n--------------------------------------------\n{text}\n"

print("--------- Count ---------\n"
      "Count Characters (1)\n"
      "Count Spaces (2)\n"
      "Count Words (3)\n"
      "Count Chosen Letters (4)\n"
      "-------- Convert --------\n"
      "Sentence case (5)\n"
      "lower case (6)\n"
      "UPPER CASE (7)\n"
      "Capitalized Case (8)\n"
      "aLtErNaTiNg cAsE (9)\n"
      "Title Case (10)\n"
      "InVeRsE CaSe (11)\n"
      "--------- File ---------\n"
      "Type/Load New Text (new)\n"
      "Download Text (download)\n"
      "Copy to Clipboard (copy)\n"
      "Clear Text and Output (clear)\n"
      "Exit Application (exit)\n")

# Main program
while True:
    process_choice = input("Choose Process: ")

    # Exit
    if process_choice == "exit":
        print("Exiting the application..")
        break

    # Count characters
    elif process_choice == "1":
        chars, total = count_characters(text)
        output += ("\n" + "Output:\n--------------------------------------------\n"
                   + "".join([f"{i} - {k} | Freq: {round(k * 100 / total, 2)}%\n" for i,k in chars.items()]))
        output += f"Total {total} characters found.\n"
        output += "\n(Numbers of Characters)\n"
        continue

    # Count spaces
    elif process_choice == "2":
        spaces, percent = count_spaces(text)
        output += ("\n" + "Output:\n--------------------------------------------\n"
                   + spaces)
        output += f"Space Freq: {percent}%"
        output += "\n(Numbers of Spaces)\n"
        continue

    # Count words
    elif process_choice == "3":
        words, total = count_words(text)
        output += ("\n" + "Output:\n--------------------------------------------\n"
                   + "".join([f"{i} - {k} | Freq: {round(k * 100 / total, 2)}%\n" for i, k in words.items()]))
        output += f"Total {total} words found.\n"
        output += "\n(Numbers of Words)\n"
        continue

    # Count chosen letters
    elif process_choice == "4":
        letter_dict, chosen_total, total = count_chosen_letters(text)
        output += ("\n" + "Output:\n--------------------------------------------\n"
                   + "".join([f"{i} - {k} | Freq: {round(k * 100 / total, 2)}%\n" for i, k in letter_dict.items()]))
        output += f"Total {chosen_total} chosen letters found.\n"
        output += "\n(Numbers of Chosen Letters)\n"
        continue

    # Sentence case
    elif process_choice == "5":
        output += ("\n" + "Output:\n--------------------------------------------\n"
                   + sentence_case(text))
        output += "\n(Sentence Case)\n"
        continue

    # Lower case
    elif process_choice == "6":
        output += ("\n" + "Output:\n--------------------------------------------\n"
                   + text.lower())
        output += "\n(Lower Case)\n"
        print()
        print(text.lower())
        print("\n(Lower Case)\n")
        continue

    # Upper case
    elif process_choice == "7":
        output += ("\n" + "Output:\n--------------------------------------------\n"
                   + text.upper())
        output += "\n(Upper Case)\n"
        print()
        print(text.upper())
        print("\n(Upper Case)\n")
        continue

    # Capitalized case
    elif process_choice == "8":
        # Split and capitalize each word (it ignores spaces more than one)
        result = " ".join([i.capitalize() for i in text.split()])
        output += ("\n" + "Output:\n--------------------------------------------\n"
                   + result)
        output += "\n(Capitalized Case)\n"
        print()
        print(result)
        print("\n(Capitalized Case)\n")
        continue

    # Alternate case
    elif process_choice == "9":
        output += ("\n" + "Output:\n--------------------------------------------\n"
                   + alternate_case(text))
        output += "\n(Alternate Case)\n"
        continue

    # Title case
    elif process_choice == "10":
        output += ("\n" + "Output:\n--------------------------------------------\n"
                   + title_case(text))
        output += "\n(Title Case)\n"
        continue

    # Inverse case
    elif process_choice == "11":
        # Start indx from 1 to apply inverse case
        output += ("\n" + "Output:\n--------------------------------------------\n"
                   + alternate_case(text, indx=1))
        output += "\n(Inverse Case)\n"
        continue

    # Download
    elif process_choice == "download":
        download_text()
        continue

    # Copy
    elif process_choice == "copy":
        copy()
        continue

    # Clear
    elif process_choice == "clear":
        text, output = clear()
        continue

    # New text
    elif process_choice.lower() == "new":
        text = get_text()
        output += f"\nText:\n--------------------------------------------\n{text}\n"
        continue

    # Invalid input
    else:
        print("Invalid input")
        continue

# Character Calculator

## Overview
This is a simple Python program that allows users to count characters, spaces, and words in a text, as well as search for specific letters. Users can either type their text manually or load a `.txt` file.

## Features
1. **Count Characters:** Counts the number of each character in the text and prints them in a sorted way.
2. **Count Spaces:** Counts how many spaces are in the text.
3. **Count Words:** Counts how many times each word appears in the text and prints them in a sorted way.
4. **Count Chosen Letters:** Allows users to count specific letters of their choice in the text, and it prints them in a sorted way.
5. **Load New Text:** Users can type new text or load a new text file without exiting the application.

## Usage
1. Clone or download the repository to your local machine.
    ```bash
    git clone https://github.com/code-freq/character-calculator.git
    ```
2. Make sure you have **Python 3.x** installed.
3. Install `tkinter` (if not already installed) using the command:
    ```bash
    pip install tk
    ```
4. Run the program (main.py)
5. Follow the on-screen prompts

## Example
Here's an example of what you might see in the program:
```bash
---------------- Simple Character Calculator ----------------
Would you like to type now, or load a .txt file? (type/load): type
Your text: Hello World

Count Characters (1)
Count Spaces (2)
Count Words (3)
Count Chosen Letters (4)
Type/Load New Text (5)
Exit Application (exit)

Choose Process: 1
----------- Numbers of Characters -----------
l - 3
o - 2
space - 1
H - 1
e - 1
W - 1
r - 1
d - 1
```

## Dependencies
- **tkinter:**  Used to open a file dialog and load `.txt` files.

> [!NOTE]
> Make sure that your text files are UTF-8 encoded for proper reading.
> If the file is not found or cannot be opened, an appropriate error message will be shown.

## Contact
For suggestions, recommendations, development ideas, or any issues, feel free to reach out at *code.freq7@gmail.com*
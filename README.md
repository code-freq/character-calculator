# Character Calculator & Converter

## Description
The **Character Calculator & Converter** is a text-processing tool that allows users to load or type text, count characters, words, spaces, and chosen letters, and convert the text into different cases. The tool provides a user-friendly command-line interface and various features to manipulate text efficiently.

## Features
1. **Text Counting:**
   - Count all characters.
   - Count spaces.
   - Count words.
   - Count user-selected letters.
   - Calculate frequencies of options above. (change here)


2. **Text Conversion:**
   - Sentence case.
   - lower case or UPPER CASE.
   - Capitalized Case.
   - aLErNaTiNg CaSe.
   - InVeRsE cAsE.
   - Title Case (APA style).


3. **File Operations:**
   - Load a `.txt` file or type text directly.
   - Download the processed output as a `.txt` file.
   - Copy the text and the processed output to the clipboard.
   - Clear the current text and output.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/code-freq/character-calculator-converter.git
   ```
2. Install the required dependencies:
   ```bash
   pip install pyperclip tkinter
   ```
   
## Usage
1. Launch the script by opening `main.py` on your IDE
2. Follow the on-screen instructions to input your text, choose counting options, or convert the text into different cases.

## Example
Here's an example of what you might see in the program:
```
---------------- Character Calculator & Converter ----------------
Would you like to type now, or load a .txt file? (type/load): type
Your text: Hello world, hello again!
--------- Count ---------
Count Characters (1)
Count Spaces (2)
Count Words (3)
Count Chosen Letters (4)
-------- Convert --------
Sentence case (5)
lower case (6)
UPPER CASE (7)
Capitalized Case (8)
aLtErNaTiNg cAsE (9)
Title Case (10)
InVeRsE CaSe (11)
--------- File ---------
Type/Load New Text (new)
Download Text (download)
Copy to Clipboard (copy)
Clear Text and Output (clear)
Exit Application (exit)

Choose Process: 1

l - 5 | Freq: 20.0%
o - 3 | Freq: 12.0%
space - 3 | Freq: 12.0%
e - 2 | Freq: 8.0%
a - 2 | Freq: 8.0%
H - 1 | Freq: 4.0%
w - 1 | Freq: 4.0%
r - 1 | Freq: 4.0%
d - 1 | Freq: 4.0%
, - 1 | Freq: 4.0%
h - 1 | Freq: 4.0%
g - 1 | Freq: 4.0%
i - 1 | Freq: 4.0%
n - 1 | Freq: 4.0%
! - 1 | Freq: 4.0%
Total 25 characters found.

(Numbers of Characters)

Choose Process: 11

HeLlO wOrLd, HeLlO aGaIn!
(Inverse Case)

Choose Process: exit
Exiting the application..

Process finished with exit code 0
```

## Dependencies
- Python 3.6 or later.
- `pyperclip` for clipboard operations
- `tkinter` for file dialog operations.

> [!NOTE]
> Make sure that your text files are UTF-8 encoded for proper reading.
> 
> If the file is not found or cannot be opened, an appropriate error message will be shown.

## Contact
For suggestions, recommendations, development ideas, or any issues, feel free to reach out at *code.freq7@gmail.com*
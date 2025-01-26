import os

logo = (r'''
 ___ ___   ___   ____    _____   ___         __   ___   ___      ___         __   ___   ____   __ __    ___  ____   ______    ___  ____  
|   T   T /   \ |    \  / ___/  /  _]       /  ] /   \ |   \    /  _]       /  ] /   \ |    \ |  T  |  /  _]|    \ |      T  /  _]|    \ 
| _   _ |Y     Y|  D  )(   \_  /  [_       /  / Y     Y|    \  /  [_       /  / Y     Y|  _  Y|  |  | /  [_ |  D  )|      | /  [_ |  D  )
|  \_/  ||  O  ||    /  \__  TY    _]     /  /  |  O  ||  D  YY    _]     /  /  |  O  ||  |  ||  |  |Y    _]|    / l_j  l_jY    _]|    / 
|   |   ||     ||    \  /  \ ||   [_     /   \_ |     ||     ||   [_     /   \_ |     ||  |  |l  :  !|   [_ |    \   |  |  |   [_ |    \ 
|   |   |l     !|  .  Y \    ||     T    \     |l     !|     ||     T    \     |l     !|  |  | \   / |     T|  .  Y  |  |  |     T|  .  Y
l___j___j \___/ l__j\_j  \___jl_____j     \____j \___/ l_____jl_____j     \____j \___/ l__j__j  \_/  l_____jl__j\_j  l__j  l_____jl__j\_j
''')

# Clears the terminal screen to continue
def clear_screen():
    if os.name == 'nt':     # Windows
        os.system('cls')
    else:                   # macOS or Linux
        os.system('clear')

# Convert
def str_to_morse(string):
    chart = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
    }
    converted_letters = []      # stack the converted letters
    forbidden_letters = []      # stact the letter other than alphabets or numbers

    for word in string.upper().split():
        for letter in word:
            if letter == "/":   # "/" means user wants to break the line
                converted_letters.append("\n")
            elif letter in chart.keys():
                converted_letters.append(f"{chart[letter]} ")
            else:
                forbidden_letters.append(letter)
        converted_letters.append("  ")

    morse_code = "".join(converted_letters)
    deleted_letters = " ".join(forbidden_letters)

    if deleted_letters != "":
        return morse_code + "\n\n" + f"⚠️ {deleted_letters} is(are) deleted."
    return morse_code


# Run the program
is_on = True
while is_on:
    print(f"{logo}\n")
    print("Please follow the instructions below to enter the correct string.\n \
- characters other than alphabets or numbers will be ignored\n \
- to separate the words, insert a space between them\n \
- enter '/' to break the line\n")
    string = input("Enter text: ")
    print(f"\n{str_to_morse(string)}\n")

    should_continue = input("Do you want to try again? (y/n): ")
    if should_continue.lower() == "y":
        clear_screen()
    elif should_continue.lower() == "n":
        is_on = False
        print("👋 Goodbye!")
    else:
        print("Type only 'Y' or 'N' please.")
        is_on = False
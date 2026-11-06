from english_words import get_english_words_set
import random

GREEN = "\033[42m"
YELLOW = "\033[43m"
RESET = "\033[0m"

word_set = get_english_words_set(['web2'], lower=True)


# Filter for a 5-letter game (like Wordle)
five_letter_words = [w.lower() for w in word_set if len(w) == 5]
word = random.choice(five_letter_words)

def user_input():
    while True:
        choice = input("Enter a 5 letter word:")
        if len(choice) > 5 or len(choice) < 5:
            print("Invalid length!")
            continue
        else:
            break
        
    return choice

def score(guess, word):
    result = ["gray"] * 5
    remaining = {}                      # letters in the answer not matched green

    # Pass 1: greens
    for i in range(5):
        if guess[i] == word[i]:
            result[i] = "green"
        else:
            remaining[word[i]] = remaining.get(word[i], 0) + 1

    # Pass 2: yellows, only while unmatched copies remain
    for i in range(5):
        if result[i] == "gray" and remaining.get(guess[i], 0) > 0:
            result[i] = "yellow"
            remaining[guess[i]] -= 1

    return result

def show(guess, result):
    out = ""
    for letter, color in zip(guess, result):
        if color == "green":
            out += f"{GREEN} {letter} {RESET}"
        elif color == "yellow":
            out += f"{YELLOW} {letter} {RESET}"
        else:
            out += f" {letter} "
    print(out)

count = 0

while True:
    guess = user_input()

    show(guess, score(guess, word))

    count+= 1
    if count == 6:
        print("Game Over!")
        print(f"Word: {word}")
        break

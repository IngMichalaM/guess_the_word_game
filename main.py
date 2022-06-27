""" Based on the excersise from Green Fox Academy in C#
 https://github.com/gfamentor/guess-the-word-game"""

TOTAL_WRONG_GUESSES = 5

current_wrong_guesses = 0
word_to_be_guessed = input('Player 1 - write your secret word: ').lower()
guessed_word = len(word_to_be_guessed) * '_'
used_letters = set()  # set

def display_word(in_word):
    print(in_word)

def update_guessed_word(in_letter, guessed_word):
    guessed_word_update = ''
    for count, letter in enumerate(word_to_be_guessed):
        if in_letter == letter:
            guessed_word_update += in_letter
        else:
            guessed_word_update += guessed_word[count]
    return guessed_word_update

print('This is the word you are looking for:')
display_word(guessed_word)

while current_wrong_guesses <= TOTAL_WRONG_GUESSES:
    letter = input('Player 2 - guess a letter: ').lower()
    if letter in used_letters:
        print(f"You have already tried this letter! Your used letters: {', '.join(used_letters)}.")
        continue
    used_letters.add(letter)  # set.add(elem)

    if letter in word_to_be_guessed:
        print(f"Good guess! Letter '{letter}' is in Player's 1 word.")
        guessed_word = update_guessed_word(letter, guessed_word)
        display_word(guessed_word)
        if not '_' in guessed_word:
            print(f'You did it! Great job. The word is "{word_to_be_guessed}".')
            break
    else:
        current_wrong_guesses += 1
        guesses_left = TOTAL_WRONG_GUESSES - current_wrong_guesses

        print(f"Nope, this letter is not in Player's 1 word. You have {guesses_left} guess", end="")
        print(f" left." if guesses_left == 1 else f"es left.")

        if current_wrong_guesses == TOTAL_WRONG_GUESSES:
            print('Too bad, you run out of guesses.')
            user_inp = input('Do you want to try again (y/n): ').lower()
            if user_inp == 'y':
                current_wrong_guesses = 0
                guessed_word = len(word_to_be_guessed) * '_'
                used_letters = set()  # set
            else:
                print(f'Ok. The word was "{word_to_be_guessed}". Better luck next time.')
                break


    #
    # if letter in word_to_be_guessed:
    #     print(f"Good guess! Letter '{letter}' is in Player's 1 word.")
    #     guessed_word = update_guessed_word(letter, guessed_word)
    #     display_word(guessed_word)
    #     if not '_' in guessed_word:
    #         print(f'Your did it! Great job. The word is "{word_to_be_guessed}".')
    #         break
    # else:
    #     current_wrong_guesses += 1
    #     guesses_left = TOTAL_WRONG_GUESSES - current_wrong_guesses
    #
    #     # print(f"{user_input} is even (sudy)" if is_even else f"{user_input} is odd")
    #
    #     print(f"Nope, this letter is not in Player's 1 word. You have {guesses_left} guess", end="")
    #     print(f" left." if guesses_left == 1 else f"es left.")
    #
    #     # if guesses_left == 1:
    #     #     print(f"Nope, this letter is not in Player's 1 word. You have {guesses_left} guess left.")
    #     # else:
    #     #     print(f"Nope, this letter is not in Player's 1 word. You have {guesses_left} guesses left.")

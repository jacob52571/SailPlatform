# imports
import sys

# constants
allowed_letters: list[str] = ['p', 'k', 'h', 'l', 'm', 'n', 'w', 'a', 'e', 'i', 'o', 'u', "'", " "]
consonants: str = "bcdfghjklmnpqrstvwxyz"

# get the message to pronounce in a loop
while True:
    word_hawaiian: str = input("What word do you want to pronounce? ").lower().strip()
    word_pronunciation: str = ""
    num_characters_to_skip: int = 0
    is_invalid: bool = False
    x: int
    for x in range(0, len(word_hawaiian)):
        if word_hawaiian[x] not in allowed_letters:
            print(str(word_hawaiian[x]) + " is not a valid character.")
            is_invalid = True
            break
        # because w has a special rule, we handle it first
        if word_hawaiian[x] == "w" and x > 0:
            if word_hawaiian[x - 1] == "i" or word_hawaiian[x - 1] == "e":
                word_pronunciation += "v"
                continue
        if word_hawaiian[x] in consonants:
            word_pronunciation += word_hawaiian[x]
            continue
        # handle spaces
        if word_hawaiian[x] == " ":
            if word_pronunciation[-1] == "-":
                word_pronunciation = word_pronunciation[:-1]
            word_pronunciation += " "
            continue
        # handle dashes
        if word_hawaiian[x] == "'":
            if word_pronunciation[-1] == "-":
                word_pronunciation = word_pronunciation[:-1]
            word_pronunciation += "'"
            continue
        # if we're here, then x is a vowel
        # we should check if x is the last character, or else we get out of bounds
        is_last_character: bool = x == len(word_hawaiian) - 1

        # if we need to skip characters because they were part of a group, then check it here
        if num_characters_to_skip > 0:
            num_characters_to_skip -= 1
            continue
        if word_hawaiian[x] == "a":
            if is_last_character:
                word_pronunciation += "ah-"
            elif word_hawaiian[x:x + 2] == "ai" or word_hawaiian[x:x + 2] == "ae":
                word_pronunciation += "eye-"
                num_characters_to_skip += 1
            elif word_hawaiian[x:x + 2] == "ao" or word_hawaiian[x:x + 2] == "au":
                word_pronunciation += "ow-"
                num_characters_to_skip += 1
            else:
                word_pronunciation += "ah-"
        elif word_hawaiian[x] == "e":
            if is_last_character:
                word_pronunciation += "eh-"
            elif word_hawaiian[x:x + 2] == "ei":
                word_pronunciation += "ay-"
                num_characters_to_skip += 1
            elif word_hawaiian[x:x + 2] == "eu":
                word_pronunciation += "eh-oo-"
                num_characters_to_skip += 1
            else:
                word_pronunciation += "eh-"
        elif word_hawaiian[x] == "i":
            if is_last_character:
                word_pronunciation += "ee-"
            elif word_hawaiian[x:x + 2] == "iu":
                word_pronunciation += "ew-"
                num_characters_to_skip += 1
            else:
                word_pronunciation += "ee-"
        elif word_hawaiian[x] == "o":
            if is_last_character:
                word_pronunciation += "oh-"
            elif word_hawaiian[x:x + 2] == "oi":
                word_pronunciation += "oy-"
                num_characters_to_skip += 1
            elif word_hawaiian[x:x + 2] == "ou":
                word_pronunciation += "ow-"
                num_characters_to_skip += 1
            else:
                word_pronunciation += "oh-"
        elif word_hawaiian[x] == "u":
            if is_last_character:
                word_pronunciation += "oo-"
            elif word_hawaiian[x:x + 2] == "ui":
                word_pronunciation += "ooey-"
                num_characters_to_skip += 1
            else:
                word_pronunciation += "oo-"

    if not is_invalid:
        print(word_hawaiian.upper() + " is pronounced " + word_pronunciation[:-1].capitalize())
        while True:
            answer = input("Do you want to enter another word? (y/yes/n/no): ").lower()
            if answer in ("n", "no"):
                sys.exit(0)
            elif answer in ("y", "yes"):
                break
            else:
                print("That's not an option.")

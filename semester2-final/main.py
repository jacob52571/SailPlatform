# imports?

# constants
allowed_letters: list[str] = ['p', 'k', 'h', 'l', 'm', 'n', 'w', 'a', 'e', 'i', 'o', 'u', "'", " "]
consonants: str = "bcdfghjklmnpqrstvwxyz"

# get the message to pronounce in a loop
while True:
    word_hawaiian: str = input("What word do you want to pronounce? ")
    word_pronunciation: str = ""
    num_characters_to_skip: int = 0
    x: int
    for x in range(0, len(word_hawaiian)):
        if word_hawaiian[x] not in allowed_letters:
            #todo permanently stop the program once an invalid character was detected
            print(str(word_hawaiian[x]) + " is not a valid character.")
            continue
        if word_hawaiian[x] in consonants:
            word_pronunciation += word_hawaiian[x]
            continue
        # if we're here, then x is a vowel
        # we should check if x is the last character, or else we get out of bounds
        is_last_character: bool = False

        # if we need to skip characters because they were part of a group, then check it here
        if num_characters_to_skip > 0:
            num_characters_to_skip -= 1
            continue
        if x == len(word_hawaiian) - 1:
            is_last_character = True
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
    print(word_hawaiian.upper() + " is pronounced " + word_pronunciation[:-1].capitalize())
    #todo check if the user wants to add another word
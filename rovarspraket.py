

consonants = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"


def translate():  # Rövarspråket secret language translator
    word = input("\nWrite a word/sentence to translate to Rövarspråket: ")
    new_word = []
    for x in word:
        if x in consonants and x.islower():
            new_word.append(x + "o" + x)
        elif x in consonants and not x.islower():
            new_word.append(x + "O" + x if word[1].isupper() else x + "o" + x.lower())
        else:
            new_word.append(x)
    new_word = "".join(new_word)
    print("\nTranslating {} to Rövarspråket: {}".format(word, new_word))
    return new_word


def decode():
    word = input("\nWrite a word/sentence to decode from Rövarspråket secret language: ")
    new_word = ""
    index = 0
    while index in range(len(word)):
        new_word += word[index]
        if word[index] in consonants:
            index += 3
        else:
            index += 1
    print("\n"+new_word)
    return new_word


while True:
    try:
        answer = int(input("\n(1)-Code , (2)-Decode, (3)-Exit : "))
        if answer == 1:
            translate()
        if answer == 2:
            decode()
        if answer == 3:
            break
    except ValueError:
        print("Try again...")


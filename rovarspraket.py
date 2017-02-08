# coding=utf-8

word = raw_input("\nWrite a word/sentence to translate to Rövarspråket: ")

consonants = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"


def translate(word):  # Rövarspråket secret language translator
    new_word = []
    for x in word:
        if x in consonants and x.islower():
            new_word.append(x + "o" + x)
        elif x in consonants and not x.islower():
            new_word.append(x + "O" + x if word[1].isupper() else x + "o" + x.lower())
        else:
            new_word.append(x)
    new_word = "".join(new_word)
    return new_word

print "\nTranslating '%s' to Rövarspråket: " % word,

print translate(word)

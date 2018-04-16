# coding=utf-8

word = input("\nWrite a word/sentence to decode from Rövarspråket secret language: ")

consonants = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"


def decode(word):
    new_word = ""
    index = 0
    while index in range(len(word)):
        new_word += word[index]
        if word[index] in consonants:
            index += 3
        else:
            index += 1
    print(new_word)


decode(word)

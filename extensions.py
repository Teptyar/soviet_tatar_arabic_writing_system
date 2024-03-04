extensional_vowels = ["و","ۇ","ە","ىُ","ي"]
def add_character(word):
    if len(word) > 1 and word[0] == " ":
        if word[1] in extensional_vowels:
            return "ئ" + word[1:]
    return word
print(add_character(" يرىُك"))



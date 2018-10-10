# Manny Pagan
# Sept 24th Python Course
# Assignment 5
# Due: Oct 10th



user_text = (reversed(input("Type something here: ")))

def spell_backwards():
    k = ['']
    for letter in list(user_text):
        k.append(letter)
    print(''.join(k))

spell_backwards()


__author__ = 'Jake'

chars = open('../default/challenge3_characters', 'r')

guardCount = 0
side = 'Left'
heldChar = '$'

# TODO: Should use regex

while 1:
    char = chars.read(1)
    keptChar = '!'
    if not char:
        break

    if char.isalpha():
        if char.isupper():
            guardCount += 1
        elif (guardCount == 3) & (side == 'Left'):
            heldChar = char
            side = 'Right'
            guardCount = 0
        elif (guardCount == 3) & (side == 'Right'):
            print(heldChar)
            side = 'Left'
            guardCount = 0
        else:
            side = 'Left'
            guardCount = 0

#linkedlist
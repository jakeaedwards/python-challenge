__author__ = 'Jake'

chars = open('../default/challenge2_characters', 'r')

counts = {}

while 1:
    char = chars.read(1)
    if not char:
        break
    value = counts.pop(char, 0)
    counts.update({char: value+1})

print(counts)

# y t i e l a u q
# equality
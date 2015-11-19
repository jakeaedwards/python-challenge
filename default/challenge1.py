__author__ = 'Jake'

# K --> M
# O --> Q
# E --> G

# Need to shift each character by two ordinal positions (Caesar Cipher)

input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb" \
        " rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
output = ''

for c in input:
    if c.isalpha():
        pos = ord(c)+2
        if pos > ord('z'):
            pos -= 26
        output += chr(pos)
    else:
        output += c

print(output)

# REVEALED SOLUTION:

url = 'http://www.pythonchallenge.com/pc/def/map.html'
trantab = str.maketrans('map', 'ocr')
print('map'.translate(trantab))

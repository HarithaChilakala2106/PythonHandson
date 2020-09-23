from random import randint

encryptstr = ""
f = open('input.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    key = 157  # randint(0, 255)
    print(key)
    encryptstr = ""
    for char in line.rstrip("\n"):
        if not char.isdigit():
            encryptstr = encryptstr + chr(ord(char) ^ key)
        else:
            encryptstr = encryptstr + str(int(char) ^ key)
    print(encryptstr)
    outputf = open('output.txt', 'a')
    outputf.write(encryptstr)

f.close()
outputf.close()

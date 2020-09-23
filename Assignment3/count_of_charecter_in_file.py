# Python3 code to demonstrate
# occurrence frequency using
# re + findall()
import re

dictionary = {}
try:
    f = open('input.txt', 'r')
    isEmpty = True
    while True:
        line = f.readline()
        if len(line) <= 0:
            break
        else:
            isEmpty = False
            for letter in line.lower():
                count = 0
                if letter.isalpha():
                    count = len(re.findall(letter, line.lower()))  # '(?i)' for ignore case
                    if letter in dictionary.keys():
                        dictionary[letter] = count
                    else:
                        # if the word doe not exist in dictionary add it
                        dictionary.update({letter: count})
    f.close()
    if not isEmpty:
        dictionarysorted = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
        output = ''
        for char in dictionarysorted:
            output = output + char[0] + ": " + str(char[1]) + ", "
        f = open('frequency_of_char_in_file.txt', 'w')
        f.write('"' + output[:len(output) - 2] + '"')
        f.close()
    else:
        print("File is Empty")

except IOError:
    print("File not Found")


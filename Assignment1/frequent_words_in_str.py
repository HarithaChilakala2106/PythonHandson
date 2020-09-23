def countwords(sentence):
    dictionary = {}
    for element in sentence.split():
        # if the word exists already in dictionary update its frequency
        if element in dictionary.keys():
            dictionary[element] += 1
        else:
            # if the word doe not exist in dictionary add it
            dictionary.update({element: 1})
            # sort the dictionary and then get the words wich occured minimum twice
    dictionarysorted = [item for item in sorted(dictionary.items(), key=lambda x: x[0]) if item[1] >= 2]
    if len(dictionarysorted) > 0:
        # merge the frequent words with space
        return ' '.join([word for word in dictionarysorted])
    else:
        print("No frequent words in given string ", sentence)


def main():
    givenstring = input("Please enter a string: ")
    while not len(givenstring) > 0:
        givenstring = input("Please enter a string : ")
    fequentwordstr = countwords(givenstring)
    if len(fequentwordstr) > 0:
        print(fequentwordstr)


main()

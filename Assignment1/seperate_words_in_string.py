def seperatestring(inputstr):
    if len(inputstr) > 0:
        # split the string by space
        return inputstr.split()


def main():
    givenstr = input("Please enter a string : ")
    while not len(givenstr) > 0:
        givenstr = input("Please enter your string : ")
    print(seperatestring(givenstr))


main()

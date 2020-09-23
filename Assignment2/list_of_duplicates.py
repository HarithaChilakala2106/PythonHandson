def list_of_duplicates_as_list(inputlist):
    finallist = list()
    currentindex = 0
    while currentindex < len(inputlist):
        currentelement = inputlist[currentindex]
        startindex = currentindex
        endindex = startindex
        # endindex is the index until which the current element is occured consecutively
        while endindex < len(inputlist) - 1:
            if inputlist[endindex + 1] == currentelement:
                endindex = endindex + 1
            else:
                break
        # create a list with current element by including all its consequtive elements equal to currentelemetn
        currentelelist = inputlist[startindex:endindex + 1]
        currentindex = endindex + 1
        finallist.append(currentelelist)
    return finallist


def main():
    inputlist = [0, 0, 1, 1, 1, 2, 3, 4, 4, 6, 6, 6, 8, 4, 4]
    print(list_of_duplicates_as_list(inputlist))


main()

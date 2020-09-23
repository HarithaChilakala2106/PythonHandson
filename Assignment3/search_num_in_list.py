import math


def search_withoutrecursion(number, inputlst):
    ind = -1
    for position, num in enumerate(inputlst):
        if num == numbertocheck:
            ind = position
    return ind


def search_withrecursion(inputlst, left, right, number):
    if right >= left:
        mid = math.floor((right + left) / 2)

        if inputlst[mid] == number:
            return mid
        elif inputlst[mid] > number:
            return search_withrecursion(inputlst, left, mid - 1, number)
        else:
            return search_withrecursion(inputlst, mid, right - 1, number)
    return -1


while True:
    inputlist = [1, 3, 5, 7, 9, 15, 20]
    print(inputlist)
    numbertocheck = int(input("Please enter a number to check in list (not empty): "))
    index = search_withoutrecursion(numbertocheck, inputlist)
    # index = search_withrecursion(inputlist, 0, len(inputlist) - 1, numbertocheck)
    if index == -1:
        print("Number  {0}  -> result: No doesn’t belong to list".format(numbertocheck))
    else:
        print("Number {0}  ->  result: Yes, belongs to list and found at index {1} :".format(numbertocheck, index))
    if input("Do you want to check another number (y/n):  ").__eq__("n"):
        break

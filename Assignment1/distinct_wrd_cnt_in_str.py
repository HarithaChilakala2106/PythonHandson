def distinct_wrd_cnt_in_str(inputstr):
    if len(inputstr) > 0:
        arrwords = {}
        wordslist = inputstr.split()
        for ele in wordslist:
            # find each word cound in given string (seperated with space and stored as list )
            # then add each word with count into a dictionary i.e arrwords
            arrwords[ele] = wordslist.count(ele)
    return arrwords


def words_with_freq_lexicographic_order(arrwords):
    arrwordssort = sorted((key, value) for (key, value) in arrwords.items())
    return arrwordssort


def main():
    listofwordswithcnt = distinct_wrd_cnt_in_str(input("Please enter a string : "))
    print("List of words in the given string with frequency :",list(listofwordswithcnt.items()))
    print("Words with frequency in lexicographic order : ", words_with_freq_lexicographic_order(listofwordswithcnt))


main()

def count_strings(names):
    """
    Find the total number of names starting with lowercase
    :param names:
    :return:
    """
    return len(list(filter(lambda name: name[0].islower(), names)))


def sort_words(words):
    """
    Sort the words in the list based on their second letter from a to z
    :param words:
    :return:
    """
    print(sorted(words, key=lambda x: x[1]))


def sort_tuples(tupleslist):
    """
    Sort the tuples in the list based on the last character of the second items
    :param tupleslist:
    :return:
    """
    print(sorted(tupleslist, key=lambda x: x[1][-1]))


if __name__ == '__main__':
    listofnames = ["student", "hi", "ReDI", "good", "evening"]
    print(listofnames)
    print("No.of words starting with lowercase letter", count_strings(listofnames))
    sort_words(listofnames)

    tuplist = [('redi', 'school'), ("backend", "python")]
    sort_tuples(tuplist)

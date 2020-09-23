def validate_password(password):
    # check password length is minimum 8 charecters
    if len(password) >= 8:
        digitcount = 0
        containsupper = False
        haveconsdigit = False
        # Iterate over charecters in password for further checks
        for i, char in enumerate(password):
            # check if any charecter in password is upper
            if char.isupper():
                containsupper = True
            if char.isdigit():
                digitcount = digitcount + 1
                # consecutive digits check can not be done for last charecter so check index value
                if i != len(password) - 1 and password[i + 1].isdigit():
                    # first = int(char) + 1 Harritha12
                    # second = password[i + 1]
                    # check for any two consecutive digits
                    if int(char) + 1 == int(password[i + 1]):
                        haveconsdigit = True
        if containsupper:
            if digitcount >= 2:
                if not haveconsdigit:
                    return True
                else:
                    print("Can’t contain two consecutive digits (e.g.: “UX525!pun” fails the criteria)")
            else:
                print('Must contain at least two digits (e.g: “Uv3!xxzy” fails the criteria)')
        else:
            print('Must contain at least one upper-case letter (e.g.: “ab3cd@1efg” fails the criteria)')
    else:
        print('Must have a minimum of 8 characters. (e.g.: “Al4e2!” fails the criteria')

    return False


def main():
    password = input("Please enter your password : ")
    while not validate_password(password):
        password = input("Please enter your password: ")
    print("Your password is strong enough")


main()

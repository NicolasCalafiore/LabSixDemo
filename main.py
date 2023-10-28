# Nicolas Calafiore

PASSWORD_ENCODED = ""
PASSWORD_RAW = ""

def print_menu():    # Prints Main Menu - Returns Menu Selection INT
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    menuSelection = input(("Please enter an option: "))
    return menuSelection

def encode():    # Converts int to list, shifts each element up by 3, returns int from joined list
    password = int(input("Please enter your password to encode: "))
    passwordList = [int(char) for char in str(password)]
    print("Your password has been encoded and stored!")
    return (''.join(str(int(char) + 3) for char in passwordList), password)

def Main():
    menuSelection = ""

    while menuSelection != "3":    # While User Does Not Select Quite
        menuSelection = print_menu()
        if menuSelection == "1":    # Encode
            PASSWORD_ENCODED, PASSWORD_RAW = encode()

        # TODO: Decode Function


if __name__ == '__main__':
    Main()


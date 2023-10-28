# Nicolas Calafiore

PASSWORD_ENCODED = ""
PASSWORD_RAW = ""

def print_menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    menuSelection = input(("Please enter an option: "))
    return menuSelection

def encode():
    password = int(input("Please enter your password to encode: "))
    passwordList = [int(char) for char in str(password)]
    print("Your password has been encoded and stored!")
    return (''.join(str(int(char) + 3) for char in passwordList), password)

def Main():
    menuSelection = ""

    while menuSelection != "3":
        menuSelection = print_menu()
        if menuSelection == "1":
            PASSWORD_ENCODED, PASSWORD_RAW = encode()
            print(PASSWORD_ENCODED)
            print(PASSWORD_RAW)

        # TODO: Decode Function


if __name__ == '__main__':
    Main()


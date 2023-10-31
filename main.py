# Nicolas Calafiore

PASSWORD_ENCODED = ""

def print_menu():    # Prints Main Menu - Returns Menu Selection INT
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    menuSelection = input(("Please enter an option: "))
    return menuSelection

def encode():    # Converts int to list, shifts each element up by 3, returns int from joined list
    password = input("Please enter your password to encode: ")
    passwordList = [int(char) for char in password]
    encodedList = []
    for i in range(len(passwordList)):
        encodedDigit = (passwordList[i] + 3) % 10
        encodedList.append(encodedDigit)
    return (''.join(str(digit) for digit in encodedList))

def decode(encoded_password):
    encodedList = [int(char) for char in encoded_password]
    decodedList = []
    for i in range(len(encodedList)):
        decodedDigit = (encodedList[i] - 3) % 10
        decodedList.append(decodedDigit)
    return ''.join(str(digit) for digit in decodedList)

def Main():
    menuSelection = ""

    while menuSelection != "3":    # While User Does Not Select Quit

        menuSelection = print_menu()
        if menuSelection == "1":    # Encode
            PASSWORD_ENCODED = encode()
            print("Your password has been encoded and stored!\n")


        if menuSelection == "2": # Decode
            print(f'The encoded pass is {PASSWORD_ENCODED}, and the original password is {decode(PASSWORD_ENCODED)}\n')






if __name__ == '__main__':
    Main()


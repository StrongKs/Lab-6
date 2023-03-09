def menu():
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")

# hi sydney, please make as decode function here and push it back
def decode(string):
    pass

# add 3 to every digit and if its bigger then 9 return the %10
def encode(string):
    encoded_string = ""
    for char in string:
        encoded_string += str((int(char) + 3) % 10)
    return encoded_string


if __name__ == "__main__":
    while True:
        menu()
        menu_option = int(input("Please enter and option: "))
        if menu_option == 1:
            user_input = input("Please enter your password to encode: ")
            input_encoded = encode(user_input)
            print("Your password has been encoded and stored!\n")
        elif menu_option == 2:
            print("The encoded password is " + input_encoded + ", and the original password is " + decode(user_input))
            print()
        elif menu_option == 3:
            break

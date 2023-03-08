# lab 6 encode, menu, and main functions by Jonathan Phillips

def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()


def encode(password):
    encoded_password_string = ''
    for i in password:
        encoded_value = (int(i) + 3) % 10
        encoded_password_string += str(encoded_value)
    encoded_password = encoded_password_string
    return encoded_password


if __name__ == '__main__':
    stop = 0
    while stop != 1:
        print_menu()
        option = int(input('Please enter an option: '))
        if option == 1:
            password = input('Please enter your password to encode: ')
            encoded_pw = encode(password)
            print('Your password has been encoded and stored!')
            print()
        elif option == 2:
            decoded_pw = decode(encoded_pw)
            print(f'The encoded password is {encoded_pw}, and the original password is {decoded_pw}.')
            print()
        elif option == 3:
            stop += 1

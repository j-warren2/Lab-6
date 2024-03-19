import sys


def encoder(password):  # Jakayla Warren
    encoded = ''
    if len(password) == 8:
        for i in password:
            i = int(i)
            new_i = i + 3
            if len(str(new_i)) == 1:
                new_i = str(new_i)
                encoded += new_i
            else:
                new_i = str(new_i)
                new_i = new_i[1:]
                encoded += new_i
    return encoded


def menu():
    print('')
    print('Menu')
    print('')
    print('-------------')
    print('')
    print('1. Encode')
    print('')
    print('2. Decode')
    print('')
    print('3. Quit')
    print('')


def main():
    menu()
    password = None
    selection = input('Please enter an option: ')
    while selection != '3':
        if selection == '1':
            print('')
            password = input('Please enter your password to encode: ')
            print('')
            print('Your password has been encoded and stored!')
            menu()
            selection = input('Please enter an option: ')
        elif selection == '2':
            pass
    else:
        sys.exit()


if __name__ == '__main__':
    main()
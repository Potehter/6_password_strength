import re


def get_entrance_black_list(password):
    try:
        file_passwords = open('passwords.txt', 'r')
    except IOError as e:
        print('Cannot check password in black list')
        return 0
    else:
        with file_passwords:
            black_passwords = file_passwords.read()
            list_black_passwords = black_passwords.split('\r\n')
            if password in list_black_passwords:
                return 0
            else:
                return 3


def get_length_strength(password):
    if len(password) > 10:
        return 3
    elif len(password) > 8:
        return 2
    elif len(password) > 5:
        return 1
    else:
        return 0


def get_character_diversity(password):
    counter = 0
    array_re_to_check = ['[a-z]', '[A-Z]', '\d', '\W']
    for each_case in array_re_to_check:
        match = re.search(each_case, password)
        if match:
            counter += 1
    return counter


def get_password_strength(password):
    strength_lenght = get_length_strength(password)
    strength_diversity = get_character_diversity(password)
    strength_from_black_list = get_entrance_black_list(password)
    total_strength = sum((strength_lenght, strength_diversity, 
                          strength_from_black_list))
    return str(total_strength)


def main():
    password = input('Input password to check: ')
    print('Strength of your password: ' + get_password_strength(password))


if __name__ == '__main__':
    main()

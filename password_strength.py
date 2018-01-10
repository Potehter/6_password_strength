import re
import getpass


def get_passwords_list():
    with open('passwords.txt', 'r') as file_passwords:
        black_passwords = file_passwords.read()
        list_black_passwords = black_passwords.split('\n')
    return list_black_passwords


def check_password_in_black_list(password):
    list_black_passwords = get_passwords_list()
    return password not in list_black_passwords


def get_length_strength(password):
    good_length = 10
    normal_length = 8
    bad_length = 5
    if len(password) > good_length:
        return 3
    elif len(password) > normal_length:
        return 2
    elif len(password) > bad_length:
        return 1
    else:
        return 0


def get_character_diversity(password):
    counter = 0
    array_patterns_to_check = ['[a-z]', '[A-Z]', '\d', '\W']
    for pattern in array_patterns_to_check:
        match = re.search(pattern, password)
        if match:
            counter += 1
    return counter


def get_password_strength(password):
    strength_lenght = get_length_strength(password)
    strength_diversity = get_character_diversity(password)
    strength_from_black_list = check_password_in_black_list(password) * 3
    total_strength = sum((
        strength_lenght,
        strength_diversity,
        strength_from_black_list
    ))
    return total_strength


def main():
    password = getpass.getpass('Input password to check: ')
    print('{}: {}'.format('Strength of your password',
                          get_password_strength(password)))


if __name__ == '__main__':
    main()

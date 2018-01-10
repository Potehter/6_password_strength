import re
import getpass


def get_passwords_list():
    with open('passwords.txt', 'r') as file_passwords:
        black_passwords = file_passwords.read()
        list_black_passwords = black_passwords.split('\r\n')
        return list_black_passwords


def get_strength_from_black_list(password):
    list_black_passwords = get_passwords_list()
    if list_black_passwords:
        if password in list_black_passwords:
            return 0
        else:
            return 3
    else:
        return 0


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
    array_cases_to_check = ['[a-z]', '[A-Z]', '\d', '\W']
    # \d - any digit, \W - any special character (not digit, letter)
    for case in array_cases_to_check:
        match = re.search(case, password)
        if match:
            counter += 1
    return counter


def get_password_strength(password):
    strength_lenght = get_length_strength(password)
    strength_diversity = get_character_diversity(password)
    strength_from_black_list = get_strength_from_black_list(password)
    total_strength = sum((
        strength_lenght,
        strength_diversity,
        strength_from_black_list
    ))
    return str(total_strength)


def main():
    password = getpass.getpass('Input password to check: ')
    print('{}: {}'.format('Strength of your password',
                          get_password_strength(password)))


if __name__ == '__main__':
    main()

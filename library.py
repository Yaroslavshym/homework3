import random


# Homework part 1
def check_number(user_password: str) -> bool:
    numbers = '1234567890'
    for char in user_password:
        if char in numbers:
            return True
    return False


def check_length(user_password: str) -> bool:
    if len(user_password) >= 8:
        return True
    return False


def check_upper_char(user_password: str) -> bool:
    for char in user_password:
        if char.isupper():
            return True
    return False


def check_lower_char(user_password: str) -> bool:
    for char in user_password:
        if char.islower():
            return True
    return False


def check_special_char(user_password: str) -> bool:
    special_char = '+-/*!"№;%:?*()='
    for char in user_password:
        return True
    return False


def check_if_space_char(user_password: str) -> bool:
    if user_password.find(' '):
        return False
    return True


def check_if_lat_char(user_password: str) -> bool:
    if user_password.isascii():
        return True
    return False


def check_password(user_password: str) -> bool:
    condition1 = check_length(user_password)
    condition2 = check_upper_char(user_password)
    condition3 = check_lower_char(user_password)
    condition4 = check_special_char(user_password)
    condition5 = check_if_space_char(user_password)
    condition6 = check_if_lat_char(user_password)
    condition7 = check_number(user_password)
    first_part_of_conditions = condition1 and condition2 and condition3
    second_part_of_conditions = condition4 and condition5 and condition6 and condition7
    list_of_conditions = all([first_part_of_conditions, second_part_of_conditions])
    if list_of_conditions:
        return True
    return False


# Homework part 2
def create_random_number(lower_number: int, higher_number: int) -> int:
    random_number = random.randint(lower_number, higher_number)
    return random_number

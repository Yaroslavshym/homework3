import library as lib


def test_check_number():
    user_password_v1 = 'Password'
    user_password_v2 = 'Password1'
    user_password_v3 = '1'
    user_password_v4 = ''
    condition1 = not lib.check_number(user_password_v1)
    condition2 = lib.check_number(user_password_v2)
    condition3 = lib.check_number(user_password_v3)
    condition4 = not lib.check_number(user_password_v4)
    list_of_conditions = [condition1, condition2, condition3, condition4]
    assert all(list_of_conditions)


def test_check_length():
    user_password_v1 = 'password'
    user_password_v2 = 'pass'
    user_password_v3 = ''
    condition1 = lib.check_length(user_password_v1)
    condition2 = not lib.check_length(user_password_v2)
    condition3 = not lib.check_length(user_password_v3)
    list_of_conditions = [condition1, condition2, condition3]
    assert all(list_of_conditions)


def test_check_upper_char():
    user_password_v1 = 'Password'
    user_password_v2 = 'PASSWORD'
    user_password_v3 = 'password'
    condition1 = lib.check_upper_char(user_password_v1)
    condition2 = lib.check_upper_char(user_password_v2)
    condition3 = not lib.check_upper_char(user_password_v3)
    list_of_conditions = [condition1, condition2, condition3]
    assert all(list_of_conditions)


def test_check_lower_char():
    user_password_v1 = 'PASSWORd'
    user_password_v2 = 'PASSWORD'
    user_password_v3 = 'password'
    condition1 = lib.check_lower_char(user_password_v1)
    condition2 = not lib.check_lower_char(user_password_v2)
    condition3 = lib.check_lower_char(user_password_v3)
    list_of_conditions = [condition1, condition2, condition3]
    assert all(list_of_conditions)


def test_check_special_char():
    list_of_user_passwords = []
    special_char = '+-/*!"№;%:?*()='
    for char in special_char:
        list_of_user_passwords.append(lib.check_special_char(f'Password{char}'))
    check_password = all(list_of_user_passwords) and not lib.check_special_char('Password')
    assert check_password


def test_check_if_lat_char():
    user_password_v1 = 'Password'
    user_password_v2 = 'Пароль'
    condition1 = lib.check_if_lat_char(user_password_v1)
    condition2 = not lib.check_if_lat_char(user_password_v2)
    list_of_conditions = [condition1, condition2]
    assert all(list_of_conditions)


def test_check_password():
    list_of_conditions = []
    user_password_v1 = 'Password'
    user_password_v2 = 'Password'
    user_password_v3 = 'password'
    user_password_v4 = 'P+ssword'
    user_password_v5 = 'Password'
    user_password_v6 = 'пароль'
    user_password_v7 = 'Password1'
    user_password_v8 = '+Password1657'
    condition1 = not lib.check_password(user_password_v1)
    condition2 = not lib.check_password(user_password_v2)
    condition3 = not lib.check_password(user_password_v3)
    condition4 = not lib.check_password(user_password_v4)
    condition5 = not lib.check_password(user_password_v5)
    condition6 = not lib.check_password(user_password_v6)
    condition7 = not lib.check_password(user_password_v7)
    condition8 = lib.check_password(user_password_v8)
    first_part_of_conditions = [condition1, condition2, condition3, condition4]
    second_part_of_conditions = [condition5, condition6, condition7, condition8]
    list_of_conditions = all([first_part_of_conditions, second_part_of_conditions])
    assert list_of_conditions


# Homework part 2


def test_random_number():
    condition1 = lib.create_random_number(0, 1)
    condition2 = lib.create_random_number(2, 3)
    final_condition_part1 = condition1 == 0 or condition1 == 1
    final_condition_part2 = condition2 == 2 or condition2 == 3
    list_of_conditions = [final_condition_part1, final_condition_part2]
    assert all(list_of_conditions)

        
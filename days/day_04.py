import re

from input.return_input import read_input_file


def task_00():
    passport_list = [i.strip() for i in read_input_file('input/day_04.inp')]
    passports = []
    passport = {}
    for i in range(len(passport_list)):
        entry = passport_list[i]
        if len(entry) == 0:
            passports.append(passport)
            passport = {}

        elif i == len(passport_list) - 1:
            for k in entry.split():
                dict_entry = (k.split(':'))
                passport[dict_entry[0]] = dict_entry[1]
            passports.append(passport)
        else:
            for k in entry.split():
                dict_entry = (k.split(':'))
                passport[dict_entry[0]] = dict_entry[1]
    return passports


def test_integer(lower=None, higher=None, number=None):
    return lower <= int(number) <= higher


def test_height(height_unit=None):
    try:
        height = int(height_unit[:-2])
        unit = height_unit[-2:]
        if unit == 'cm' and 150 <= height <= 193:
            return True
        elif unit == 'in' and 59 <= height <= 76:
            return True
        else:
            return False
    except ValueError:
        print(height_unit)
        return False


def test_hair_color(hair_color=None):
    return bool(re.match(r"^#[0-9a-f]{6}$", hair_color))


def test_eye_color(eye_color=None):
    return eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def test_passpord_id(passport_id=None):
    return bool(re.match(r"^[0-9]{9}$", passport_id))


def check_for_valid_passport(passport=None):
    valid_keys = {'hgt', 'eyr', 'pid', 'hcl', 'iyr', 'ecl', 'byr'}
    return (len(valid_keys - passport.keys())) == 0


def task_01():
    passports = task_00()
    valid_passports = 0
    for passport in passports:
        if check_for_valid_passport(passport=passport):
            valid_passports += 1
    return valid_passports


def task_02():
    passports = task_00()
    counter = 0
    for passport in passports:
        if check_for_valid_passport(passport):
            if test_integer(lower=1920, higher=2002, number=passport['byr']):
                if test_integer(lower=2010, higher=2020, number=passport['iyr']):
                    if test_integer(lower=2020, higher=2030, number=passport['eyr']):
                        if test_height(height_unit=passport['hgt']):
                            if test_hair_color(passport['hcl']):
                                if test_eye_color(passport['ecl']):
                                    if test_passpord_id(passport_id=passport['pid']):
                                        counter += 1
    return counter


if __name__ == '__main__':
    print(test_integer(lower=2, higher=5, number=3))
    print(test_height(height_unit='34cm'))
    print(test_passpord_id(passport_id='03737962'))

from input.return_input import read_input_file


def task_01():
    passport_list = [i.strip() for i in read_input_file('input/day_04.inp')]
    passports = []
    passport = {}
    valid_passports = 0
    valid_keys = {'hgt', 'eyr', 'pid', 'hcl', 'iyr', 'ecl', 'byr'}
    for i in range(len(passport_list)):
        entry = passport_list[i]
        if len(entry) == 0:
            passports.append(passport)
            passport = {}

        elif i == len(passport_list) - 1:
            for i in entry.split():
                dict_entry =(i.split(':'))
                passport[dict_entry[0]] = dict_entry[1]
            passports.append(passport)
        else:
            for i in entry.split():
                dict_entry =(i.split(':'))
                passport[dict_entry[0]] = dict_entry[1]
    for passport in passports:
        if (len(valid_keys - passport.keys())) == 0:
            valid_passports += 1
    return valid_passports

def task_02():
    return
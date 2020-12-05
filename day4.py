import re

passports = []

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def multiplyList(myList) :

    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x
    return result

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def valid_field(field):
    if field[0] == 'byr':
     return RepresentsInt(field[1]) and 1920 <= int(field[1]) <= 2002
    if field[0] == 'iyr':
        return RepresentsInt(field[1]) and 2010 <= int(field[1]) <= 2020
    if field[0] == 'eyr':
        return RepresentsInt(field[1]) and 2020 <= int(field[1]) <= 2030

    if field[0] == 'hgt':
        if 'cm' in field[1]:
            return RepresentsInt(field[1].replace('cm','')) and 150 <= int(field[1].replace('cm','')) <= 193
        if 'in' in field[1]:
            return RepresentsInt(field[1].replace('in','')) and 59 <= int(field[1].replace('in','')) <= 76
        return False

    if field[0] == 'hcl':
        return re.match('^#[0-9a-f]{6}$', field[1]) is not None

    if field[0] == 'ecl':
        return field[1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if field[0] == 'pid':
        return re.match('^[0-9]{9}$', field[1]) is not None
    if field[0] == 'cid':
        return True
    return False

passport = []
with open("day4-input.txt", 'r') as infile:
    while True:
        line = infile.readline()
        if not line:
            break
        line = line.strip()
        if line == "":
            passports.append(passport)
            passport = []
        else:
            passport.extend(line.split(" "))

count_valid = 0
count_valid_data = 0

for p in passports:
    count_valid_fields = 0
    count_valid_fields_data = []
    for data in p:
        if data.split(":")[0] in required_fields:
            count_valid_fields += 1
            count_valid_fields_data.append(valid_field(data.split(":")))
            # print(data)
    if(count_valid_fields == len(required_fields)):
        count_valid += 1
        if False not in count_valid_fields_data:
            #print(count_valid_fields_data)
            count_valid_data += 1

    #print(count_valid_fields_data)

print(count_valid)


print("")
print("PART2")
print(count_valid_data)

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

def read_file(filename):
    data = []
    answer = []
    with open(filename, 'r') as infile:
        while True:
            line = infile.readline()
            if not line:
                break
            line = line.strip()
            if line == "":
                data.append(answer)
                answer = []
            else:
                answer.extend(line)
    return data

def read_file_part_2(filename):
    data = []
    answer = []
    with open(filename, 'r') as infile:
        while True:
            line = infile.readline()
            if not line:
                break
            line = line.strip()
            if line == "":
                data.append(answer)
                answer = []
            else:
                answer.append(line)
    return data



dataset = "abcdefghijklmnopqrstuvwxyz"

data = read_file("day6-input.txt")

# print(data)

sum = 0
for d in data:
    sum += (len(set(d)))

print(sum)


print("PART2: ")

data = read_file_part_2("day6-input.txt")
# print("DATA:", data)

from collections import Counter
counts = 0
for group in data:
    count_group = 0
    answers = []
    for person in group:
        answers.append(list(set(''.join(person))))
    counts += len(set.intersection(*map(set,answers)))

print(counts)

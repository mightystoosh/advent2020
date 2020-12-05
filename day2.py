


def is_pwd_valid(data):
    count_of_string = data["length"].split("-")
    #print(data, int(count_of_string[0]), int(count_of_string[1]), data["pwd"].count(data["char"]))
    if int(count_of_string[0]) <= data["pwd"].count(data["char"]) <= int(count_of_string[1]):
        return True
    return False

def is_pwd_valid2(data):
    count_of_string = data["length"].split("-")
    #print(data, int(count_of_string[0]), int(count_of_string[1]), data["pwd"].count(data["char"]))
    if (data["char"] == data["pwd"][int(count_of_string[0]) - 1]) and (data["char"] != data["pwd"][int(count_of_string[1]) - 1]) or (data["char"] != data["pwd"][int(count_of_string[0]) - 1]) and (data["char"] == data["pwd"][int(count_of_string[1]) - 1]):
        return True
    return False

policy = {"length": "", "char": "", "pwd": ""}
data = []

with open("day2-input.txt", 'r') as infile:
    while True:
        line = infile.readline()
        if not line:
            break
        line = line.strip().split(" ")
        data.append({"length": line[0], "char": line[1].replace(":",""), "pwd": line[2]})

count = 0
for i in data:
    if is_pwd_valid(i):
        print(i)
        count += 1
print("PART1: ", count)

count = 0
for i in data:
    if is_pwd_valid2(i):
        print(i)
        count += 1
print("PART2: ", count)

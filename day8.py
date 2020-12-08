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
    with open(filename, 'r') as infile:
        while True:
            line = infile.readline()
            if not line:
                break
            line = line.strip()
            data.append(line)
    return data

def initialize_data():
    data = read_file("day8-input.txt")
    order = 0
    new_data = {}
    for d in data:
        command  = d.split()
        new_data[order] = [command[0], int(command[1].replace('+','')), 0]
        order += 1
    return new_data


def do_command(data, current, accumulator):
    order, num_times, command, attribute = current, data[current][2], data[current][0], data[current][1]
    #print(order, num_times, command, attribute)
    if num_times == 1:
        return order, accumulator, data, False
    if command == 'nop':
        order += 1
    elif command == 'acc':
        accumulator += attribute
        order += 1
    elif command == 'jmp':
        order += attribute

    data[current][2] += 1
    return order, accumulator, data, True

accumulator = 0
previous = 0
data = (initialize_data())
#print(data)
current = 0

keep_running = True
while keep_running:
    current, accumulator, data, keep_running = do_command(data, current, accumulator)

print("PART1:", accumulator)


# PART2

data = (initialize_data())

#print(data)

current = 0
accumulator = 0
previous_jmp = []
keep_running = True

keep_running = True
while current != max(data):
    current, accumulator, data, keep_running = do_command(data, current, accumulator)
    if data[current][0] == "jmp":
        previous_jmp.append(current)
    if keep_running is False:
        #print("END", current, previous, previous_jmp, data[previous_jmp[-2]])
        accumulator = 0
        current = 0
        previous = 0
        data = (initialize_data())
        data[previous_jmp[-2]][0] = 'nop'
        previous_jmp = []
    else:
        previous = current

current, accumulator, data, keep_running = do_command(data, current, accumulator)
print("PART2:", accumulator)


#order, num_times, command, atrribute

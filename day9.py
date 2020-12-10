import re
import itertools

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def sum_list(mylist, num):
    if sum(mylist) == num:
        return True
    else:
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
            data.append(int(line))
    return data


def find_sum(data, to_find, length=2):
    # print(data)
    for i, d in enumerate(data):
      for x in range(0, len(data)):
        if i + length + x > len(data):
          break
        # print(data[i : i + length + x])
        if sum(data[i : i + length + x]) == to_find:
            return data[i : i + length + x]
        elif sum(data[i + x: i + length]) > to_find:
            continue
    data.pop(0)
    return find_sum(data, to_find, length + 1)


def findPairs(lst, K, combo=2):
    if combo > len(lst):
        yield None
    find_combo = [pair for pair in itertools.combinations(lst, combo) if sum(pair) == K]
    if find_combo != []:
        yield find_combo
    else:
        yield from findPairs(lst, K ,combo + 1)

def part1(data, length):
    data_find_answer = []
    for i, d in enumerate(data):
        #print(i ,d)
        found_answer = True
        if i + length >= len(data) - 1:
            break
        for combos in itertools.combinations(data[i : i + length], 2):
            found_answer = True
            for x in range(i, i + length):
                if sum_list(combos, data[x]):
                    # print("FOUND: ", data[x])
                    data_find_answer.append(x)
            if sum_list(combos, data[i + length]):
                data_find_answer.append(i + length)

    range_data = set(range(length, len(data) - length))
    #print(range_data)
    data_find_answer = [d for d in data_find_answer if d >= length and d < len(data) - length ]
    answer = (range_data - set(data_find_answer))

    e = next(iter(answer))
    search = data[e]

    return search


if __name__ == '__main__':

    data = read_file('day9-input.txt')
    # print(data)
    #data =[35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
    data_find_answer = []

    length = 25

    #print(set(data_find_answer))
    search = part1(data, length)

    print("PART1:", search)
    print("-----")
    t = find_sum(data, search)

    #t = findPairs(data, search)
    print("T:", t)
    my_list = t
    print(my_list, min(my_list), max(my_list), min(my_list) + max(my_list))
    print("PART 2:", min(my_list) + max(my_list))

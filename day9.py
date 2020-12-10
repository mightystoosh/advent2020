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
    print(data)
    for i, d in enumerate(data):
        print(data[i: i + length])
        if sum(data[i: i + length]) == to_find:
            return min(data[i: i + length]), max(data[i:i + length])
        elif sum(data[i:i + length]) > to_find:
            continue
        else:
             find_sum(data[i: length + 1], to_find, length + 1)


import sys

def findPairs(lst, K, combo=2):
    if combo >= len(lst) -1:
        yield None
    find_combo = [pair for pair in itertools.combinations(lst, combo) if sum(pair) == K]
    if find_combo != []:
        yield find_combo
    else:
        yield from findPairs(lst, K ,combo + 1)
        #return findPairs(lst, K, combo + 1)

# def chunks(lst, n):
#     """Yield successive n-sized chunks from lst."""
#     for i in range(0, len(lst), n):
#         yield lst[i:i + n]

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


def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)


if __name__ == '__main__':

    data = read_file('day9-input.txt')
    # print(data)
    #data =[35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
    data_find_answer = []

    length = 25

    #print(set(data_find_answer))
    search = part1(data, length)

    print("PART1:", search)
    print("PART2:")
    #t = find_sum(data, search)

    #t = findPairs(data, search)
    #print(t)

    combo = 2

    data = data[0: data.index(search)]
    data = [d for d in data if d <= search/2]
    print(len(data))

    import pprint, time
    result = findPairs(data, search)
    #result = subset_sum(data, search)

    my_list = next(result)

    print(my_list, min(my_list), max(my_list), min(my_list) + max(my_list))
    #
    # t = None
    # splits = 10
    # while t is None:
    #     if splits >= len(data):
    #         break
    #     print("splits: ", splits)
    #     chunky = (list(chunks(data, splits)))
    #     for d in chunky:
    #         for c in range(2, splits):
    #             print(c)
    #             t = findPairs(data, search, c)
    #             if t:
    #                 break
    #         if t:
    #             break
    #         else:
    #             splits += 5
    #
    # print(t)

    # executor = concurrent.futures.ProcessPoolExecutor(10)
    # futures = [executor.submit(findPairs, data, search, combo) for combo in range(2, len(data))]
    # #print (len(futures))
    # concurrent.futures.wait(futures)



    #print(min(found) + max(found))
    # use data[e] and get a set of at least two numbers that add to this value

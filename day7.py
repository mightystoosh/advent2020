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

def create_bag_tree(data):
    master={}
    for bags in data:
        bag_info = bags.split(" contain ")
        #if bag_info[1] == "no other bags.":
        #    return master
        bag = bag_info[0].replace(' bags','')
        if bag not in master:
            master[bag] = []
            other_bags = bag_info[1].split(", ")
            for other in other_bags:
                t = re.match('[0-9]+ (.*) bag', other)
                if(t):
                    my_bag_new = t[1]
                    master[bag].append(my_bag_new.strip())
    return master

def create_bag_tree_with_counts(data):
    master={}
    for bags in data:
        bag_info = bags.split(" contain ")
        #if bag_info[1] == "no other bags.":
        #    return master
        bag = bag_info[0].replace(' bags','')
        if bag not in master:
            master[bag] = []
            other_bags = bag_info[1].split(", ")
            for other in other_bags:
                t = re.match('([0-9]+) (.*) bag', other)
                if(t):
                    my_bag_new = t[2]
                    master[bag].append({my_bag_new.strip(): t[1]})
    return master

def traverse_master(master, my_bag, ignored = [], count = 0):
    if master is None:
        return count
    for bag in master:
        if my_bag in master[bag]:
            if bag not in ignored:
                count += 1
            new_master = master.copy()
            del new_master[bag]
            ignored.append(bag)
            count += traverse_master(new_master, bag, ignored)
    return count

def count_bags(master, my_bag, ignored = [], count = 1):
    if master is None:
        return count
    if my_bag in master:
        for bag in master[my_bag]:
            key = list(dict(bag))[0]
            num = int(bag[key])
            new_master = master.copy()
            del new_master[my_bag]
            count += (num * count_bags(new_master, key))
    return count


data = read_file("day7-input.txt")
#print(data)

my_bag = 'shiny gold'

master = create_bag_tree(data)
print(master)

count = traverse_master(master, my_bag)
print("PART1: ", count)


data = read_file("day7-input.txt")
master = create_bag_tree_with_counts(data)
#print(master)
count = count_bags(master, my_bag) - 1

print("PART2: ", count)

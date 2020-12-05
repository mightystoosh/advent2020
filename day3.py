paths = []

def multiplyList(myList) :

    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x
    return result


def hit_tree(path, last_pos):
    orig = last_pos
    while last_pos > len(path) - 1:
        path = path + path
    if '#' == path[last_pos]:
        #print(orig, last_pos, path)
        return True

    return False

with open("day3-input.txt", 'r') as infile:
    while True:
        line = infile.readline()
        if not line:
            break
        line = line.strip()
        paths.append(line)

count_trees = 0
last_pos = 3
orig_path = paths
paths.pop(0)
for path in paths:
    if hit_tree(path, last_pos):
        count_trees += 1
    last_pos += 3


print(count_trees)


#PART2
print("")
print("PART2:")

paths = []
with open("day3-input.txt", 'r') as infile:
    while True:
        line = infile.readline()
        if not line:
            break
        line = line.strip()
        paths.append(line)

#paths = ["..##.......","#...#...#..",".#....#..#.","..#.#...#.#",".#...##..#.","..#.##.....",".#.#.#....#",".#........#","#.##...#...","#...##....#",".#..#...#.#"]
trees_product = []

slopes = [1, 3, 5, 7, 1]
slopes2 = [1, 1, 1, 1, 2]

for i, slope in enumerate(slopes):
    last_pos = slope
    count = 0
    count_trees = 0
    for path in paths:
        #print("slope is: ", slope, slopes2[i], "line: ", count)
        if count == 0 or count % slopes2[i] != 0:
            pass
        else:
            #print("NOT SKIPPED:", count)
            if hit_tree(path, last_pos):
                #print("PATH: ",last_pos, path[:last_pos] + 'O' + path[last_pos + 1:])
                count_trees += 1
            last_pos += slope
        count += 1
    trees_product.append(count_trees)

print (trees_product, multiplyList(trees_product))

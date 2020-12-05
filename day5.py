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

data = []

def seat_id(row, col):
    return row * 8 + col

def traverse_row(data, row, col, final_row=None, final_col=None):
    #print (data, row, col)
    if not data:
        return final_row[0], final_col[0]
    elif data[0] == "F":
        final_row = [row[0], int((row[1] +row[0]) / 2)]
        return traverse_row(data[1:], final_row, col, final_row, col)
    elif data[0] == "B":
        final_row = [int((row[1] + row[0]) / 2) + 1, row[1]]
        return traverse_row(data[1:], final_row, col, final_row, col)

    elif data[0] == "L":
        final_col = [col[0], int((col[1] +col[0]) / 2)]
        return traverse_row(data[1:], row,  final_col, row, final_col)
    elif data[0] == "R":
        final_col = [int((col[1] + col[0]) / 2) + 1, col[1]]
        return traverse_row(data[1:], row, final_col, row, final_col)

with open("day5-input.txt", 'r') as infile:
    while True:
        line = infile.readline()
        if not line:
            break
        line = line.strip()
        data.append(line)

#data = ['BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL']
final_seating_order = []
final_seating_order_id = []


for d in data:
    row = [0, 127]
    col = [0 , 7]
    final_row, final_col = traverse_row(d, row, col)
    final_seating_order.append([final_row,final_col])
    final_seating_order_id.append(seat_id(final_row,final_col))

#print(final_seating_order)
print("PART1: ",max(final_seating_order_id))


#print("PART2: ",sorted(final_seating_order_id))

count = 0
previous = 0
my_seat = 0

for previous, current in zip(sorted(final_seating_order_id), sorted(final_seating_order_id)[1:]):
    if current - previous != 1:
        print("PART2: ", current -1)


# for x in sorted(final_seating_order_id):
#     if count == 0:
#         previous = x
#         count += 1
#     elif (x - previous) != 1:
#         print("PART2: ",x - 1)
#         break
#     else:
#         previous = x
#         count += 1

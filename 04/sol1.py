from functools import reduce
from os import read


with open('input.txt') as data:
    input = data.read().split('\n\n')
    readNums = input[0].split(',')
    boards = input[1:-1]

def boardWin(rows, nums):
    # print(board)
    # rows = list(map(lambda x: list(filter(lambda y: y != '', x.split(' '))), board.split('\n')))
    # print('ROWS')
    # print(rows)
    columns = []
    length = len(rows[0])
    for i in range(0,length):
        column = []
        for row in rows:
            # print('ROW')
            # print(row)
            column.append(row[i])
        # print(column)
        columns.append(column)
    # print('COLS')
    # print(columns)
    options = rows + columns
    # print(options)
    completeLines = []

    for line in options:
        def isReadOut(lineNums, readOutNums):
            for num in lineNums:
                if num not in readOutNums:
                    return False
            return True

        if isReadOut(line, nums):
            completeLines.append(line)
    return completeLines


# print(boardWin(boards[0],['90', '92','15','83','25','3','88','13','50']))

def findFirstWin(boards, nums):
    for i in range(1, len(nums)):
        readOut = nums[0:i]
        # print(readOut)
        for board in boards:
            rows = list(map(lambda x: list(filter(lambda y: y != '', x.split(' '))), board.split('\n')))
            if(boardWin(rows, readOut)):
                return rows, readOut

def boardPoints(rows, readOut):
    unreadNums = []
    for row in rows:
        for num in row:
            if num not in readOut:
                unreadNums.append(num)
    return reduce(lambda a, b: int(a) + int(b), unreadNums) * int(readOut[-1])

def getFirstPoints(boards, nums):
    firstWin = findFirstWin(boards, nums)
    return boardPoints(firstWin[0], firstWin[1])

print(getFirstPoints(boards, readNums))
# print(findFirstWin(boards, readNums))
# print(readNums)
# def addNumToBoard(board, num):





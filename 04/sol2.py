from functools import reduce
from os import read


with open('input.txt') as data:
    input = data.read().split('\n\n')
    readNums = input[0].split(',')
    boards = input[1:-1]

def boardWin(rows, nums):
    columns = []
    length = len(rows[0])
    for i in range(0,length):
        column = []
        for row in rows:
            column.append(row[i])
        columns.append(column)
    options = rows + columns
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

def findLastWin(boards, nums):
    unfinishedBoards = []
    for i in range(1, len(nums)):
        readOut = nums[0:i]
        newUnfinBoards = []
        for board in boards:
            rows = list(map(lambda x: list(filter(lambda y: y != '', x.split(' '))), board.split('\n')))
            if(not boardWin(rows, readOut)):
                newUnfinBoards.append(board)
        if len(newUnfinBoards) > 0:
            unfinishedBoards = newUnfinBoards
        else:
            return unfinishedBoards, readOut

def boardPoints(rows, readOut):
    unreadNums = []
    for row in rows:
        for num in row:
            if num not in readOut:
                unreadNums.append(num)
    return reduce(lambda a, b: int(a) + int(b), unreadNums) * int(readOut[-1])

def getLastPoints(boards, nums):
    lastWin = findLastWin(boards, nums)
    print(lastWin[0][0])
    rows = list(map(lambda x: list(filter(lambda y: y != '', x.split(' '))), lastWin[0][0].split('\n')))
    return boardPoints(rows, lastWin[1])

# print(findLastWin(boards, readNums))
print(getLastPoints(boards, readNums))





#!/usr/bin/env python3

board = []
for i in range(8):
    r = list(input())
    board.append(r)
board = board[::-1]
for i in range(8):
    for j in range(8):
        if board[i][j]=="*":
            row = j + 97
            print(chr(row)+str(i+1))


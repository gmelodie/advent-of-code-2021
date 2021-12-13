from sys import stdin

def read_board():
    board = []
    is_marked = []
    for i in range(5):
        board.append([int(num) for num in input().split()])
        is_marked.append([False]*5)
    return (board, is_marked)


def mark_board(board, is_marked, number):
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                is_marked[i][j] = True


def is_bingo(is_marked):
    # check rows
    for i in range(5):
        if is_marked[i] == [True]*5:
            return True
    # check cols
    for j in range(5):
        col = [is_marked[i][j] for i in range(5)]
        if col == [True]*5:
            return True
    return False


def calculate_score(board, is_marked, last_drawn_number):
    score = 0
    for i in range(5):
        for j in range(5):
            if not is_marked[i][j]:
                score += board[i][j]
    return score*last_drawn_number


boards = [] # [(b1, marked1), ...]
drawn_numbers = [int(num) for num in input().split(',')]

for line in stdin: # ignore newlines
    boards.append(read_board())

# print(boards)
for number in drawn_numbers:
    for (board, is_marked) in boards:
        mark_board(board, is_marked, number)
        if is_bingo(is_marked):
            print(calculate_score(board, is_marked, number))
            exit(0)

print(boards)

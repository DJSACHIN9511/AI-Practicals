# Tic Tac Toe with A* Search (No external libraries)

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != '_' for row in board for cell in row])

def get_possible_moves(board, player):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                new_board = [row[:] for row in board]
                new_board[i][j] = player
                moves.append((new_board, (i, j)))
    return moves

def heuristic(board):
    score = 0
    lines = []

    # Rows and columns
    for i in range(3):
        lines.append([board[i][j] for j in range(3)])
        lines.append([board[j][i] for j in range(3)])

    # Diagonals
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    for line in lines:
        if line.count('X') == 2 and line.count('_') == 1:
            score += 10
        elif line.count('X') == 1 and line.count('_') == 2:
            score += 1
        elif line.count('O') == 2 and line.count('_') == 1:
            score -= 8
    return score

def a_star_ai_move(board):
    # 1. Check if AI can win in one move
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                test_board = [row[:] for row in board]
                test_board[i][j] = 'X'
                if check_winner(test_board, 'X'):
                    return test_board, (i, j)

    # 2. Check if Player can win in next move, and block it
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                test_board = [row[:] for row in board]
                test_board[i][j] = 'O'
                if check_winner(test_board, 'O'):
                    board[i][j] = 'X'
                    return board, (i, j)

    # 3. Use heuristic as fallback
    best_move = None
    best_score = -1000
    for next_state, move in get_possible_moves(board, 'X'):
        score = heuristic(next_state)
        if score > best_score:
            best_score = score
            best_move = (next_state, move)
    return best_move


def main():
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    print("Welcome to Tic Tac Toe (You are O, AI is X)")
    print_board(board)

    while True:
        # Player move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
                if board[row][col] == '_':
                    board[row][col] = 'O'
                    break
                else:
                    print("Cell already filled.")
            except:
                print("Invalid input. Try again.")

        print("Your Move:")
        print_board(board)

        if check_winner(board, 'O'):
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI move
        board, move = a_star_ai_move(board)
        print(f"AI plays at {move}:")
        print_board(board)

        if check_winner(board, 'X'):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()

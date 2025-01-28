import random
import os
import sys
import time
import threading
import keyboard  # Library for async interraction

# Play field sizes
WIDTH, HEIGHT = 20, 30

# Figures
SHAPES = [
    [[1, 1, 1, 1]],  # Line
    [[1, 1], [1, 1]],  # Square
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # L-reversed
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]]   # S
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board():
    return [[0] * WIDTH for _ in range(HEIGHT)]

def print_board(board, shape, shape_pos):
    temp_board = [row[:] for row in board]
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                temp_y, temp_x = shape_pos[1] + y, shape_pos[0] + x
                if 0 <= temp_y < HEIGHT and 0 <= temp_x < WIDTH:
                    temp_board[temp_y][temp_x] = cell

    for row in temp_board:
        print('|' + ''.join('#' if cell else ' ' for cell in row) + '|')
    print('-' * (WIDTH + 2))

def check_collision(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                new_x, new_y = off_x + x, off_y + y
                if (
                    new_x < 0 or
                    new_x >= WIDTH or
                    new_y >= HEIGHT or
                    (new_y >= 0 and board[new_y][new_x])
                ):
                    return True
    return False

def place_shape(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                board[off_y + y][off_x + x] = cell

def remove_complete_lines(board):
    removed_lines = 0
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    removed_lines = HEIGHT - len(new_board)
    for _ in range(removed_lines):
        new_board.insert(0, [0] * WIDTH)
    return new_board, removed_lines

def rotate_shape(shape):
    return [list(row) for row in zip(*shape[::-1])]

def game_loop():
    global board, current_shape, shape_position, game_over, lines_cleared, score

    while not game_over:
        time.sleep(0.3)  # Speed

        new_position = [shape_position[0], shape_position[1] + 1]
        if not check_collision(board, current_shape, new_position):
            shape_position = new_position
        else:
            place_shape(board, current_shape, shape_position)
            board, lines = remove_complete_lines(board)
            lines_cleared += lines
            score += lines * 10

            if lines_cleared >= 100:
                clear_console()
                print_board(board, current_shape, shape_position)
                print(f"Score: {score}, Lines Cleared: {lines_cleared}")
                choice = input("You have 100 lines passed, wish to continue? (y/n): ").strip().lower()
                if choice != 'y':
                    game_over = True
                    break
                lines_cleared = 0

            current_shape = random.choice(SHAPES)
            shape_position = [WIDTH // 2 - len(current_shape[0]) // 2, 0]

            if check_collision(board, current_shape, shape_position):
                game_over = True

        clear_console()
        print_board(board, current_shape, shape_position)
        print(f"Score: {score}, Lines Cleared: {lines_cleared}")

def handle_input():
    global shape_position, current_shape, game_over

    while not game_over:
        if keyboard.is_pressed('a'):
            new_position = [shape_position[0] - 1, shape_position[1]]
            if not check_collision(board, current_shape, new_position):
                shape_position = new_position
        elif keyboard.is_pressed('d'):
            new_position = [shape_position[0] + 1, shape_position[1]]
            if not check_collision(board, current_shape, new_position):
                shape_position = new_position
        elif keyboard.is_pressed('w'):
            new_shape = rotate_shape(current_shape)
            if not check_collision(board, new_shape, shape_position):
                current_shape = new_shape
        elif keyboard.is_pressed('s'):
            new_position = [shape_position[0], shape_position[1] + 1]
            if not check_collision(board, current_shape, new_position):
                shape_position = new_position
        time.sleep(0.05)  # Small delay filter for keyboard

def main():
    global board, current_shape, shape_position, game_over, lines_cleared, score

    board = create_board()
    current_shape = random.choice(SHAPES)
    shape_position = [WIDTH // 2 - len(current_shape[0]) // 2, 0]  # Begin position
    game_over = False
    lines_cleared = 0
    score = 0

    input_thread = threading.Thread(target=handle_input, daemon=True)
    input_thread.start()

    game_loop()

    clear_console()
    print("Game is finished! Thanks wathing")
    print(f"Your score: {score}")

if __name__ == "__main__":
    main()

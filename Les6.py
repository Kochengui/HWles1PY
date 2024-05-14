import sys
from datetime import datetime

def check_date(input_date):
    try:
        date_obj = datetime.strptime(input_date, '%Y-%m-%d')
        print(f"Дата {input_date} корректна.")
    except ValueError:
        print(f"Дата {input_date} некорректна. Пожалуйста, введите дату в формате YYYY-MM-DD.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Пожалуйста, введите дату для проверки в формате YYYY-MM-DD.")
    else:
        date_to_check = sys.argv[1]
        check_date(date_to_check)




def is_safe(board):
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                return False
    return True

def check_queens_attack(queens_positions):
    if len(queens_positions) != 8:
        return False
    
    return is_safe(queens_positions)

if __name__ == "__main__":
    queens_positions = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]
    
    board = []
    for position in queens_positions:
        board.append(position[1])

    result = check_queens_attack(board)
    
    if result:
        print("Ферзи не бьют друг друга.")
    else:
        print("Ферзи бьют друг друга.")



import random

def generate_random_queens():
    queens_positions = []
    for _ in range(8):
        queens_positions.append((random.randint(1, 8), random.randint(1, 8)))
    
    return queens_positions

def check_and_print_successful_arrangements():
    successful_arrangements_found = 0
    while successful_arrangements_found < 4:
        queens_positions = generate_random_queens()
        
        board = []
        for position in queens_positions:
            board.append(position[1])

        if check_queens_attack(board):
            print("Успешная расстановка ферзей:")
            for i, position in enumerate(queens_positions):
                print(f"Ферзь {i+1}: {position}")
            print()
            successful_arrangements_found += 1

if __name__ == "__main__":
    check_and_print_successful_arrangements()

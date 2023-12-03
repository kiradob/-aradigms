def print_board(board):
    # Функция для печати игрового поля
    for row in board:
        print(' | '.join(row))
        print('-' * 9)


def check_winner(board):
    # Проверка наличия победителя
    rows = board + list(zip(*board)) + [[board[i][i] for i in range(3)]] + [[board[i][2-i] for i in range(3)]]
    for row in rows:
        if all(cell == 'X' for cell in row):
            return 'X'
        elif all(cell == 'O' for cell in row):
            return 'O'
    return None


def play_game():
    # Основная функция игры
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Ходит игрок {current_player}")
        row = int(input("Введите номер строки (от 1 до 3): ")) - 1
        col = int(input("Введите номер столбца (от 1 до 3): ")) - 1

        if board[row][col] == ' ':
            board[row][col] = current_player
            winner = check_winner(board)

            if winner:
                print_board(board)
                print(f"Победил игрок {winner}!")
                break
            elif all(cell != ' ' for row in board for cell in row):
                print_board(board)
                print("Ничья!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Эта ячейка уже занята!")
            continue


play_game()



# В данном коде были использованы следующие парадигмы:

# Императивное программирование: Используется для описания последовательности шагов игры и логики проверки победы. 
# Цикл while True используется для основного цикла игры, условные операторы if/elif/else используются для проверки условий 
# и принятия решений.

# Структурное программирование: Код организован в виде функций, где каждая функция выполняет конкретную задачу. 
# Функции print_board, check_winner и play_game разделены по функциональности и отвечают за отображение игрового поля, 
# проверку победителя и основную логику игры соответственно.

# Функциональное программирование: Функции check_winner и print_board являются чистыми функциями, которые получают входные 
# данные и возвращают результат без побочных эффектов.

# Использование списка: Поле игры представлено в виде двумерного списка (board), где каждый элемент представляет ячейку игрового поля.

# Использование циклов: Цикл for row in board используется для итерации по каждой строке игрового поля при печати его состояния. 
# Также используются циклы for для создания итерируемых объектов в функции check_winner.

# Использование условных операторов: Условные операторы if/elif/else используются для проверки различных условий, например, 
# проверка победителя и проверка наличия свободной ячейки для хода игрока.

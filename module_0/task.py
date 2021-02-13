import numpy as np
from math import floor, ceil

def game_core_binary(number):
    '''Приравниваем еденице, т.к. можно считать, что первая проверка делается вне цикла'''
    count = 1

    left = 1
    right = 100
    current = (left + right) / 2 # текущее положение бинарного сечения

    '''Проверяем сразу и верхнее и нижнее целое от текущего положения сечения, 
    для случаев когда оно дробное'''
    while ceil(current) != number and floor(current) != number:
        if current < number:
            left = current
        else:
            right = current

        current = (left + right) / 2
        count += 1

    '''Почти всегда надо будет добавлять ещё одну проверку, т.к. мы не наем, целое сверху, или снизу наше искомое'''
    if ceil(current) != floor(current):
        count += 1

    return count


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)

score_game(game_core_binary)
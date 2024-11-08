# coding=utf-8
import random


def guessing_game(max_tries=None):
    a, b = 0, 10
    ans = random.randint(a, b)

    n_tries = 0

    # get rid of `while True`
    while user_guess := input(f'input a number in [{a}, {b}]: '):
        try:
            user_ans = int(user_guess)
        except ValueError:
            print(f'Invalid input: {user_guess}, try another input.')
            continue

        n_tries += 1
        if user_ans == ans:
            print('Just right')
            break
        elif user_ans > ans:
            print('Too high')
        else:
            print('Too low')

        if max_tries is not None and n_tries >= max_tries:
            print(f'You have tried {n_tries} times, exit now...')
            break


if __name__ == '__main__':
    guessing_game(max_tries=None)

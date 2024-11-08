# coding=utf-8


def run_time():
    times = []
    while True:
        user_input = input(f'Enter 10 km run time: ').strip()
        if not user_input:
            break

        try:
            user_ans = float(user_input)
        except ValueError:
            print(f'Invalid input: `{user_input}`, try another input.')
            continue

        times.append(user_ans)

    msg = 'Average of {:.2f} over {} runs'
    n_runs = len(times)
    avg = 0.0
    if times:
        avg = sum(times) / len(times)
    return msg.format(avg, n_runs)


if __name__ == '__main__':
    print(run_time())

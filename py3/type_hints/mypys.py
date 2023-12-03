# coding=utf-8
# mypy mypys.py
# Success: no issues found in 1 source file

# mypy --disallow-untyped-defs mypys.py
# mypys.py:5: error: Function is missing a type annotation  [no-untyped-def]
# Found 1 error in 1 file (checked 1 source file)

# or --disallow- incomplete-defs


def show_count(n: int, thing: str, plural: str | None = None) -> str:
    if n == 1:
        return f'1 {thing}'
    count_text = str(n) if n else 'no'
    if not plural:
        plural = f'{thing}s'
    return f'{count_text} {plural}'


if __name__ == '__main__':
    print(show_count(2, 'apple'))
    # mypy: Too many arguments for "show_count"
    print(show_count(2, 'index', 'indices'))

# coding=utf-8
from typing import Callable


def update(probe: Callable[[], float],
           display: Callable[[float], None]) -> None:
    temperature = probe()
    display(temperature)


def probe_ok() -> int:
    return 42


def display_wrong(temperature: int) -> None:
    print(hex(temperature))


def display_ok(temperature: complex) -> None:
    print(temperature)


if __name__ == '__main__':
    update(probe_ok, display_wrong)
    update(probe_ok, display_ok)

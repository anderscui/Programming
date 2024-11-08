# coding=utf-8


def hex_output(hex_text: str):
    if hex_text is None:
        return None
    hex_text = hex_text.strip()

    result = 0
    for power, digit in enumerate(reversed(hex_text)):
        # can replace `int` with `ord`
        c_val = int(digit, base=16)
        result +=  c_val * (16 ** power)
    return result


if __name__ == '__main__':
    assert hex_output('') == 0
    assert hex_output('11') == 17
    assert hex_output('50') == 80
    assert hex_output('100') == 256
    assert hex_output('2010') == 8208


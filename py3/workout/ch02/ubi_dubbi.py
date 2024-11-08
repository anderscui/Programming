# coding=utf-8


def ubi_dubbi(word: str):
    if not word:
        return word
    first_upper = word[0].isupper()
    parts = []
    for c in word:
        if c.lower() in 'aeiou':
            parts.append(f'ub{c}')
        else:
            parts.append(c)
    result = ''.join(parts)
    if first_upper:
        result = result.capitalize()
    return result


if __name__ == '__main__':
    assert ubi_dubbi('milk') == 'mubilk'
    assert ubi_dubbi('Milk') == 'Mubilk'
    assert ubi_dubbi('octopus') == 'uboctubopubus'
    assert ubi_dubbi('Octopus') == 'Uboctubopubus'
    assert ubi_dubbi('elephant') == 'ubelubephubant'

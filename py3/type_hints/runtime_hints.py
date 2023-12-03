# coding=utf-8
import inspect


def clip(text: str, max_len: int = 80) -> 'str':
    return text[:max_len]


if __name__ == '__main__':
    # return -> 'str'
    print(clip.__annotations__)
    # return -> str
    print(inspect.get_annotations(clip, eval_str=True))

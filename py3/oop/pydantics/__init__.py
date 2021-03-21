# coding=utf-8
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'Jane Doe'


if __name__ == '__main__':
    user1 = User(id=1)
    print(user1)
    print(user1.__fields_set__)
    print(user1.dict())
    print(user1.json())
    print(user1.schema())

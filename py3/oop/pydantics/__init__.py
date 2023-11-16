# coding=utf-8
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = 'Jane Doe'


if __name__ == '__main__':
    user1 = User(id=1)
    print(user1)
    print(user1.model_fields_set)
    print(user1.model_dump())
    print(user1.model_dump_json())
    print(user1.model_json_schema())

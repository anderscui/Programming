# coding=utf-8
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = 'Jane Doe'


if __name__ == '__main__':
    # id is required.
    user1 = User(id=1)
    assert user1.id == 1

    user1 = User(id='123')
    assert (user1.id, user1.name) == (123, 'Jane Doe')
    assert user1.model_fields_set == {'id'}

    user2 = User(id=1, name='andersc')
    assert user2.model_fields_set == {'name', 'id'}
    assert user2.model_dump() == {'id': 1, 'name': 'andersc'}

    # json string
    print(user1.model_dump_json())
    # json Schema
    print(user1.model_json_schema())

    user3 = user2.model_copy(update={'id': 11}, deep=True)
    assert user3.model_dump() == {'id': 11, 'name': 'andersc'}

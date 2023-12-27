# coding=utf-8
from pydantic import BaseModel, ValidationError
from typing import TypeVar, Generic

DataT = TypeVar('DataT')


class DataModel(BaseModel):
    numbers: list[int]
    people: list[str]


class Response(BaseModel, Generic[DataT]):
    data: DataT | None = None


data = DataModel(numbers=[1, 2, 3], people=['anders'])

print(Response[int](data=1))
print(Response[str](data='value'))
print(Response[DataModel](data=data))

try:
    resp = Response[int](data='value')
except ValidationError as e:
    print(e)

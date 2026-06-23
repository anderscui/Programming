# coding=utf-8
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


if __name__ == '__main__':
    h1 = Hero(name='Pond', secret_name='Dive Wilson')
    h2 = Hero(name='Spider-Boy', secret_name='Pedro Parqueador')
    h3 = Hero(name='Rusty-Man', secret_name='Tommy Sharp', age=20)

    engine = create_engine('sqlite:///database.db')
    # # create all tables
    # SQLModel.metadata.create_all(engine)
    # with Session(engine) as session:
    #     session.add(h1)
    #     session.add(h2)
    #     session.add(h3)
    #     session.commit()

    with Session(engine) as session:
        stat = select(Hero).where(Hero.name == 'Rusty-Man')
        hero = session.exec(stat).first()
        print(hero.name)

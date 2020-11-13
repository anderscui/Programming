# coding=utf-8
import asyncio
import asyncpg
import datetime
from concurrency.asyncio_book.pg_util import Database


async def demo(conn: asyncpg.Connection):
    await conn.execute('''CREATE TABLE users(
        id serial PRIMARY KEY,
        name text,
        dob date
        )'''
    )

    async def get_row():
        return await conn.fetchrow('SELECT * FROM users WHERE name = $1', 'Bob')

    pk = await conn.fetchval('Insert Into users (name, dob) VALUES ($1, $2) '
                             'RETURNING id', 'Bob', datetime.date(1984, 1, 1))
    print('After INS:', await get_row())

    await conn.execute('UPDATE users SET dob = $1 WHERE id = 1', datetime.date(1985, 2, 1))
    print('After UPD:', await get_row())

    await conn.execute('DELETE FROM users where id = 1')
    print('After DEL:', await get_row())


async def main():
    async with Database('test', owner=True) as conn:
        await demo(conn)


if __name__ == '__main__':
    asyncio.run(main())

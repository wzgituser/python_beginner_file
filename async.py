import asyncio

async def main():
    print('a')
    await asyncio.sleep(5)
    await func_two()
    print('b')


async def func_two():
    print('1')
    await asyncio.sleep(2)
    print('2')


asyncio.run(main())
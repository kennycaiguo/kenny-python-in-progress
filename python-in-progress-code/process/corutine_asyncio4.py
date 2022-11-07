import asyncio
import functools


def callback(args, *, kwargs="default"):
    print(f'普通函数做回调函数获取参数{args},{kwargs}')


async def main(loop):
    print('注册callback')
    loop.call_soon(callback, 1)
    wrapped = functools.partial(callback, kwargs='not default')
    loop.call_soon(wrapped, 2)
    await asyncio.sleep(0.25)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        loop.close()

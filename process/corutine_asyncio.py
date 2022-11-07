import asyncio


async def foo():
    print("这是一个协程")


def main():
    loop = asyncio.get_event_loop()
    try:
        print("协程开始执行。。。")
        coro = foo()
        print('进入循环事件')
        loop.run_until_complete(coro)
    finally:
        print('关闭循环事件')
        loop.close()


if __name__ == '__main__':
    main()

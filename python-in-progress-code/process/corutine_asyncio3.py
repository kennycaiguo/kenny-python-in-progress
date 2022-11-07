import asyncio


async def num(n):
    print(f"当前的数字是:{n}")
    await asyncio.sleep(n)
    print(f"等待时间:{n}")


async def main():
    tasks = [num(i) for i in range(5)]  # 协程列表
    # await asyncio.gather(*tasks) #有序并发
    await asyncio.wait(tasks)  # 并发运行协程列表的协程


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()

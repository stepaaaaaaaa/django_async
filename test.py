import asyncio

async def hello():
    await asyncio.sleep(3)
    return "Hello"

async def world():
    await asyncio.sleep(3)
    return "World"

async def thenia():
    await asyncio.sleep(3)
    return "Thenia"

async def krut():
    await asyncio.sleep(3)
    return "Krut"

async def main():
    results = await asyncio.gather(hello(), world(), thenia(), krut())
    print(list(results))

asyncio.run(main())

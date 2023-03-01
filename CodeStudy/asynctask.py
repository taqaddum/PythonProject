import asyncio
import nest_asyncio
nest_asyncio.apply()


async def func1():
    await asyncio.sleep(2)
    print('func1 done')

async def func2():
    await asyncio.sleep(1)
    print('func2 done')

async def main():
    tasks = {asyncio.create_task(func1()), asyncio.create_task(func2())}
    done, pending = await asyncio.wait(tasks)
    return done, pending

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()



if __name__=="__main__":
    # done, pending = asyncio.run(main())
    # print(done, pending, sep='\n')
    asyncio.run(tcp_echo_client('Hello World!'))

import asyncio
from datetime import datetime


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i+1} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = start_strongman('Pasha', 3)
    task2 = start_strongman('Denis', 4)
    task3 = start_strongman('Apollon', 5)

    await task1
    await task2
    await task3

time_start = datetime.now()
asyncio.run(start_tournament())
time_end = datetime.now()
time_res = time_end - time_start
print('Время соревнования:', time_res)

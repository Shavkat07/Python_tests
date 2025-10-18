import asyncio
import random
"""    --------------------- 1 - task ---------------------------  """

#
# async def say_hello():
#     await asyncio.sleep(2)
#     print("Hello async World!")
#
#

# asyncio.run(say_hello())

"""    --------------------- 2 - task ---------------------------  """


# import time
# async def task1():
#     print(time.time())
#     print("Task 1! Start message")
#     await asyncio.sleep(2)
#     print(time.time())
#     print("Task 1! Finish message")
#
# async def task2():
#     print(time.time())
#     print("Task 2! Start message")
#     await asyncio.sleep(2)
#     print(time.time())
#     print("Task 2! Finish message")
#
# async def task3():
#     print(time.time())
#     print("Task 3! Start message")
#     await asyncio.sleep(2)
#     print(time.time())
#     print("Task 3! Finish message")
#
# async def main():
#     results = await asyncio.gather(task1(), task2(), task3())
#     return results
#
#
# print(asyncio.run(main()))


"""    --------------------- 3 - task ---------------------------  """


# async def fetch_data(url) -> str:
#     print(f"Fetching data from {url}")
#     random_num = random.randint(1, 3)
#     print(f"Random number is {random_num}")
#     await asyncio.sleep(random_num)
#     return f"Data from {url}"
#
#
# async def main():
#     urls = ["api/user", "api/product", "api/order"]
#     a = [fetch_data(urls[i]) for i in range(3)]
#     results = await asyncio.gather(*a)
#     return results
# print(asyncio.run(main()))

"""    --------------------- 4 - task ---------------------------  """




"""    --------------------- 5 - task ---------------------------  """
"""    --------------------- 6 - task ---------------------------  """
"""    --------------------- 7 - task ---------------------------  """
"""    --------------------- 8 - task ---------------------------  """
"""    --------------------- 9 - task ---------------------------  """
"""    --------------------- 10 - task ---------------------------  """
"""    --------------------- 11 - task ---------------------------  """

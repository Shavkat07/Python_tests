import time
import asyncio

async def download_file(file_id):
    print("Downloading file", file_id)
    await asyncio.sleep(2)
    print("Downloaded file", file_id)


async def main():
    start=time.time()

    tasks= [download_file(i) for i in range(3)]

    end=time.time()

    print("--- %s seconds ---" % (end - start))

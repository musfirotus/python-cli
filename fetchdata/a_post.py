import asyncio
import aiohttp
import time

urls = 'https://jsonplaceholder.typicode.com/posts'

async def fetch(urls):
    async with aiohttp.ClientSession as session:
        async with session.get(urls) as resp:
            print(resp.status)
    
async def get_title(urls):
    start = time.time()
    print(f"started at {time.strftime('%X')}")
    
    list_tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(url))
        list_tasks.append(task)
        
    for task in list_tasks:
        await task
    
    end = time.time()
    print(f"Finished at {time.strftime('%X')}")
    print(f"Total time: {round(int(end - start))}")
    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(run_task(list_url))
    loop.run_until_complete(get_title(urls))
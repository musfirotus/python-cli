import aiohttp
import asyncio
import time
import json
from Fetch import Fetcher as fetcher

api_key = '77caa6be65528227fe570a7b767f7dce'
id_keanu = 6384
id_robert = 3223
id_tom = 1136406
url_keanu = f'https://api.themoviedb.org/3/person/{id_keanu}/movie_credits?api_key={api_key}&language=en-US'
url_robert = f'https://api.themoviedb.org/3/person/{id_robert}/movie_credits?api_key={api_key}&language=en-US'
url_tom = f'https://api.themoviedb.org/3/person/{id_tom}/movie_credits?api_key={api_key}&language=en-US'

async def fetch_keanu():
    start = time.time()
    print(f"started at {time.strftime('%X')}")
    
    # Keanu Reeves
    html = await fetcher.get(url_keanu)
    loads = json.loads(html)
    print(json.dumps(loads, indent=4))
    
    end = time.time()
    print(f"Finished at {time.strftime('%X')}")
    print(f"Total time: {round(int(end - start))}")
    
async def fetch_dua():
    start = time.time()
    print(f"started at {time.strftime('%X')}")
    
    # Robert Downey
    html2 = await fetcher.get(url_robert)
    loads2 = json.loads(html2)
    print(json.dumps(loads2, indent=4))
    
    # Tom Holland
    html3 = await fetcher.get(url_tom)
    loads3 = json.loads(html3)
    print(json.dumps(loads3, indent=4))
    
    end = time.time()
    print(f"Finished at {time.strftime('%X')}")
    print(f"Total time: {round(int(end - start))}")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(fetch_keanu())
    loop.run_until_complete(fetch_dua())
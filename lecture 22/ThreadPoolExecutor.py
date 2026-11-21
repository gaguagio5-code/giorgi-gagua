import threading
import time
from concurrent.futures import ThreadPoolExecutor

import requests

URL = "https://jsonplaceholder.typicode.com/posts"
POST_IDS = range(1, 101)          

def fetch_post(post_id):
    """Sends a GET request to /posts/<post_id> and returns the status code."""
    response = requests.get(f"{URL}/{post_id}", timeout=10)
    return response.status_code

def run_with_threads():
    threads = []
    for post_id in POST_IDS:
        thread = threading.Thread(target=fetch_post, args=(post_id,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def run_with_pool():
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(fetch_post, POST_IDS))
    return results


if __name__ == "__main__":
    start_time = time.time()
    run_with_threads()
    threads_time = time.time() - start_time
    print(f"100 threads:{threads_time:.2f} s")

    start_time = time.time()
    results = run_with_pool()
    pool_time = time.time() - start_time
    print(f"ThreadPool (10 workers): {pool_time:.2f} s")

    print(f"\nPool results: {results.count(200)} of {len(results)} requests returned 200")
import threading
import time

import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_post(post_id):
    response = requests.get(f"{URL}/{post_id}", timeout=10)
    print(f"Post {post_id}: status {response.status_code}")


if __name__ == "__main__":
    start_time = time.time()

    threads = []
    for post_id in range(1, 101):            
        thread = threading.Thread(target=fetch_post, args=(post_id,))
        threads.append(thread)
        thread.start()                     

    for thread in threads:
        thread.join()                       

    total_time = time.time() - start_time
    print(f"\n100 requests finished in {total_time:.2f} seconds")
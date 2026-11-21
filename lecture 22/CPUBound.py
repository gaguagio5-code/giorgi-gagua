import time
from multiprocessing import Pool, cpu_count

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

def product_range(start_end):
    start, end = start_end         
    result = 1
    for i in range(start, end + 1):
        result = result * i
    return result

def parallel_factorial(n, processes):
    size = n // processes
    pieces = []
    for p in range(processes):
        start = p * size + 1
        end = (p + 1) * size
        if p == processes - 1:     
            end = n
        pieces.append((start, end))

    with Pool(processes) as pool:
        partial_results = pool.map(product_range, pieces)

    result = 1
    for part in partial_results:
        result = result * part
    return result

if __name__ == "__main__":
    number = 100000
    processes = cpu_count()        

    start_time = time.time()
    answer_1 = factorial(number)
    single_time = time.time() - start_time
    print("Single process:", round(single_time, 2), "seconds")

    start_time = time.time()
    answer_2 = parallel_factorial(number, processes)
    multi_time = time.time() - start_time
    print("Multiprocessing with", processes, "processes:", round(multi_time, 2), "seconds")

    print("Same answer:", answer_1 == answer_2)
    print("Speedup:", round(single_time / multi_time, 2), "x")
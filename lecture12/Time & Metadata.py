import time
from functools import wraps


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Running {func.__name__}... Executed in {elapsed:.2f} seconds.")
        return result
    return wrapper


@log_execution
def slow_add(a, b):
    """Adds two numbers after a 1-second delay."""
    time.sleep(1)
    return a + b


result = slow_add(2, 3)
print(result)               # 5
print(slow_add.__name__)    # slow_add
print(slow_add.__doc__)     # Adds two numbers after a 1-second delay.
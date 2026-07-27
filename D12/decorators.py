import time
from functools import wraps

def timer(unit="ms"):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = fn(*args, **kwargs)
            end = time.perf_counter()
            cost = end - start
            factor = 1000 if unit == "ms" else 1
            print(f"{fn.__name__} 耗时 {cost*factor:.2f} {unit}")
            return result
        return wrapper
    return decorator

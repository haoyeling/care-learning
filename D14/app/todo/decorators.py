import time
from functools import wraps

def timer(unit="ms"):
    def decorator(fn):
        #wraps保证函数名不被吃掉
        @wraps(fn)
        #args单个参数或者元组，*args拆开元组，分成几个参数；**kwarges关键字参数，打包成字典
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

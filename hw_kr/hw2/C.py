import random
import time
import functools

def timeout(rps):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **argv):
            lastused = time.time()
            result = func(*args, **argv)
            if (time.time() - lastused < 1/rps):
                time.sleep((-time.time() + lastused + 1/rps))
            return result
        return wrapper
    return decorator

   
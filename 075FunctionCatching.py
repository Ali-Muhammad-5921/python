from functools import lru_cache
import time

@lru_cache()   # it memoizes the vlaue not memorize memoize means to store the value of a computation so it can be subsequently called without performing the computation.
def fx(n):
    time.sleep(5)
    return n*2

print(fx(10))
print('Done for 10')
print(fx(25))
print('Done for 25')
print(fx(10))
print('Done for 10')
print(fx(25))
print('Done for 25')
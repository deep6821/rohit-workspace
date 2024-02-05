"""
Memoization is a way of caching the results of a function call. If a function is memoized, evaluating
it is simply a matter of looking up the result you got the first time the function  was  called  with
those parameters.

This is recorded in the memoization cache. If the lookup fails, that’s because the function has never been
called with those parameters. Only then do you need to run the function itself.

------------------------------------------------------------------------------
Memoization only makes sense if the function is deterministic, or you can live with the result being out of
date.

But if the function is expensive, memoization can result in a massive speedup. You’re trading the
computational complexity of the function for that of lookup.
"""
import functools


# 1. Memoization by hand: misusing a default parameter
# The trick here is that cache is a keyword parameter of the function. Python evaluates keyword parameters
# once and only once, when the function is imported.
# This means that if the keyword parameter is mutable (which a dictionary is), then it only  gets
# initialized once. This is often the cause of subtle bugs, but in this case we take advantage of
# it by  mutating the keyword parameter. The changes we make (i.e. populating the cache) don’t get
# wiped out by cache={} in the function definition, because that expression doesn’t get evaluated again.
def fib_default_memoized(n, cache={}):
    print("\n======================")
    print("Cache: ", cache)
    if n in cache:
        ans = cache[n]
    elif n <= 2:
        ans = 1
        cache[n] = ans
    else:
        ans = fib_default_memoized(n - 2) + fib_default_memoized(n - 1)
        cache[n] = ans

    return ans


# 2. Memoization by hand: objects
# 3. Memoization by hand: using global
# 4. An aside: decorators
def memoize(func):
    cache = func.cache = {}
    @functools.wraps(func)
    def memoized_func(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return memoized_func


@memoize
def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    else: return fibonacci(n - 1) + fibonacci(n - 2)


# 5. functools.lru_cache
@functools.lru_cache()
def fib_lru_cache(n):
    if n < 2:
        return n
    else:
        return fib_lru_cache(n - 2) + fib_lru_cache(n - 1)


# print(fib_default_memoized(9))
# print(fib_lru_cache(9))
# print(fibonacci(9))

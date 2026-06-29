
_cache = {}

def fibonacci(n):
    if n in _cache:
        return _cache[n]

    if n <= 1:
        return n

    _cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return _cache[n]
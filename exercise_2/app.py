from time import time


def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 2) + fib(n - 1)


n = 35
start = time()
f = fib(n)
end = time()

print(f"fib({n}) = {f}")
print(f"fib({n}) took {end - start} seconds")

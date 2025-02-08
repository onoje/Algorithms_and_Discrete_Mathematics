import time


# Example list = [0, 1, 1, 2, 3, 5, 8, ...]
def recursive_fibonacci(n):
    if n < 0:
        return "ERROR"
    elif n <= 1:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def iterative_fibonacci(n):
    a = 0
    b = 1
    if n > 0:
        for i in range(n):
            a, b = b, a + b
        return a
    else:
        return "ERROR"


start = time.time() * 10**12
print(recursive_fibonacci(10))
end = time.time() * 10**12
print(end - start, "Pico Second")

start = time.time() * 10**12
print(iterative_fibonacci(10))
end = time.time() * 10**12
print(end - start, "Pico Second")

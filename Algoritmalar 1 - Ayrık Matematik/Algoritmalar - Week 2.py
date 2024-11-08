import time

number_values = [10, 100, 1000, 10000]


def sum_with_loop(array):
    s = 0
    x = 0
    while x < len(array):
        s = s + array[x]
        x = x + 1
    return s


def sum_with_builtin(array):
    s = sum(array)
    return s


for values in number_values:
    numbers = []
    for i in range(1, 101):
        for j in range(values):
            numbers.append(i)

    print(f"Array Size: ", len(numbers))

    start = time.time() * 10 ** 12
    print("Sum With Loop: ", sum_with_loop(numbers))
    end = time.time() * 10 ** 12
    print("Pico Second:", end - start)

    start = time.time() * 10 ** 12
    print("Sum With Builtin: ", sum_with_builtin(numbers))
    end = time.time() * 10 ** 12
    print("Pico Second:", end - start)

    if sum_with_loop(numbers) == sum_with_builtin(numbers):
        print("Match")
    print("------------------------------")

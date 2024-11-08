def integer_overflow():
    MAX_INT_8 = 127
    MIN_INT_8 = -128
    value = MAX_INT_8
    print(f"Initial value: {value}")

    value += 1
    if value > MAX_INT_8:
        value = MIN_INT_8 - (MAX_INT_8 - value + 1)
    print(f"Value after overflow: {value}")

    value = MIN_INT_8
    print(f"Initial value for underflow: {value}")

    value -= 1
    if value < MIN_INT_8:
        value = MAX_INT_8 + (-MIN_INT_8 + value + 1)
    print(f"Value after underflow: {value}")


integer_overflow()
print("----------------------------------------")

















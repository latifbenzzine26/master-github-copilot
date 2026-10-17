import math

def calculate_area(radius):     

    return math.pi * radius ** 2


def fibonacci(n):   
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    merged = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            value = a[i]
            i += 1
        else:
            value = b[j]
            j += 1

        if not merged or merged[-1] != value:
            merged.append(value)

    while i < len(a):
        value = a[i]
        i += 1
        if not merged or merged[-1] != value:
            merged.append(value)

    while j < len(b):
        value = b[j]
        j += 1
        if not merged or merged[-1] != value:
            merged.append(value)

    return merged


zzz = [q for q in range(2, 100) if all(q % w for w in range(2, int(q**0.5) + 1))]
print(zzz[:10])




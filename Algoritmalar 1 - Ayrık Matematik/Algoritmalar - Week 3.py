numbers = [1, 2, 3, 4, 5, 6, 7]


def iterative_ternary_search(numbers, n):
    first = 0
    last = len(numbers) - 1
    while last >= first:
        mid1 = first + (last - first) // 3
        mid2 = last - (last - first) // 3

        if numbers[mid1] == n:
            return mid1
        if numbers[mid2] == n:
            return mid2

        if n < numbers[mid1]:
            last = mid1 - 1
        elif n > numbers[mid2]:
            first = mid2 + 1
        else:
            first = mid1 + 1
            last = mid2 - 1
    return False


first = 0
last = len(numbers) - 1


def recursive_ternary_search(numbers, first, last, n):
    if last >= first:
        mid1 = first + (last - first) // 3
        mid2 = last - (last - first) // 3

        if numbers[mid1] == n:
            return mid1
        if numbers[mid2] == n:
            return mid2

        if n < numbers[mid1]:
            return (recursive_ternary_search(numbers, first, mid1 - 1, n))
        elif n > numbers[mid2]:
            return (recursive_ternary_search(numbers, mid2 + 1, last, n))
        else:
            return (recursive_ternary_search(numbers, mid1 + 1, mid2 - 1, n))
    return False


print("iterative search: ", (iterative_ternary_search(numbers, 4)))
print("recursive search: ", (recursive_ternary_search(numbers, first, last, 4)))


#......................................................................................


number = int(input("sayı giriniz: "))


def iterative_sum(number):
   x = 0
   while number > 0:
       x = x + number
       number = number - 1
   return (x)


def recursive_sum(number):
   if number == 1:
       return (1)
   else:
      return( number + recursive_sum(number - 1))

print("iterative sum: ", (iterative_sum(number)))
print("recursive sum: ", (recursive_sum(number)))
def comb_sort(array):
    gap = len(array)
    swapped = True

    while gap > 1 or swapped:
        if gap > 1:
            gap = int(gap / 1.3)

        swapped = False

        for i in range(0, len(array) - gap):
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                swapped = True
      
    return array

array= [100,23,35,14,65,46,-7,8,912,-10]
print(comb_sort(array))
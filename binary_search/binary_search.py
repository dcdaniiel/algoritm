def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int((low + high) / 2)
        hit = arr[mid]

        print("HISTORY: ", mid)
        if hit == item:
            return mid
        if hit > item:
            high = mid - 1
        else:
            low = mid + 1

    return None



print(binary_search(range(0, 10000), 7689))

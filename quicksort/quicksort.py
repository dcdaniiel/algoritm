def sum(arr):
    if len(arr) == 0:
        return 0

    num = arr.pop()

    return num + sum(arr)


print("SUM", sum([2,4,6]))

def count(arr, l=0):

    if not len(arr):
        return l

    arr.pop()

    return count(arr, l+1 )



print("COUNT: ", count([1,2,3]))


def high(arr, n=0):

    if not len(arr):
        return n

    f = arr.pop()

    if f > n:
        return high(arr, f)
    else:
        return high(arr, n)

print("HIGH: ", high([10, 2, 8, 20, 20]))



def binary_search(arr, item, low=False, high=False):

    low = low or 0
    high = high or len(arr) - 1

    mid = int((low + high) / 2)
    hit = arr[mid]

    print("HISTORY: ", hit)

    if hit == item:
        return mid

    if hit > item:
        return binary_search(arr, item, low, mid)
    else:
        return binary_search(arr, item, mid, high)


print("BINARY SEARCH: ", binary_search(range(1, 100000), 9))


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivo = arr[0]
        menor = [ i for i in arr[1:] if i <= pivo]
        maior = [ i for i in arr[1:] if i > pivo]
        print("PIVO", pivo,  "MENOR: ", menor, "MAIOR: ", maior )

        return quicksort(menor) + [pivo] + quicksort(maior)

print("QUICKSORT: ", quicksort([1,10,2,6,9,15]))
























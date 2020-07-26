def search(arr):
    low = arr[0]
    indice = 0

    for i in range(1, len(arr)):
        if(arr[i] < low):
            low = arr[i]
            indice = i

    return indice


print(search([10,3,4,60,1, 2]))



def sort_by_selection(arr):
    newArr = []
    for i in range(len(arr)):
        low = search(arr)
        newArr.append(arr.pop(low))

    return newArr



print(sort_by_selection([10, 3, 12, 123, 1,2]))

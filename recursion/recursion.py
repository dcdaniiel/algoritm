def count(n):
    print(n)
    if n <= 0:
        return
    else:
        count(n-1)


print(count(10))



def fat(n):
    print(n)

    if n == 1:
        return 1
    else:
        return n * fat( n - 1 )



print("FATORIAL: ", fat(5))

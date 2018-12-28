
def route_num(gridsize):
    arr = [1] * gridsize
    print(arr)
    for i in range(gridsize):

        for j in range(i):
            arr[j] = arr[j] + arr[j - 1]
            print(arr[j],end=" ")
        arr[i] = 2 * arr[i - 1]
        print(arr[i],end=" ")
    return arr[gridsize - 1]


n = route_num(4)

print("%s paths found" % n)
def iterate(arr):
    for i in range(5):
        arr2 = arr.copy()
        arr2.append(i)
        print(arr2)

iterate([2,3,4])
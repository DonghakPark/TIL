arr = [1,2,3,4,5,6,7]

def swap(index1, index2):
    temp = arr[0]
    arr[0] = arr[1]
    arr[1] = temp

def permutation(arrsize):
    if (arrsize == 1):
        for i in range(7):
            print(arr[i])
        return


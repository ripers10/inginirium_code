import numpy

arr = numpy.arange(10)
arr2 = numpy.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
print(arr2)

def inner(array1, array2):
    for i, e in enumerate(array1):
        if (e in array2) == False:
            return False

    return True

print(inner(arr, arr2))

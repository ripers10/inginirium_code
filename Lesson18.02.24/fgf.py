import numpy

arr = numpy.empty([2, 2], dtype=int)
print(arr)

arr1 = numpy.ones([2, 2], dtype=int)
print(arr1)

arr2 = numpy.arange(10)
print(arr2)

print(arr2[slice(2, 7, 2)])

print(arr2[::])
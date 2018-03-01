import numpy

array = numpy.array([1,2,3,4,5,6])

print(array.ndim)

print(array.shape)

array2 = array.reshape(3,2)

print(array2)

print(array2*2)

array3=numpy.array([1,2,numpy.NaN,4,5])

print(numpy.isnan(array3))

print(array3.dtype)

array4=numpy.array([1,2,numpy.NaN,"test",5])

print(array4.dtype)

print(array[:3])


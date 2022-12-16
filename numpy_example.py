import numpy as np

# Create np array
array = np.array([[7, 77, 777], [5, 55, 555]])
print(type(array))
print(type(array.shape))
print(array[1, 1])

print("___________________________\n")

# Create other np array
array1 = np.zeros((1080, 1920))
print(array1)

print("___________________________\n")

# Create other np array
array2 = np.full((2, 2), 9.1)
print(array2)

print("___________________________\n")

# Create other np array
array3 = np.eye(7, 7)
print(array3)

print("___________________________\n")

# Create other np array
array4 = np.ones((10, 7, 2))
print(array4)

print("___________________________\n")

# Create other np array
array5 = np.random.random((5, 5))
print(array5)

print("___________________________\n")

# Create other np array
array6 = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33], [41, 42, 43]])
print(array6)

print("___________________________\n")

# Create other np array
cols = np.array([0, 1, 2, 0])
rows = np.arange(4)
print(f"Cols = {cols}")
print(f"Rows = {rows}")

for row, col in zip(rows, cols):
	print(f"({row},{col})")

print("___________________________\n")

# Create other np array
array7 = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33], [41, 42, 43]])
filter = (array7 > 15)
print(filter)
print("***")
filtered = array7[filter]
print(filtered)
print("***")
print(array7[(array7 % 2 == 0)])
print("***")
array7[(array7 % 2 == 0)] += 100
print(array7)

print("___________________________\n")

# Create other np array
array8 = np.array([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]])
print(array8)
print("***")
array_slice = array8[:2, 1:3]
print(array_slice)
print("***")
print(f"Slice: {array_slice[0, 0]}")
print("***")
array_slice[0, 0] += 100
print(f"Slice: {array_slice[0, 0]}")
print("***")
print(f"Array originial: {array8[0, 1]}")
print("***")
new_array = np.array(array_slice)
print(new_array)

print("___________________________\n")

# Create other np array
array10 = np.array([11, 12])
print(array10.dtype)
print("***")

array10 = np.array([11.0, 12.0])
print(array10.dtype)
print("***")

array10 = np.array([11, 12], dtype=np.float64)
print(array10.dtype)
print("***")

array10 = np.array([11.1, 12.1], dtype=np.int64)
print(array10.dtype)
print("***")

print("___________________________\n")

# Create other np array
x = np.array([[111, 112], [121, 122]], dtype=np.int32)
y = np.array([[211.1, 212.1], [221.1, 222.1]], dtype=np.float64)

print(x)
print(y)
print("***")
print(x - y)
print("***")
print(np.subtract(x, y))
print("***")
print(x * y)
print("***")
print(np.multiply(x, y))
print("***")
print(x / y)
print("***")
print(np.divide(x, y))
print("***")
print(np.sqrt(x))

print("___________________________\n")

# Create other np array
array11 = 10 * np.random.randn(2, 5)
print(array11)
print("***")
print(array11.mean())
print("***")
print(array11.mean(axis=1))
print("***")

print("___________________________\n")

# Create other np array
array12 = np.random.randn(10)
print(array12)
print("***")
sort = np.array(array12)
sort.sort()
print(sort)
print("***")

print("___________________________\n")

# Create other np array
array13 = np.array([1, 4, 7, 1, 4, 4, 4, 1, 2])
print(np.unique(array13))

print("___________________________\n")

# Create other np array
s1 = np.array(['escritorio', 'mesa', 'silla'])
s2 = np.array(['escritorio', 'mesa', 'lampara'])
print(s1)
print(s2)
print("***")
print(np.intersect1d(s1, s2))
print("***")
print(np.union1d(s1, s2))
print("***")
print(np.setdiff1d(s1, s2))
print("***")
print(np.in1d(s1, s2))

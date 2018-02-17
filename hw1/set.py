# test the set
'''
s1 = set()
s1.add((1,2))
s1.add((2,5))

print(s1)
print((1,2) in s1)
if (1,2) in s1:
	print "Gooooooooooood"

def demo(x):
	if x < 5:
		print "Fuck"
		demo(x + 1)
	else:
		return


for i in range(0,10):
	print i
	demo(i)
'''
from random import *

'''
def Partition(A, p, r):
	x = A[r]
	i = p - 1
	temp = 0

	for j in range(p, r):
		if A[j] <= x:
			i += 1
			temp = A[i]
			A[i] = A[j]
			A[j] = temp
	temp = A[i+1]
	A[i+1] = A[r]
	A[r] = A[i+1]
	return i + 1

def QuickSort(A, p, r):
	if p < r:
		q = Partition(A, p, r)
		QuickSort(A, p, q - 1)
		QuickSort(A, q + 1, r)

#print "random gen num %d" %(randint(1, 100))
Arr = []
for i in range(20):
	Arr.append(randint(1, 100))
	print "Arr[%d] = %d" %(i, Arr[i])

print "-----Sorting Result-----"

QuickSort(Arr, 0, len(Arr) - 1)

for i in range(len(Arr)):
	print "Arr[%d] = %d" %(i, Arr[i])
'''

Arr = [9 ,13, 2, 5, 19,33, 67, 33, 90, 3, 128, 99, 33, 77, 21]
print max(Arr)


from random import shuffle
A = [i for i in range(10)]
shuffle(A) # shuffle() function has no return value, so A=shuffle(A) will cause an error.
print "sorting_array\n%s\n"%A
for j in range(1,10):
    key = A[j]
    i = j - 1
    while i>=0 and A[i]>key:
        A[i+1] = A[i]
        i -= 1
    A[i+1] = key
print "sorted_array:\n%s\n"%A

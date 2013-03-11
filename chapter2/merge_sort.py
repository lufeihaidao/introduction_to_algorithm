from math import floor
from random import shuffle

#global A
def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    inf = float("inf") # infinity
    l_list = [ A[p+i] for i in range(n1) ]
    l_list.append(inf)
    r_list = [ A[q+i+1]  for i in range(n2) ]
    r_list.append(inf)
    i = 0
    j = 0
    for k in range(p, r+1):
        if l_list[i] <= r_list[j]:
            A[k] = l_list[i]
            i += 1
        else:
            A[k] = r_list[j]
            j += 1

def merge_sort(A, p, r):
    if p < r:
        q = int(floor( (p + r) / 2 ))
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def test():
    A = [i for i in range(10)]
    shuffle(A)
    print "sorting_array\n%s"%A
    merge_sort(A, 0, len(A)-1)
    print "sortied_array\n%s"%A

test()

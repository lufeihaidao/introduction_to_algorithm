from random import shuffle
def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-1,i,-1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]

a = range(10)
shuffle(a)
print "sorting_array\n%s"%a
bubble_sort(a)
print "sortied_array\n%s"%a

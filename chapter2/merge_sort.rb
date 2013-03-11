def merge(a, p, q, r)
    n1 = q - p + 1
    n2 = r - q
    inf = 1.0/0 # infinity
    l_list = (0..n1-1).map { |i| a[p+i] }
    l_list << (inf)
    r_list = (0..n2-1).map{ |i|  a[q+i+1] }
    r_list << (inf)
    i = 0
    j = 0
    for k in p..r
        if l_list[i] <= r_list[j]
            a[k] = l_list[i]
            i += 1
        else
            a[k] = r_list[j]
            j += 1
        end
    end
end


def merge_sort(a, p, r)
    if p < r
        q = ( (p + r) / 2 ).floor
        merge_sort(a, p, q)
        merge_sort(a, q+1, r)
        merge(a, p, q, r)
    end
end

def test()
    a = (0..9).to_a.shuffle
    print "sorting_array\n%s\n"%a.to_s
    merge_sort(a, 0, a.length-1)
    print "sortied_array\n%s\n"%a.to_s
end

test()

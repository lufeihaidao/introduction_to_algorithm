def bubble_sort(a)
    for i in 0..a.length-1
        for j in (a.length-1).downto i+1
            if a[j] < a[j-1]
                a[j], a[j-1] = a[j-1], a[j]
            end
        end
    end
end

a = (0..9).to_a.shuffle
puts "sorting_array\n%s"%a.to_s
bubble_sort a
puts "sortied_array\n%s"%a.to_s

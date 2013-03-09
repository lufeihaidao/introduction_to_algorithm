A = (0..9).to_a.shuffle
puts "sorting_array:\n%s\n"%A.to_s
for j in 1..9
  key = A[j]
  i = j - 1
  while i >= 0 && A[i] > key
    A[i+1] = A[i]
    i -= 1
  end
  A[i+1] = key
end
puts "sorted_array:\n%s\n"%A.to_s

# find min value in an array - time complexity O(n), space complexity O(1)

my_array = [3, 7, 12, 9, 4, 11]
#print( my_array[0] )

#Python

min_val = my_array[0]

for n in my_array[1:]:
  if min_val > n:
    min_val = n

print('min val:', min_val)
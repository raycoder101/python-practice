# bubble sort algorithm - time complexity O(n^2), space complexity O(1)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(n-1):
  print('loop #', i+1)
  for j in range(n-1-i):
    if my_array[j] > my_array[j+1]:
      my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
    print(my_array)

print('sorted array: ', my_array)
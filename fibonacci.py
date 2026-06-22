#fibonacci sequence - time complexity O(2^n), space complexity O(n)

print("Fibonacci Sequence solution 1: loop")
print(0)
print(1)
count = 2

def fibonacci(prev1, prev2, iteration):
  for n in range(3,iteration+1):
    newFibo = prev1 + prev2
    print(newFibo)
    prev2 = prev1
    prev1 = newFibo

fibonacci(1,0,10)


print("Fibonacci Sequence solution 2: recursion")

print(0)
print(1)
count = 2

def fibonacciR(prev1, prev2, iteration):
  global count
  if count <= iteration:
    newFib = prev1 + prev2
    print(newFib)
    prev2 = prev1
    prev1 = newFib
    
    count += 1
    
    fibonacciR(prev1, prev2, iteration)

fibonacciR(1,0,19)


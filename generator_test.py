######################################################################
# First example: A generator function using 'yield'
def count_up_to(max_num):
    count = 1
    while count <= max_num:
        yield count  # Pauses here and hands over the value
        count += 1   # Resumes here on the next call

# 1. Create the generator object
counter = count_up_to(3)

print(counter) 
# Output: <generator object count_up_to at 0x...>
# Notice it didn't print the numbers yet! It's just waiting.

# 2. Grab values one by one using next()
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(next(counter))  # Output: 3

# If you call next(counter) again, it raises a StopIteration loop exit.


######################################################################
# 1. A List Comprehension (Computes everything instantly in memory)
squares_list = [x**2 for x in range(1, 6)]
print(squares_list)  
# Output: [1, 4, 9, 16, 25]

# Iterating through it
for x in squares_list:
    print(x)  # Prints 1, 4, 9, 16, 25 one by one

# 2. A Generator Expression (Computes things "lazily" on demand)
squares_gen = (x**2 for x in range(1, 6))
print(squares_gen)   
# Output: <generator object <genexpr> at 0x...>

# Iterating through it
for num in squares_gen:
    print(num)  # Prints 1, 4, 9, 16, 25 one by one

# NOTE: Once a generator is consumed, it's empty! 
# If you try to loop through squares_gen again, nothing will print.
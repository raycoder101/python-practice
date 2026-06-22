list_a = [x*x for x in range(1, 4)]
print(list_a)

generator_a = (x*x for x in range(1,4))
print(generator_a)
print(next(generator_a))
print(next(generator_a))
print(next(generator_a))
print(next(generator_a))
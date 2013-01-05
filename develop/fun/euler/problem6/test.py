sum_of_squares = 0
for i in range(1, 101):
    sum_of_squares += i ** 2
print sum_of_squares

square_of_sum = sum(range(1, 101)) ** 2
print square_of_sum

print sum_of_squares - square_of_sum 


# Sample input tuple
input_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Create a new tuple with even numbers using a tuple comprehension
even_numbers_tuple = tuple(num for num in input_tuple if num % 2 == 0)

# Display the result
print("Original tuple:", input_tuple)
print("Tuple with even numbers:", even_numbers_tuple)

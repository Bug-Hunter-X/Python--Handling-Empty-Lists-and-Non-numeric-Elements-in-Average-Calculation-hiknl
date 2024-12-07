def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle list with no numbers
    return sum(numeric_numbers) / len(numeric_numbers)

# Correct usage 
my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [1, 2, 'a']
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [1, 2, 3]
average = calculate_average(my_numbers)
print(f"The average is: {average}") 
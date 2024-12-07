def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Incorrect usage leading to ZeroDivisionError
my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

# Another incorrect usage leading to TypeError
my_numbers = [1, 2, 'a']
average = calculate_average(my_numbers)
print(f"The average is: {average}")
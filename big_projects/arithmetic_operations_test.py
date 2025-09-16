from arithmetic_operations import perform_operation


print("Arithmetic Operations")
number_one = float(input("Enter the first number: ").strip())
number_two = float(input("Enter the second number: ").strip())
operation = input("Enter one of these operations (add, subtract, multiply, divide): ").strip().lower()

result = perform_operation(number_one, number_two, operation)

print(f"Result: {result}")

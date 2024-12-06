def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
number = 10
result = is_even_or_odd(number)
print(f"The number {number} is {result}.")

inp = input("Enter a number: ")
if type(inp) == int or type(inp) == float:
    print("yes this is a number")
else:
    print("this is not a number")
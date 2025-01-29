string = input("Enter a string: ")
uppercase_count = sum(1 for char in string if char.isupper())
lowercase_count = sum(1 for char in string if char.islower())

print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase_letters: {lowercase_count}")
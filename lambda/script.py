# Simple lambda function
add_two = lambda my_input: my_input + 2

print(add_two(3))
print(add_two(100))
print(add_two(-2))

# is_substring
is_substring = lambda my_string: my_string in "This is the master string"

print(is_substring('I'))
print(is_substring('am'))
print(is_substring('the'))
print(is_substring('master'))
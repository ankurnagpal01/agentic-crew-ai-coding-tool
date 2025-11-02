```python
def is_palindrome(s):
    # Normalize the string: remove spaces and convert to lowercase
    normalized_str = ''.join(s.split()).lower()
    # Check if the string is equal to its reverse
    return normalized_str == normalized_str[::-1]

# Example usage
input_string = "A man a plan a canal Panama"
result = is_palindrome(input_string)
print(f"The string '{input_string}' is a palindrome: {result}")
```
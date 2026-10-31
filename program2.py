def is_palindrome(text):
    # Standardize the text: lowercase it and remove non-alphanumeric characters
    clean_text = .join(char.lower() for char in text if char.isalnum())
    
    # Check if the text reads the same forward and backward
    return clean_text == clean_text[::-1]

# Examples
print(is_palindrome(racecar))  # Returns: True
print(is_palindrome(RadAr))    # Returns: True (Case-insensitive)
print(is_palindrome(hello))    # Returns: False

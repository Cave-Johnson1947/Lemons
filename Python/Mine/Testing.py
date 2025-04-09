def caesar_cipher(plaintext, key):
    ciphertext = ""

    # Loop through each character in the plaintext
    for char in plaintext:
        # Check if the character is an uppercase letter
        if char.isupper():
            ciphertext += chr((ord(char) + key - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            ciphertext += chr((ord(char) + key - 97) % 26 + 97)
        else:
            # Non-letter characters are added as is
            ciphertext += char
    
    return ciphertext

# Get user input
plaintext = input("Enter the plaintext: ")
key = int(input("Enter the key (shift): "))

# Ensure the key is positive
if key < 0:
    print("Key must be a positive integer.")
else:
    print(f"Encrypted text: {caesar_cipher(plaintext, key)}")

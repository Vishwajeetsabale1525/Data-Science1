# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 19:59:42 2023

@author: Vishwajeet
"""

import secrets
import string
import base64

def generate_password(length=12):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a secure random password
    password = ''.join(secrets.choice(characters) for _ in range(length))

    return password

def encode_password(password):
    # Encode the password using base64
    encoded_password = base64.b64encode(password.encode()).decode()
    
    return encoded_password

def decode_password(encoded_password):
    # Decode the password using base64
    decoded_password = base64.b64decode(encoded_password.encode()).decode()
    
    return decoded_password

# Generate a random password
password = generate_password()

# Encode the password
encoded_password = encode_password(password)

# Decode the password
decoded_password = decode_password(encoded_password)

# Print the results
print("Generated Password:", password)
print("Encoded Password:", encoded_password)
print("Decoded Password:", decoded_password)

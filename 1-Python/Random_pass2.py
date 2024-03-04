# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 19:51:39 2023

@author: Vishwajeet
"""

import random

# Playfair cipher functions (as shown in previous responses)
def generate_playfair_matrix(key):
    # Implementation of the Playfair cipher functions goes here

 def playfair_encrypt(plaintext, key):
    # Implementation of Playfair encryption goes here

  def find_coordinates(matrix, char):
    # Implementation of finding coordinates in the Playfair matrix goes here

# Define a list of possible keys for the game
        keys = ["CRYPTO", "PUZZLE", "SECRET", "ENCRYPT", "CHALLENGE", "SOLVE"]

# Select a random key for the game
        key = random.choice(keys)

# Generate the Playfair matrix using the selected key
playfair_matrix = generate_playfair_matrix(key)

# Define the message to be decrypted by the participants
message = "ZFXDZMYIJKUJAWW"
ciphertext = playfair_encrypt(message, key)

# Provide participants with a clue
clue = "Welcome to the Cryptographic Challenge Game!\nDecrypt the following message using a Playfair cipher with the key: '{}'".format(key)

# Print the clue and the encrypted message
print(clue)
print(ciphertext)

# Participants must decrypt the message using the Playfair cipher and the provided key
# To win the game, they need to reveal the decrypted message

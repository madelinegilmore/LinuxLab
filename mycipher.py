import sys

def ceasar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is alphabetic
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        # Skip digits, punctuation marks, and blanks
    return result

def print_encoded_blocks(encoded_text):
    block_size = 5
    blocks_per_line = 10
    blocks = [encoded_text[i:i+block_size] for i in range(0, len(encoded_text), block_size)]
    for i in range(0, len(blocks), blocks_per_line):
        print(' '.join(blocks[i:i+blocks_per_line]))

text = input("Enter the text to encrypt: ").upper()
shift = int(input("Enter the shift value: "))
encrypted_text = ceasar_cipher(text, shift)
print("Encrypted text:")
print_encoded_blocks(encrypted_text)

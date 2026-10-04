import base64
try:
    from .utils import string_to_bit_array, bit_array_to_string, bits_to_int, pad, unpad
except ImportError:  # dijalankan langsung sebagai skrip
    from utils import string_to_bit_array, bit_array_to_string, bits_to_int, pad, unpad
try:
    from .des import des_encrypt, des_decrypt
except ImportError:  # dijalankan langsung sebagai skrip
    from des import des_encrypt, des_decrypt

def encrypt(plaintext, key):
    padded_text = pad(plaintext)
    plaintext_bits = string_to_bit_array(padded_text)
    key_bits = string_to_bit_array(key[:8])  
    
    ciphertext_bits = []
    for i in range(0, len(plaintext_bits), 64):
        block = plaintext_bits[i:i+64]
        encrypted_block = des_encrypt(block, key_bits)
        ciphertext_bits.extend(encrypted_block)
    
    ciphertext_bytes = bytes(bits_to_int(ciphertext_bits[i:i+8]) for i in range(0, len(ciphertext_bits), 8))
    return base64.b64encode(ciphertext_bytes).decode('utf-8')

def decrypt(ciphertext, key):
    ciphertext_bytes = base64.b64decode(ciphertext)
    ciphertext_bits = [int(bit) for byte in ciphertext_bytes for bit in format(byte, '08b')]
    key_bits = string_to_bit_array(key[:8]) 
    
    plaintext_bits = []
    for i in range(0, len(ciphertext_bits), 64):
        block = ciphertext_bits[i:i+64]
        decrypted_block = des_decrypt(block, key_bits)
        plaintext_bits.extend(decrypted_block)
    
    plaintext = bit_array_to_string(plaintext_bits)
    return unpad(plaintext)
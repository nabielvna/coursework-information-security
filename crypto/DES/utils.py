import string
import random

def generate_random_key():
    key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    return key

def permute(block, table):
    return [block[i - 1] for i in table]

def split(block):
    return block[:len(block)//2], block[len(block)//2:]

def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]

def left_shift(x, n):
    return x[n:] + x[:n]

def int_to_bits(n, bits):
    return [int(b) for b in format(n, f'0{bits}b')]

def bits_to_int(bits):
    return int(''.join(map(str, bits)), 2)

def string_to_bit_array(text):
    return [int(bit) for char in text.encode('utf-8') for bit in format(char, '08b')]

def bit_array_to_string(bits):
    return ''.join(chr(bits_to_int(bits[i:i+8])) for i in range(0, len(bits), 8))

def pad(text):
    pad_length = 8 - (len(text) % 8)
    return text + chr(pad_length) * pad_length

def unpad(text):
    pad_length = ord(text[-1])
    return text[:-pad_length]
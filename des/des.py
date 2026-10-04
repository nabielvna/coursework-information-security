try:
    from .des_tables import DES_TABLES
except ImportError:  # dijalankan langsung sebagai skrip
    from des_tables import DES_TABLES
try:
    from .utils import permute, split, xor, left_shift, int_to_bits, bits_to_int
except ImportError:  # dijalankan langsung sebagai skrip
    from utils import permute, split, xor, left_shift, int_to_bits, bits_to_int

def generate_subkeys(key):
    key = permute(key, DES_TABLES["PC1"])
    C, D = split(key)
    subkeys = []
    for i in range(16):
        if i in [0, 1, 8, 15]:
            C = left_shift(C, 1)
            D = left_shift(D, 1)
        else:
            C = left_shift(C, 2)
            D = left_shift(D, 2)
        subkey = permute(C + D, DES_TABLES["PC2"])
        subkeys.append(subkey)
    return subkeys

def f_function(R, subkey):
    expanded_R = permute(R, DES_TABLES["E"])
    xored = xor(expanded_R, subkey)
    S_output = []
    for i in range(8):
        block = xored[i*6:(i+1)*6]
        row = bits_to_int([block[0], block[5]])
        col = bits_to_int(block[1:5])
        S_output.extend(int_to_bits(DES_TABLES["S_BOXES"][i][row][col], 4))
    return permute(S_output, DES_TABLES["P"])

def des_round(L, R, subkey):
    return R, xor(L, f_function(R, subkey))

def des_encrypt(plaintext, key):
    subkeys = generate_subkeys(key)
    block = permute(plaintext, DES_TABLES["IP"])
    L, R = split(block)
    for subkey in subkeys:
        L, R = des_round(L, R, subkey)
    block = permute(R + L, DES_TABLES["IP_INV"])  
    return block

def des_decrypt(ciphertext, key):
    subkeys = generate_subkeys(key)
    block = permute(ciphertext, DES_TABLES["IP"])
    L, R = split(block)
    for subkey in reversed(subkeys):
        L, R = des_round(L, R, subkey)
    block = permute(R + L, DES_TABLES["IP_INV"])  
    return block
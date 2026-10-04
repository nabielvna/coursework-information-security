__version__ = "1.0.0"
__author__ = "nabielvna"

# Core DES operations
from .crypto import (
    encrypt,
    decrypt,
)

from .des import (
    des_encrypt,
    des_decrypt,
)

# Utility functions
from .utils import (
    generate_random_key,
    string_to_bit_array,
    bit_array_to_string,
    pad,
    unpad,
)

# Define public API
__all__ = [
    # Core functionality
    'encrypt',
    'decrypt',
    'des_encrypt',
    'des_decrypt',
    
    # Utilities
    'generate_random_key',
    'string_to_bit_array',
    'bit_array_to_string',
    'pad',
    'unpad',
]
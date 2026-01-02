"""
Hey there! Welcome to Cryzen. 

I built this library to make cryptography and hashing simple and accessible 
for everyone, especially for those working in mobile-first environments. 
Whether you're looking to secure a user's password or just want to hide 
some data quickly, Cryzen has a tool for you.

Here’s a quick guide on how to use what's inside:

-------------------------------------------------------------------------------
 1. ENCRYPTION & DECRYPTION (When you need to get the data back)
-------------------------------------------------------------------------------

● AstraCrypt: This is the heavyweight champion here. It uses AES-256-CBC 
  to keep your data super secure. Use this for sensitive stuff like private 
  messages or files. (Make sure yo vpyypto installed!)
  
  Example:
    >>> from cryzen import astra_encrypt, astra_decrypt
    >>> my_token = astra_encrypt("Hey Mahadi!", "your-secret-key")
    >>> print(astra_decrypt(my_token, "your-secret-key"))

● FluxCipher: Need something fast and simple? Flux uses a XOR cipher. 
  It’s great for quick data masking or obfuscation where you don't 
  need military-grade security but just want to keep things hidden.
  
  Example:
    >>> from cryzen import flux_encrypt, flux_decrypt
    >>> secret = flux_encrypt("Hide this", "my-key")
    >>> print(flux_decrypt(secret, "my-key"))

● ZenCode: A handy wrapper for URL-safe Base64. Perfect for sending 
  tokens or short messages through web links without breaking them.

-------------------------------------------------------------------------------
️ 2. SECURE HASHING (One-way only, no going back!)
-------------------------------------------------------------------------------

● OmegaHash: This is what you should use for passwords. It uses 
  PBKDF2-HMAC-SHA512 with 200,000 rounds and a random salt. It's designed 
  to be slow for hackers but safe for your users.
  
  Example:
    >>> from cryzen import omega_hash
    >>> # This gives you 'salt$hash' - store the whole thing!
    >>> hashed_pass = omega_hash("user_password_123")

● TerraHash: Your go-to for standard SHA-256 hashing. Reliable, 
  globally recognized, and perfect for file integrity checks.

● NovaHash: Built for speed! It uses BLAKE2b to give you a fast, 
  compact hash whenever you need performance over everything else.

-------------------------------------------------------------------------------
 A FEW EXTRAS
-------------------------------------------------------------------------------
Inside 'cryzen.utils', I've added some helper functions to handle 
conversions between text, bytes, hex, and base64 so you don't have to 
worry about encoding issues.

Author: Mahadi
License: MIT
Find me on GitHub: https://github.com/mahadi99900/cryzen

Happy Coding! 💻
"""

from .astracrypt import astra_encrypt, astra_decrypt
from .flux import flux_encrypt, flux_decrypt
from .nova import nova_hash
from .omega import omega_hash
from .terra import terra_hash
from .zencode import zencode_encrypt, zencode_decrypt

__all__ = [
    'astra_encrypt', 'astra_decrypt',
    'flux_encrypt', 'flux_decrypt',
    'nova_hash', 'omega_hash',
    'terra_hash',
    'zencode_encrypt', 'zencode_decrypt'
]

def hello():
    print("Cryzen 0.1.2 is ready and loaded!")

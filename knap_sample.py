# After `$ pip install TextVault`

from TextVault import KnapsackEncryptor
txt = "Hello, World!"
enc = KnapsackEncryptor()

pub, priv = enc.newkey()
a = enc.encrypt(txt, pub)
A = enc.decrypt(a, priv)

print("Public key:", pub)
print("Private key:", priv)

print("Original:", txt)
print("Encrypted:", a)
print("Decrypted:", A)
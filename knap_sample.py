# After `$ pip install TextVault`

from TextVault import KnapsackEncryptor, KnapsackKey
txt = "Hello, World!"
enc = KnapsackEncryptor()

pub, priv = enc.newkey()
a = enc.encrypt(txt, pub)
A = enc.decrypt(a, priv)

print("Public key:", pub)
print("Private key:", priv)
print()

print("Original:", txt)
print("Encrypted:", a)
print("Decrypted:", A)
print()

pub.export_txt("knap_public_key.txt")
pub2 = KnapsackKey.import_txt("knap_public_key.txt")

print("Original Key:", pub)
print("After Save & Load:", pub2)
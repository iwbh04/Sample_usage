# After `$ pip install TextVault`

from TextVault import KnapsackEncryptor, KnapsackKey
txt = "Hello, World! 😀"
enc = KnapsackEncryptor()

pub, priv = enc.newkey()
encrypted = enc.encrypt(txt, pub)
decrypted = enc.decrypt(encrypted, priv)

print("Public key:", pub)
print("Private key:", priv)
print()

print("Original:", txt)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
print()

pub.export_txt("knap_public_key.txt")
pub_2 = KnapsackKey.import_txt("knap_public_key.txt")

print("Original Key:", pub)
print("After Save & Load:", pub_2)
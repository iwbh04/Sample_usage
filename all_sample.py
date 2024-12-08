from TextVault import *
# --------------------------------------------------
print("\n--------------------------------------------------\n** Knapsack **\n")
# --------------------------------------------------

txt = "Hello, World! 😀"
enc = KnapsackEncryptor()

pub, priv = enc.newkey()
encrypted = enc.encrypt(txt, pub)
decrypted = enc.decrypt(encrypted, priv)

print("Public key:", pub)
print("Private key:", priv)
print()

print(" Original:", txt)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
print()

pub.export_txt("knap_public_key.txt")
pub_2 = KnapsackKey.import_txt("knap_public_key.txt")

print("     Original Key:", pub)
print("After Save & Load:", pub_2)

# --------------------------------------------------
print("\n--------------------------------------------------\n** RSA **\n")
# --------------------------------------------------

enc = RsaEncryptor()

print("Generating RSA keys...")
public_key, private_key = enc.newkey()

# Save keys to files
enc.save_keys(public_key, private_key)
print("Keys saved to 'public_key.txt' and 'private_key.txt'.")

# Load keys back from files
public_key = enc.load_key("public_key.txt")
private_key = enc.load_key("private_key.txt")
print("Keys loaded back from files.")

print("Public Key:", public_key)
print("Private Key:", private_key)

# Message to encrypt and decrypt
message = "Hello"
print("\nOriginal Message:", message)

# Encrypt the message
encrypted_msg = enc.encrypt(message, public_key)
print("Encrypted Message:", encrypted_msg)

# Decrypt the message
decrypted_msg = enc.decrypt(encrypted_msg, private_key)
print("Decrypted Message:", decrypted_msg)

# --------------------------------------------------
print("\n--------------------------------------------------\n** Vigenere **\n")
# --------------------------------------------------

txt = "Hello, World!"
enc = VigenereEncryptor()

key = enc.newkey()
encrypted = enc.encrypt(txt, key)
decrypted = enc.decrypt(encrypted, key)

print("Key:", key)
print()

print("Original:", txt)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
print()

# --------------------------------------------------
print("\n--------------------------------------------------\n** JMatrix **\n")
# --------------------------------------------------

# Instantiate the encryptor
encryptor = JMatrixEncryptor(matrix_size=3)

# Generate keys
public_key, private_key = encryptor.newkey()
print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")

# Encrypt a message
message = "hello"
encrypted_message = encryptor.encrypt(message, public_key)
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")

# Decrypt the message
decrypted_message = encryptor.decrypt(encrypted_message, private_key)
print(f"Decrypted Message: {decrypted_message}")

# --------------------------------------------------
print("\n--------------------------------------------------\n** HillNum **\n")
# --------------------------------------------------

cipher = Hillcipherwithnumbers(size=2)

print("Generated Key Matrix:")
print(cipher.key_matrix)

plaintext = "A1B2C34"
print("Original Text:", plaintext)

encrypted = cipher.encrypt(plaintext)
print("Encrypted Text (as numbers):", encrypted)

decrypted = cipher.decrypt(encrypted)
print("Decrypted Text:", decrypted)

# Generate a random password
random_password = cipher.generate_random_password()
print("Generated Random Password:", random_password)

# Using the random password in encryption
print("Encrypting the generated random password:")
encrypted_password = cipher.encrypt(random_password)
print("Encrypted Password (as numbers):", encrypted_password)

decrypted_password = cipher.decrypt(encrypted_password)
print("Decrypted Password:", decrypted_password)

# Verification for random password
if random_password == decrypted_password:
    print("Success: Decrypted password matches the generated password!")
else:
    print("Error: Decrypted password does not match the generated password.")

# --------------------------------------------------
print("\n--------------------------------------------------\n")
# --------------------------------------------------

# deleting text files
from os import remove
remove("public_key.txt")
remove("private_key.txt")
remove("knap_public_key.txt")

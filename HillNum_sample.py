from TextVault import Hillciperwithnumbers

if __name__ == "__main__":
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

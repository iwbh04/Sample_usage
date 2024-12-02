from rsa import generate_keys, encrypt, decrypt

if __name__ == "__main__":
    print("Generating RSA keys...")
    public_key, private_key = generate_keys()

    print("Public Key:", public_key)
    print("Private Key:", private_key)

    message = "HELLO"
    print("\nOriginal Message:", message)

    encrypted_msg = encrypt(public_key, message)
    print("Encrypted Message:", encrypted_msg)

    decrypted_msg = decrypt(private_key, encrypted_msg)
    print("Decrypted Message:", decrypted_msg)
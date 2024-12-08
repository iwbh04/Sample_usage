from TextVault.rsa import RsaEncryptor
# need to install TextVault into the repository first
if __name__ == "__main__":
    # Instantiate the Encryptor
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

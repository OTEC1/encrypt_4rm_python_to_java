from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    print(key)
    message = "ones".encode()
    f = Fernet(key)
    encrypt = f.encrypt(message)
    dec = f.decrypt(encrypt)
    print("Encrypt = " + str(encrypt))
    print("decrypted = " + str(dec))


write_key()

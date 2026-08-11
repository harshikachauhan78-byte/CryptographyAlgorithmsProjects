from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)

public_key = key.publickey()
private_key = key

message = input("Enter message: ").encode()

cipher = PKCS1_OAEP.new(public_key)
encrypted = cipher.encrypt(message)

print("Encrypted:", encrypted.hex())

decipher = PKCS1_OAEP.new(private_key)
decrypted = decipher.decrypt(encrypted)

print("Decrypted:", decrypted.decode())
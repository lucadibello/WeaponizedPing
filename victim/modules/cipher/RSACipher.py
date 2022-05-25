from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class RSACipher:
  
  @staticmethod
  def encrypt(plaintext):
    recipient_key = RSA.importKey(open("./key/receiver.pem").read())
    
    # Transform string to byte array
    plaintext = plaintext.encode() 

    # Encrypt the plaintext
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    ciphertext = cipher_rsa.encrypt(plaintext)

    # Return the encrypted text
    return ciphertext

  @staticmethod
  def decrypt(ciphertext):
    sender_key = RSA.importKey(open("../attacker/key/private.pem").read())
    
    # Decrypt the ciphertext
    cipher_rsa = PKCS1_OAEP.new(sender_key)
    plaintext = cipher_rsa.decrypt(ciphertext)

    # Return the decrypted text
    return plaintext.decode()

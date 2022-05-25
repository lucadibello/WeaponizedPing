from Crypto.PublicKey import RSA

key = RSA.generate(4096)
private_key = key.exportKey()
with open("./private.pem", "wb") as f:
    f.write(private_key)

public_key = key.publickey().exportKey()
with open("receiver.pem", "wb") as f:
    f.write(public_key)
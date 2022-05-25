# Read file accepted from stdin and decrypt it using the key set by the user.
#!/usr/bin/env python3
# Path: utility/decrypt-file.py

# Prepare the file to be decrypted
import sys
import os
import argparse

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key", help="Path to the private key", required=True)
parser.add_argument("-f", "--file", help="File to decrypt", required=True)
args = parser.parse_args()

# Check if the key file exists
if not os.path.isfile(args.key):
  print("Private key not found")
  sys.exit(1)

if not os.path.isfile(args.file):
  print("Encrypted IMCP payload dump not found")
  sys.exit(1)

# Read the file to be decrypted
file = open(args.file, "rb")
data = file.read()

# Skip first 8 bytes
data = data[8:]

file.close()

# Decrypt the file using the Crypto library
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Load RSA private key
key = RSA.importKey(open(args.key).read())
cipher = PKCS1_OAEP.new(key)
decrypted = cipher.decrypt(data)

# Print decrypted data
print(decrypted)

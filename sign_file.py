# sign_file.py
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Step 1: Read the file to be signed
file_path = "agreement.pdf"
with open(file_path, 'rb') as f:
    message = f.read()

# Step 2: Create SHA-256 hash of the message
hash_obj = SHA256.new(message)

# Step 3: Generate RSA private-public key pair
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Step 4: Sign the hash with the private key
signature = pkcs1_15.new(key).sign(hash_obj)

# Step 5: Save the signature, public key, and original file (if needed)
with open("signature.sig", 'wb') as sig_file:
    sig_file.write(signature)

with open("public.pem", 'wb') as pub_file:
    pub_file.write(public_key)

with open("private.pem", 'wb') as priv_file:
    priv_file.write(private_key)

print("Signature and keys generated successfully.")

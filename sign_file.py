from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
import os

# Step 1: Load the file to be signed
file_path = "agreement.pdf"
with open(file_path, "rb") as f:
    file_data = f.read()

# Step 2: Generate RSA key pair
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Step 3: Sign the file
signature = private_key.sign(
    file_data,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Step 4: Save the signature
with open("signature.sig", "wb") as sig_file:
    sig_file.write(signature)

# Step 5: Save the public key
with open("public.pem", "wb") as pub_file:
    pub_file.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

# Step 6: Save the private key (⚠️ do NOT share this file publicly)
with open("private.pem", "wb") as priv_file:
    priv_file.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))

print("✅ Signature and keys generated successfully!")

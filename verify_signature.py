from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature
import os

# Input paths from user
file_path = input("Enter the path to the file you received (e.g., agreement.pdf): ")
signature_path = input("Enter the path to the signature file (e.g., signature.sig): ")
public_key_path = input("Enter the path to the sender's public key (e.g., public.pem): ")

# Step 1: Load file contents
try:
    with open(file_path, "rb") as f:
        file_data = f.read()
    with open(signature_path, "rb") as f:
        signature = f.read()
    with open(public_key_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())
except FileNotFoundError as e:
    print(f"❌ Error: {e}")
    exit()

# Step 2: Verify the signature
try:
    public_key.verify(
        signature,
        file_data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("✅ Signature verification succeeded! File is authentic.")
except InvalidSignature:
    print("❌ Signature verification failed: File has been tampered with or public key is invalid.")
    print("⚠️  The file has been deleted for security.")
    os.remove(file_path)

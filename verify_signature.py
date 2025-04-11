from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature
import os

def verify_signature(file_path, signature_path, public_key_path):
    # Read the original file
    with open(file_path, 'rb') as f:
        file_data = f.read()

    # Read the digital signature
    with open(signature_path, 'rb') as sig_file:
        signature = sig_file.read()

    # Load the public key
    with open(public_key_path, 'rb') as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())

    # Verify signature
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
        print("\n✅ Signature verification passed: Integrity and authenticity verified.")
    except InvalidSignature:
        print("\n❌ Signature verification failed: File has been tampered with or public key is invalid.")
        os.remove(file_path)
        print("⚠️  The file has been deleted for security.")

if __name__ == "__main__":
    # Ask user to paste or enter paths (for cloned GitHub repo, use relative paths)
    file_path = input("Enter the path to the file you received (e.g., agreement.pdf): ").strip()
    signature_path = input("Enter the path to the signature file (e.g., signature.sig): ").strip()
    public_key_path = input("Enter the path to the sender's public key (e.g., public.pem): ").strip()

    verify_signature(file_path, signature_path, public_key_path)

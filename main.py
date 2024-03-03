import base64
import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

while True:
    # RSA鍵ペアの生成
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=1024,
        backend=default_backend()
    )

    # .onionドメインの生成
    public_key = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.PKCS1
    )
    digest = hashlib.sha1(public_key).digest()
    onion_address = base64.b32encode(digest[:10]).decode().lower()

    # .onionドメインが特定の文字列を含むかチェック
    if "su" in onion_address:
        onion_address += ".onion"
        print("Onion Address:", onion_address)
        print("---------------------------")
        print(public_key)
        print("---------------------------")
        print(private_key)
        break
        

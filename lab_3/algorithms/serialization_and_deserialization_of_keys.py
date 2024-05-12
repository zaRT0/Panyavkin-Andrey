import json

from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


def serialize_symmetric_key_to_file(file_path: str, key: bytes):
    with open(file_path, "wb") as key_file:
        key_file.write(key)


def deserialize_symmetric_key_to_file(file_path: str):
    with open(file_path, mode="rb") as key_file:
        d_symmetric_key = key_file.read()
        return d_symmetric_key
    

def serialize_asymmetric_public_key(public_pem: str, public_key: rsa.RSAPublicKey):
    with open(public_pem, 'wb') as public_out:
        public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
             format=serialization.PublicFormat.SubjectPublicKeyInfo))
        

def serialize_asymmetric_private_key(private_pem: str, private_key: rsa.RSAPrivateKey):
    with open(private_pem, 'wb') as private_out:
        private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
              format=serialization.PrivateFormat.TraditionalOpenSSL,
              encryption_algorithm=serialization.NoEncryption()))
        

def deserialize_asymmetric_public_key(public_pem: str):
    with open(public_pem, 'rb') as pem_in:
        public_bytes = pem_in.read()
    d_public_key = load_pem_public_key(public_bytes)
    return d_public_key


def deserialize_asymmetric_private_key(private_pem: str):
    with open(private_pem, 'rb') as pem_in:
        private_bytes = pem_in.read()
    d_private_key = load_pem_private_key(private_bytes,password=None,)
    return d_private_key
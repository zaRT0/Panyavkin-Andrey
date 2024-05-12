import json

from cryptography.hazmat.primitives.serialization import (
    load_pem_public_key,
    load_pem_private_key,
)
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


def serialize_symmetric_key_to_file(file_path: str, key: bytes) -> None:
    """
    Serialize a symmetric key to a file.
    args: file_path (str), key (bytes)
    returns: none
    """
    try:
        with open(file_path, "wb") as key_file:
            key_file.write(key)
    except Exception as e:
        print("An error occurred:", e)


def deserialize_symmetric_key_to_file(file_path: str) -> bytes:
    """
    Deserialize a symmetric key to a file.
    args: file_path (str)
    кeturns: bytes
    """
    try:
        with open(file_path, mode="rb") as key_file:
            d_symmetric_key = key_file.read()
            return d_symmetric_key
    except Exception as e:
        print("An error occurred:", e)


def serialize_asymmetric_public_key(public_pem: str, public_key: rsa.RSAPublicKey) -> None:
    """
    Serialize an asymmetric public key to a PEM file
    args: public_pem (str), public_key (rsa.RSAPublicKey)
    returns: none
    """
    try:
        with open(public_pem, "wb") as public_out:
            public_out.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            )
    except Exception as e:
        print("An error occurred:", e)


def serialize_asymmetric_private_key(private_pem: str, private_key: rsa.RSAPrivateKey) -> None:
    """
    Serialize an asymmetric private key to a PEM file
    args:private_pem (str), private_key (rsa.RSAPrivateKey)
    returns: none
    """
    try:
        with open(private_pem, "wb") as private_out:
            private_out.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption(),
                )
            )
    except Exception as e:
        print("An error occurred:", e)


def deserialize_asymmetric_public_key(public_pem: str) -> rsa.RSAPublicKey:
    """
    Deserialize an asymmetric public key from a PEM file.
    args: public_pem (str)
    returns: rsa.RSAPublicKey
    """
    try:
        with open(public_pem, "rb") as pem_in:
            public_bytes = pem_in.read()
        d_public_key = load_pem_public_key(public_bytes)
        return d_public_key
    except Exception as e:
        print("An error occurred:", e)


def deserialize_asymmetric_private_key(private_pem: str) -> rsa.RSAPrivateKey:
    """
    Deserialize an asymmetric private key from a PEM file.
    args: private_pem (str)
    returns: rsa.RSAPrivateKey
    """
    try:
        with open(private_pem, "rb") as pem_in:
            private_bytes = pem_in.read()
        d_private_key = load_pem_private_key(
            private_bytes,
            password=None,
        )
        return d_private_key
    except Exception as e:
        print("An error occurred:", e)
        return None

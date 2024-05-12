from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa

from algorithms.reading_and_writing_data import write_key_bytes
from algorithms.serialization_and_deserialization_of_keys import (
    deserialize_asymmetric_public_key,
    deserialize_asymmetric_private_key,
    deserialize_symmetric_key_to_file,
    serialize_symmetric_key_to_file,
)


class AsymmetricAlgorithm:
    def create_asymmetric_key(self):
        keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        private_key = keys
        public_key = keys.public_key()
        return public_key, private_key

    def encrypt_symmetric__key_with_public_key(
        self, public_key_path, symmetric_key_path, encrypted_symmetric_key_path
    ):
        symmetric_key = deserialize_symmetric_key_to_file(symmetric_key_path)
        public_key = deserialize_asymmetric_public_key(public_key_path)
        encrypted_key = public_key.encrypt(
            symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        write_key_bytes(encrypted_symmetric_key_path, encrypted_key)

    def decrypt_symmetric__key_with_private_key(
        self,
        encrypted_symmetric_key_path,
        private_key_path,
        decrypted_symmetric_key_path,
    ):
        encrypted_sym_key = deserialize_symmetric_key_to_file(
            encrypted_symmetric_key_path
        )
        private_key = deserialize_asymmetric_private_key(private_key_path)
        encrypted_symmetric_key = private_key.decrypt(
            encrypted_sym_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        serialize_symmetric_key_to_file(
            decrypted_symmetric_key_path, encrypted_symmetric_key
        )
        return encrypted_symmetric_key

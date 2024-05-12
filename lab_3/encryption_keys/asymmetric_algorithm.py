from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa

from reading_and_writing_data import write_key_bytes
from serialization_and_deserialization_of_keys import deserialize_asymmetric_public_key, deserialize_asymmetric_private_key, deserialize_symmetric_key_to_file, serialize_symmetric_key_to_file, write_key_bytes

class AsymmetricCryptography:
    def create_asymmetric_key(self):
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        private_key = keys
        public_key = keys.public_key()
        return private_key, public_key
    
    
    def encrypt_symmetric__key_with_public_key(self):
        
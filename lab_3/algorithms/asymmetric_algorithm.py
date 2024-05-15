from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa

from algorithms.reading_and_writing_data import Functions
from algorithms.serialization_and_deserialization_of_keys import Serializations


class AsymmetricAlgorithm:
    def create_asymmetric_key(self) -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
        """
        generate two asymmetric key (public and private)
        args: self
        return: _type_: _description_
        """
        try:
            keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
            private_key = keys
            public_key = keys.public_key()
            return public_key, private_key
        except Exception as e:
            raise RuntimeError(f"Failed to generate asymmetric keys: {e}")

    def encrypt_symmetric__key_with_public_key(
        self, public_key_path, symmetric_key_path, encrypted_symmetric_key_path
    ) -> None:
        """
        this method encrypt symmetric key by using asymmetric public key
        arg: public_key_path (str), symmetric_key_path (str), encrypted_symmetric_key_path (str)
        return: None
        """
        try:
            symmetric_key = Serializations.deserialize_symmetric_key_to_file(
                symmetric_key_path
            )
            public_key = Serializations.deserialize_asymmetric_public_key(
                public_key_path
            )
            encrypted_key = public_key.encrypt(
                symmetric_key,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
            Functions.write_key_bytes(encrypted_symmetric_key_path, encrypted_key)
        except Exception as e:
            raise RuntimeError(f"Failed to encrypt symmetric key with public key: {e}")

    def decrypt_symmetric__key_with_private_key(
        self,
        encrypted_symmetric_key_path,
        private_key_path,
        decrypted_symmetric_key_path,
    ) -> bytes:
        """
        this method decrypt symmetric key by using private asymmetric key
        arg: encrypted_symmetric_key_path (str), private_key_path (str), decrypted_symmetric_key_path (str)=
        return: bytes
        """
        try:
            encrypted_sym_key = Serializations.deserialize_symmetric_key_to_file(
                encrypted_symmetric_key_path
            )
            private_key = Serializations.deserialize_asymmetric_private_key(
                private_key_path
            )
            encrypted_symmetric_key = private_key.decrypt(
                encrypted_sym_key,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
            Serializations.serialize_symmetric_key_to_file(
                decrypted_symmetric_key_path, encrypted_symmetric_key
            )
            return encrypted_symmetric_key
        except Exception as e:
            raise RuntimeError(f"Failed to decrypt symmetric key: {e}")

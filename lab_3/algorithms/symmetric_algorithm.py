import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

from algorithms.reading_and_writing_data import Functions
from algorithms.serialization_and_deserialization_of_keys import Serializations


class SymmetricAlgorithm:
    """
    class for a symmetric algorithm
    methods:
        create_symmetric_key: generate symmetric key
        encrypting_text_using_symmetric_key: method for encrypting text by using symmetric key
        dencrypting_text_using_symmetric_key: method for decrypting text by using symmetric key
    """
    def create_symmetric_key(self) -> bytes:
        """
        generate key
        args: self
        return: bytes
        """
        key = os.urandom(16)
        return key

    def encrypting_text_using_symmetric_key(
        self, symmetric_key_path: str, text_path: str, encrypted_text_path: str
    ) -> bytes:
        """
        method for encrypting text by using symmetric key
        args: symmetric_key_path(str), description_text_path (str), description_encrypted_text_path (str)
        return: bytes
        """
        try:
            iv = os.urandom(16)
            symmetric_key = Serializations.deserialize_symmetric_key_to_file(symmetric_key_path)
            text = Functions.read_text_file(text_path)
            cipher = Cipher(algorithms.SEED(symmetric_key), modes.CBC(iv))
            padder = padding.PKCS7(128).padder()
            text_on_bytes = bytes(text, "UTF-8")
            p_text = padder.update(text_on_bytes) + padder.finalize()
            encryptor = cipher.encryptor()
            encrypt_text = encryptor.update(p_text) + encryptor.finalize()
            encrypt_text = iv + encrypt_text
            Functions.write_key_bytes(encrypted_text_path, encrypt_text)
            return encrypt_text
        except Exception as e:
            raise RuntimeError(f"Failed to encrypt text: {e}")

    def dencrypting_text_using_symmetric_key(
        self,
        symmetric_key_path: str,
        encrypted_text_path: str,
        dencrypted_text_path: str,
    ) -> str:
        """
        method for decrypting text by using symmetric key
        args: symmetric_key_path (str), encrypted_text_path: (str), dencrypted_text_path: (str)
        return: str
        """
        try:
            text = Functions.read_key_bytes(encrypted_text_path)
            size_key = 16
            iv = text[:size_key]
            encrypted_text = text[size_key:]
            symmetric_key = Serializations.deserialize_symmetric_key_to_file(symmetric_key_path)
            cipher = Cipher(algorithms.SEED(symmetric_key), modes.CBC(iv))
            decryptor = cipher.decryptor()
            dc_text = decryptor.update(encrypted_text) + decryptor.finalize()
            unpadder = padding.PKCS7(size_key * 8).unpadder()
            unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()
            new_unpadded_text = unpadded_dc_text.decode("UTF-8")
            Functions.write_text_file(dencrypted_text_path, new_unpadded_text)
            return new_unpadded_text
        except Exception as e:
            raise RuntimeError(f"Failed to decrypt text: {e}")

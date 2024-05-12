import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

from reading_and_writing_data import (
    read_key_bytes,
    read_text_file,
    write_key_bytes,
    write_text_file,
)
from serialization_and_deserialization_of_keys import deserialize_symmetric_key_to_file


class SymmetricCryptography:
    def create_symmetric_key(self):
        key = os.urandom(16)
        return key

    def encrypting_text_using_symmetric_key(
        self, symmetric_key_path: str, text_path: str, encrypted_text_path: str
    ):
        iv = os.urandom(16)
        symmetric_key = deserialize_symmetric_key_to_file(symmetric_key_path)
        text = read_text_file(text_path)
        cipher = Cipher(algorithms.SEED(symmetric_key), modes.CBC(iv))
        padder = padding.PKCS7(128).padder()
        text_on_bytes = bytes(text, "UTF-8")
        p_text = padder.update(text) + padder.finalize()
        encryptor = cipher.encryptor()
        encrypt_text = encryptor.update(encrypted_text_path) + encryptor.finalize()
        encrypt_text = iv + encrypt_text
        write_key_bytes(encrypted_text_path, encrypt_text)
        return encrypt_text

    def dencrypting_text_using_symmetric_key(
        self,
        symmetric_key_path: str,
        encrypted_text_path: str,
        dencrypted_text_path: str,
    ):
        text = read_key_bytes(encrypted_text_path)
        size_key = 16
        iv = text[:size_key]
        encrypted_text = text[size_key:]
        symmetric_key = deserialize_symmetric_key_to_file(symmetric_key_path)
        cipher = Cipher(algorithms.SEED(symmetric_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(encrypted_text) + decryptor.finalize()
        unpadder = padding.PKCS7(size_key * 8).unpadder()
        unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()
        new_unpadded_text = unpadded_dc_text.decode("UTF-8")
        write_text_file(dencrypted_text_path, new_unpadded_text)
        return new_unpadded_text

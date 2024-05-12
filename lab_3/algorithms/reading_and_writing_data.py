import json

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


class FileHandler:
    def read_json_file(file_path: str) -> dict:
        """
        a method for reading paths from a json file
        parametrs: file_path as str
        return: dict
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print("Файл не найден.")
        except json.JSONDecodeError:
            print("Ошибка при декодировании JSON-данных.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def read_key_bytes(file_path: str) -> bytes:
        """_summary_
        parametrs: file_path as str
        return: bytes
        """
        try:
            with open(file_path, "rb") as file:
                data = file.read()
            return data
        except FileNotFoundError:
            print("File not found.")
            return b""
        except Exception as e:
            print("An error occurred:", e)
            return b""

    def read_text_file(file_path: str) -> str:
        """
        Read text from a file
        parameters: file_path as str
        return: str
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = file.read()
            return data
        except FileNotFoundError:
            print("Файл не найден.")
            return ""
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return ""

    def write_key_bytes(file_path: str, bytes_text: bytes) -> None:
        """
        writes key bytes
        Args:file_path as str , bytes_text as bytes
        return none
        """
        try:
            with open(file_path, "wb") as file:
                file.write(bytes_text)
        except Exception as e:
            print("An error occurred:", e)

    def write_text_file(file_path: str, info: str) -> None:
        """
        writes text files
        Args: file_path as str, info as str
        return: none
        """
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(info)
        except Exception as e:
            print("An error occurred:", e)

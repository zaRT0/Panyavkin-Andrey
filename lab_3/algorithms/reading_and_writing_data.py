import json

from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


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
    with open(file_path, "rb") as file:
        data = file.read()
    return data


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
    with open(file_path, "wb") as file:
        file.write(bytes_text)
    
    
def write_text_file(file_path: str, info: str) -> None:
    with open(file_path, "w", encoding='utf-8') as file:
        file.write(info)
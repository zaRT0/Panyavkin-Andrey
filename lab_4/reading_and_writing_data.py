import json


class Functions:
    """
    this class contains contains function for works with text and files
    methods:
        read_json_file: reading json file
        write_text_file: method for a writing text files
    """

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


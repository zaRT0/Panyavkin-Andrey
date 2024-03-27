import os
import json

from work_with_json2 import read_json_file
from constants2 import PATHS2

from collections import Counter

def read_text_file(file_path: str) -> str:
    """
    Read text from a file.
    Parameters:
        file_path (str): Path to the text file.
    Returns:
        str: Contents of the text file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Файл не найден.")
        return ""
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return ""

def character_frequency(text: str) -> dict:
    """
    Calculate the frequency of each character in the text.
    Parameters:
        text (str): Input text.
    Returns:
        dict: A dictionary where keys are characters and values are their frequencies.
    """
    return dict(Counter(text))

def main():
    json_data = read_json_file(PATHS2)
    if json_data:
        folder_path = json_data.get("folder")
        input_file = json_data.get("input")

        input_file_path = folder_path + "/" + input_file

        text = read_text_file(input_file_path)
        if text:
            frequencies = character_frequency(text)

            total_chars = sum(frequencies.values())

            sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

            for char, freq in sorted_frequencies:
                decimal_freq = freq / total_chars
                print(f"Символ '{char}': {decimal_freq:.4f}")




if __name__ == "__main__":
    main()
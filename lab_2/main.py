import json

from scipy.special import erfc
from mpmath import gammainc
from math import sqrt, factorial
from constants import BLOCK_SIZE, PI_VALUES, PATH


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


def frequency_bit_test(sequence: str) -> float:
    """
    frequency bit test function
    param: sequence as str
    return: p-value
    """
    try:
        N = len(sequence)
        Sn = sum(1 if bit == "1" else -1 for bit in sequence) / sqrt(N)
        p_value = erfc(Sn / sqrt(2))
        return p_value
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def consecutive_bits_test(sequence: str) -> float:
    """
    consecutive bit test function
    param: sequence as str
    return: p-value
    """
    try:
        N = len(sequence)
        proportion_of_ones = sequence.count("1") / N
        if abs(proportion_of_ones - 0.5) >= 2 / sqrt(N):
            return 0
        Vn = sum(1 if sequence[i] != sequence[i + 1] else 0 for i in range(N - 1))
        p_value = erfc(
            (abs(Vn - 2 * N * proportion_of_ones * (1 - proportion_of_ones)))
            / (2 * sqrt(2 * N) * proportion_of_ones * (1 - proportion_of_ones))
        )
        return p_value
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def long_sequence_units_test(sequence: str) -> float:
    """
    long sequence units test function
    param: sequence as str
    return: p-value
    """
    try:
        blocks = [
            sequence[i : i + BLOCK_SIZE] for i in range(0, len(sequence), BLOCK_SIZE)
        ]
        statistics = {"v1": 0, "v2": 0, "v3": 0, "v4": 0}
        for block in blocks:
            max_ones = 0
            current_ones = 0
            for bit in block:
                if bit == "1":
                    current_ones += 1
                    max_ones = max(max_ones, current_ones)
                else:
                    current_ones = 0
            if max_ones <= 1:
                statistics["v1"] += 1
            elif max_ones == 2:
                statistics["v2"] += 1
            elif max_ones == 3:
                statistics["v3"] += 1
            else:
                statistics["v4"] += 1
        chi_square = sum(
            ((statistics[f"v{i+1}"] - 16 * PI_VALUES[i]) ** 2) / (16 * PI_VALUES[i])
            for i in range(4)
        )
        p_value = gammainc(1.5, chi_square / 2)
        return p_value
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main() -> None:
    data = read_json_file(PATH)
    for language, sequence in data.items():
        p_value_frequency_bit_test = frequency_bit_test(sequence)
        p_value_consecutive_bits_test = consecutive_bits_test(sequence)
        p_value_long_sequence_units_test = long_sequence_units_test(sequence)
        print(f"Язык: {language}")
        print(f"p-value frequency_bit_test: {p_value_frequency_bit_test}")
        print(f"p-value p_value_consecutive_bits_test: {p_value_consecutive_bits_test}")
        print(
            f"p-value p_value_long_sequence_units_test: {p_value_long_sequence_units_test}"
        )
        print()


if __name__ == "__main__":
    main()

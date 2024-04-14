import math
import json

from scipy.special import erfc
from mpmath import gammainc
from math import sqrt, factorial
from work_with_json_file import read_json_file

def frequency_bit_test(sequence: str) -> float:
    N = len(sequence)
    Sn = sum(1 if bit == '1' else -1 for bit in sequence) / sqrt(N)
    p_value = erfc(Sn / sqrt(2))
    return p_value

def calculate_p_value(sequence: str) -> float:
    N = len(sequence)
    proportion_of_ones = sequence.count('1') / N
    if abs(proportion_of_ones - 0.5) >= 2 / sqrt(N):
        return 0
    Vn = sum(1 if sequence[i] != sequence[i + 1] else 0 for i in range(N - 1))
    p_value = erfc((abs(Vn - 2 * N * proportion_of_ones * (1 - proportion_of_ones))) /
                   (2 * sqrt(2 * N) * proportion_of_ones * (1 - proportion_of_ones)))
    return p_value

def calculate_p_value_from_sequence(sequence: str) -> float:
    block_size = 8
    pi_values = [0.2148, 0.3672, 0.2305, 0.1875]
    blocks = [sequence[i:i+block_size] for i in range(0, len(sequence), block_size)]
    statistics = {'v1': 0, 'v2': 0, 'v3': 0, 'v4': 0}
    for block in blocks:
        max_ones = 0
        current_ones = 0
        for bit in block:
            if bit == '1':
                current_ones += 1
                max_ones = max(max_ones, current_ones)
            else:
                current_ones = 0
        if max_ones <= 1:
            statistics['v1'] += 1
        elif max_ones == 2:
            statistics['v2'] += 1
        elif max_ones == 3:
            statistics['v3'] += 1
        else:
            statistics['v4'] += 1
    chi_square = sum(((statistics[f'v{i+1}'] - 16 * pi_values[i]) ** 2) / (16 * pi_values[i]) for i in range(4))
    p_value = gammainc(1.5, chi_square / 2)
    return p_value

def process_sequences_combined(file_path: str):
    data = read_json_file(file_path)
    for language, sequence in data.items():
        p_value_frequency_bit_test = frequency_bit_test(sequence)
        p_value_calculate_p_value = calculate_p_value(sequence)
        p_value_calculate_p_value_from_sequence = calculate_p_value_from_sequence(sequence)
        print(f"Язык: {language}")
        print(f"p-value frequency_bit_test: {p_value_frequency_bit_test}")
        print(f"p-value calculate_p_value: {p_value_calculate_p_value}")
        print(f"p-value calculate_p_value_from_sequence: {p_value_calculate_p_value_from_sequence}")
        print()

def main():
    file_path = "lab_2/binary_sequence.json"
    process_sequences_combined(file_path)

if __name__ == "__main__":
    main()
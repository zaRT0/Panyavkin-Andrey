import hashlib
import multiprocessing as mp
import logging
import time

from matplotlib import pyplot as plt

from reading_and_writing_data import Functions
from constants import PATH, DATA


class Hash:
    def card_number_checking(
        hash: str, bin: tuple, middle_numbers: int, last_numbers: str
    ) -> str:
        """
        This method is checking card numbers
        param: hash as (str),  bin as (tuple), middle_numbers as (int), last_numbers as (str)
        return: str
        """
        for first_numbers in bin:
            card_number = f"{first_numbers}{middle_numbers:06d}{last_numbers}"
            if hashlib.sha224(card_number.encode()).hexdigest() == hash:
                return card_number

    def create_card_number(hash: str, bin: tuple, last_numbers: str) -> str:
        """
        This method creating card number
        param: hash as (str),  bin as (tuple), last_numbers as (str)
        return: str
        """
        with mp.Pool(processes=mp.cpu_count()) as p:
            for result in p.starmap(
                Hash.card_number_checking,
                (
                    (hash, bin, middle_numbers, last_numbers)
                    for middle_numbers in range(0, 999999)
                ),
            ):
                if result:
                    p.terminate()
                    break
        return result

    def luhns_algorithm(card_number: str) -> bool:
        """
        This method is checking card numbers for an accuracy
        param: card_nuber (str)
        return: bool
        """
        digits = [int(digit) for digit in card_number]
        for i in range(len(digits) - 2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
        total = sum(digits)
        return total % 10 == 0

    def time_for_find_collisions(
        hash: str, last_numbers: str, bin: tuple, path: str
    ) -> None:
        """
        This method marks the time of collisions
        param: hash as (str), last_numbers as (str), bin as (tuple), path as (str)
        return: None
        """
        collision_time = [[], []]
        for cores in range(1, int(mp.cpu_count() * 1.5)):
            start = time.time()
            with mp.Pool(processes=mp.cpu_count()) as p:
                for result in p.starmap(
                    Hash.card_number_checking,
                    (
                        (hash, bin, middle_numbers, last_numbers)
                        for middle_numbers in range(0, 999999)
                    ),
                ):
                    if result:
                        p.terminate()
                        break
            end = time.time() - start
            collision_time[0].append(cores)
            collision_time[1].append(end)
        Hash.create_graphic_of_collision_time(collision_time, path)

    def create_graphic_of_collision_time(collisions_time: tuple, path: str) -> None:
        """
        This method creates graphivs of a time collision
        param: collisions_time as (tuple), path as (str)
        return: None
        """
        cores = collisions_time[0]
        times = collisions_time[1]

        min_time_index = times.index(min(times))
        min_time_core = cores[min_time_index]
        min_time = times[min_time_index]

        plt.figure(figsize=(10, 6))
        plt.plot(
            cores,
            times,
            marker="o",
            linestyle="-",
            color="b",
            label="Time per number of cores",
        )
        plt.scatter(min_time_core, min_time, color="r", zorder=5)
        plt.annotate(
            f"Min Time: {min_time:.2f} s\nCores: {min_time_core}",
            xy=(min_time_core, min_time),
            xytext=(min_time_core + 0.5, min_time + 0.5),
            arrowprops=dict(facecolor="black", shrink=0.05),
        )

        plt.xlabel("Number of Cores")
        plt.ylabel("Collision Time (seconds)")
        plt.title("Collision Time vs Number of Cores")
        plt.legend()
        plt.grid(True)

        plt.savefig(path)
        plt.close()


if __name__ == "__main__":
    data = Functions.read_json_file(DATA)

    test_hash = data.get("hash", "")
    test_last_numbers = data.get("last_four_numbers", "")
    test_bin = tuple(data.get("bin", []))

    created_card_number = Hash.create_card_number(
        test_hash, test_bin, test_last_numbers
    )

    print("Созданный номер карты:", created_card_number)

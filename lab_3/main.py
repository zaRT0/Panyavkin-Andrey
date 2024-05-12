import argparse

from algorithms.asymmetric_algorithm import AsymmetricAlgorithm
from algorithms.symmetric_algorithm import SymmetricAlgorithm
from algorithms.serialization_and_deserialization_of_keys import (
    serialize_symmetric_key_to_file,
    serialize_asymmetric_public_key,
    serialize_asymmetric_private_key,
)
from algorithms.reading_and_writing_data import read_json_file


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-gen_s", "--generation_symmetric", help="symmetric key generation"
    )
    group.add_argument(
        "-gen_a", "--generation_asymmetric", help="asymmetric key generation"
    )
    group.add_argument("-enc", "--ecryption_text", help="encryption text file")
    group.add_argument("-dec", "--decryption_text", help="decryption text file")
    group.add_argument(
        "-enc_sym", "--ecryption_symmetric_key", help="ecryption symmetric key"
    )
    group.add_argument(
        "-dec_sym", "--decryption_symmetric_key", help="decryption symmetric key"
    )
    parser.add_argument(
        "setting", type=str, help="Path to the json file with the settings"
    )

    args = parser.parse_args()
    symmetric = SymmetricAlgorithm()
    asymmetric = AsymmetricAlgorithm()
    setting = read_json_file(args.setting)

    match args:
        case args if args.generation_symmetric:
            symmetric_key = symmetric.create_symmetric_key()
            serialize_symmetric_key_to_file(setting["symmetric_key"], symmetric_key)
        case args if args.generation_asymmetric:
            public_key, private_key = asymmetric.create_asymmetric_key()
            serialize_asymmetric_public_key(
                setting["asymmetric_public_key"], public_key
            )
            serialize_asymmetric_private_key(
                setting["asymmetric_private_key"], private_key
            )
        case args if args.ecryption_text:
            encrypted_text = symmetric.encrypting_text_using_symmetric_key(
                setting["symmetric_key"],
                setting["initial_file"],
                setting["encrypted_file"],
            )
            print("Зашифрованный текст: {encrypted_text}")
        case args if args.decryption_text:
            decrypted_text = symmetric.dencrypting_text_using_symmetric_key(
                setting["symmetric_key"],
                setting["encrypted_file"],
                setting["decrypted_file"],
            )
            print(f"Расшифрованный текст: {decrypted_text}")
        case args if args.ecryption_symmetric_key:
            asymmetric.encrypt_symmetric__key_with_public_key(
                setting["asymmetric_public_key"],
                setting["symmetric_key"],
                setting["encrypted_symmetric_key"],
            )
        case args if args.decryption_symmetric_key:
            asymmetric.decrypt_symmetric__key_with_private_key(
                setting["encrypted_symmetric_key"],
                setting["asymmetric_private_key"],
                setting["decrypted_symmetric_key"],
            )


if __name__ == "__main__":
    main()

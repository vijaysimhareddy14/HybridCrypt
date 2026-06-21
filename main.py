from cipher import encrypt
from cipher import decrypt

from key_schedule import generate_round_keys

from avalanche import avalanche_test

from file_crypto import (
    encrypt_file,
    decrypt_file
)

from rsa import (
    generate_keys
)

from hybrid_crypto import (
    hybrid_encrypt_file,
    hybrid_decrypt_file
)

public_key, private_key = generate_keys()


def menu():

    while True:

        print("\n===== HybridCrypt =====")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Avalanche Test")
        print("4. Encrypt File")
        print("5. Decrypt File")
        print("6. Hybrid Encrypt File")
        print("7. Hybrid Decrypt File")
        print("8. Exit")

        choice = input("Choice: ")

        if choice == "1":

            plaintext = input(
                "Plaintext: "
            )

            key = input(
                "Key: "
            )

            round_keys = generate_round_keys(
                key
            )

            encrypted = encrypt(
                plaintext,
                round_keys
            )

            print(
                encrypted.hex()
            )

        elif choice == "2":

            cipher_hex = input(
                "Cipher Hex: "
            )

            key = input(
                "Key: "
            )

            round_keys = generate_round_keys(
                key
            )

            plaintext = decrypt(
                bytes.fromhex(
                    cipher_hex
                ),
                round_keys
            )

            print(
                plaintext
            )

        elif choice == "3":

            text = input(
                "Text: "
            )

            key = input(
                "Key: "
            )

            changed, total, percent = avalanche_test(
                text,
                key
            )

            print(
                f"\nChanged Bits : {changed}"
            )

            print(
                f"Total Bits   : {total}"
            )

            print(
                f"Avalanche %  : {percent:.2f}"
            )

        elif choice == "4":

            input_file = input(
                "Input File: "
            )

            output_file = input(
                "Output File: "
            )

            key = input(
                "Key: "
            )

            encrypt_file(
                input_file,
                output_file,
                key
            )

        elif choice == "5":

            input_file = input(
                "Encrypted File: "
            )

            output_file = input(
                "Output File: "
            )

            key = input(
                "Key: "
            )

            decrypt_file(
                input_file,
                output_file,
                key
            )

        elif choice == "6":

            input_file = input(
                "Input File: "
            )

            output_file = input(
                "Output File: "
            )

            hybrid_encrypt_file(
                input_file,
                output_file,
                public_key
            )

        elif choice == "7":

            input_file = input(
                "Encrypted File: "
            )

            output_file = input(
                "Output File: "
            )

            hybrid_decrypt_file(
                input_file,
                output_file,
                private_key
            )

        elif choice == "8":

            break

        else:

            print(
                "Invalid choice"
            )


if __name__ == "__main__":
    menu()
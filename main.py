from cipher import encrypt
from cipher import decrypt

from key_schedule import generate_round_keys

from avalanche import avalanche_test

from file_crypto import (
    encrypt_file,
    decrypt_file
)


def menu():

    while True:

        print("\n===== HybridCrypt =====")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Avalanche Test")
        print("4. Encrypt File")
        print("5. Decrypt File")
        print("6. Exit")

        choice = input("Choice: ")

        if choice == "1":

            plaintext = input(
                "Enter plaintext: "
            )

            key = input(
                "Enter key: "
            )

            round_keys = generate_round_keys(
                key
            )

            encrypted = encrypt(
                plaintext,
                round_keys
            )

            print(
                "\nCipher (hex):",
                encrypted.hex()
            )

        elif choice == "2":

            cipher_hex = input(
                "Enter cipher hex: "
            )

            key = input(
                "Enter key: "
            )

            round_keys = generate_round_keys(
                key
            )

            cipher_bytes = bytes.fromhex(
                cipher_hex
            )

            decrypted = decrypt(
                cipher_bytes,
                round_keys
            )

            print(
                "\nPlaintext:",
                decrypted
            )

        elif choice == "3":

            text = input(
                "Enter text: "
            )

            key = input(
                "Enter key: "
            )

            changed, total, percent = avalanche_test(
                text,
                key
            )

            print("\nChanged Bits :", changed)
            print("Total Bits   :", total)
            print(
                "Avalanche %  :",
                round(percent, 2)
            )

        elif choice == "4":

            input_file = input(
                "Input file: "
            )

            output_file = input(
                "Output file: "
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
                "Encrypted file: "
            )

            output_file = input(
                "Output file: "
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

            print("Bye")
            break

        else:

            print("Invalid option")


if __name__ == "__main__":
    menu()
from cipher import encrypt
from cipher import decrypt

from key_schedule import generate_round_keys

from avalanche import avalanche_test


def menu():

    while True:

        print("\n===== HybridCrypt =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Avalanche Test")
        print("4. Exit")

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

            print("Bye")
            break

        else:

            print("Invalid option")


if __name__ == "__main__":
    menu()
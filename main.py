from cipher import encrypt
from cipher import decrypt
from key_schedule import generate_round_keys


def menu():

    while True:

        print()
        print("===== HybridCrypt =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Choice: ")

        if choice == "1":

            text = input(
                "Enter plaintext: "
            )

            key = input(
                "Enter key: "
            )

            round_keys = generate_round_keys(
                key
            )

            encrypted = encrypt(
                text,
                round_keys
            )

            print()
            print(
                "Cipher (hex):",
                encrypted.hex()
            )

        elif choice == "2":

            cipher_hex = input(
                "Cipher hex: "
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

            print()
            print(
                "Plaintext:",
                decrypted
            )

        elif choice == "3":

            print("Bye")
            break

        else:

            print("Invalid option")


if __name__ == "__main__":
    menu()
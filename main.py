from Lab1 import CeaserCipher
from Lab3 import PlayFair

if __name__ == '__main__':
    # LABORATORY WORK 2
    play_fair = PlayFair()
    alphabet = [c for c in "AĂÂBCDEFGHIÎKLMNOPQRSȘTȚUVWXYZ"]

    while True:
        print("\nChoose an option:")
        print("1. Encrypt with PlayFair")
        print("2. Decrypt with PlayFair")
        print("3. Exit")
        print("=" * 70)

        option = input("\nYour choice (1-3): ").strip()

        if option not in ["1", "2", "3"]:
            print("\nError: Invalid option. Please choose 1, 2, or 3.")
            continue

        option = int(option)

        # ENCRYPTION
        if option == 1:

            # Input message
            while True:
                print("\nInput the message to encrypt:")
                message = input().strip()
                if not message:
                    print("Error: Message cannot be empty.")
                    continue
                if not all(c.isalpha() or c.isspace() for c in message):
                    print("Error: Message must contain only letters and spaces.")
                    continue
                break

            # Input key
            while True:
                print("\nInput the encryption key (letters only, maximum 7 letters):")
                key = input().strip()
                if not key:
                    print("Error: Key cannot be empty.")
                    continue
                if not key.isalpha():
                    print("Error: Key must contain only letters.")
                    continue
                if len(key) > 7:
                    print("Error: Key must have maximum 7 letters.")
                    continue
                break

            # Step 1
            step1 = play_fair.substitute_letters_in_string(message)
            print(f"\n STEP 1: Convert to uppercase and replace J with I, remove spaces")
            print(f"  Result: {step1}")

            # Step 2
            step2 = play_fair.split_string_into_digraphs(step1)
            print(f"\n STEP 2: Split into pairs of 2 letters")
            print(f"  Result: {step2}")

            # Step 3
            step3 = play_fair.handle_double_letters(step2)
            step3_spaces = play_fair.split_string_into_digraphs(step3)
            print(f"\n STEP 3: Handle double letters (insert Q, X, or Z between same letters)")
            print(f"  Result: {step3_spaces}")

            # Step 4
            step4 = play_fair.handle_incomplete_pairs(step3)
            print(f"\n STEP 4: Handle incomplete pairs (add extra letter if needed)")
            print(f"  Result: {step4}")

            # Step 5
            print(f"\n STEP 5: Build Encryption Matrix from key")
            print(f"  Key used: {key.upper()}")
            encryption_matrix = play_fair.build_encryption_matrix(key, alphabet)

            # Step 6
            print(f"\n STEP 6: Encrypt the message using the matrix")
            play_fair.encrypt_string(step4, encryption_matrix)

        # DECRYPTION
        elif option == 2:

            # Input encrypted message
            while True:
                print("\nInput the encrypted message:")
                encrypted_message = input().strip()
                if not encrypted_message:
                    print("Error: Encrypted message cannot be empty.")
                    continue
                encrypted_message_clean = encrypted_message.replace(" ", "")
                if not encrypted_message_clean.isalpha():
                    print("Error: Encrypted message must contain only letters.")
                    continue
                if len(encrypted_message_clean) % 2 != 0:
                    print("Error: Encrypted message must have even number of letters.")
                    continue
                break

            # Input key
            while True:
                print("\nInput the decryption key (letters only, maximum 7 letters):")
                key = input().strip()
                if not key:
                    print("Error: Key cannot be empty.")
                    continue
                if not key.isalpha():
                    print("Error: Key must contain only letters.")
                    continue
                if len(key) > 7:
                    print("Error: Key must have maximum 7 letters.")
                    continue
                break

            # Step 1
            step1 = play_fair.split_string_into_digraphs(encrypted_message)
            print(f"\n STEP 1: Split encrypted message into pairs")
            print(f"  Result: {step1}")

            # Step 2
            print(f"\n STEP 2: Build Decryption Matrix from key")
            print(f"  Key used: {key.upper()}")
            encryption_matrix = play_fair.build_encryption_matrix(key, alphabet)

            # Step 3
            print(f"\n STEP 3: Decrypt the message using the matrix")
            play_fair.decrypt_string(encrypted_message, encryption_matrix)

        # EXIT
        elif option == 3:
            print("\nExiting...")
            break

    # # LABORATORY WORK 1
    # ceaser_cipher = CeaserCipher()
    # characters_list = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    # characters_codes_dict = {i: char for i, char in enumerate(characters_list)}
    #
    # while True:
    #     print("\nChoose an option:")
    #     print("1. Ceaser algorithm")
    #     print("2. Ceaser with 2 keys")
    #     print("3. Decrypt a predefined message")
    #     print("4. Exit")
    #     option = input("Your choice: ")
    #
    #     if option not in ["1", "2", "3", "4"]:
    #         print("Error: the option picked should be 1, 2, 3 or 4.")
    #         continue
    #
    #     option = int(option)
    #
    #     # PART 1
    #     if option == 1:
    #         print("\nCeaser algorithm:")
    #         print("1. Encrypt a message")
    #         print("2. Decrypt a message")
    #         option_part1 = input("Your choice: ")
    #         if option_part1 not in ["1", "2"]:
    #             print("Error: Incorrect choice. It should be 1 or 2.")
    #             continue
    #
    #         print("Input the message:")
    #         message_part1 = input()
    #         if not message_part1.isalpha():
    #             print("Error: Message must contain only letters.")
    #             continue
    #
    #         print("Input the key (1-25): ")
    #         key_part1_str = input()
    #         if not key_part1_str.isdigit():
    #             print("Error: Key should be a number.")
    #             continue
    #         key_part1 = int(key_part1_str)
    #         if key_part1 < 1 or key_part1 >= 26:
    #             print("Error: Wrong key. Key should be between 0 and 25.")
    #             continue
    #
    #         if option_part1 == "1":
    #             print("Encrypted:",
    #                   ceaser_cipher.encrypt_text(message_part1, key_part1, characters_list, characters_codes_dict))
    #         else:
    #             print("Decrypted:",
    #                   ceaser_cipher.decrypt_text(message_part1, key_part1, characters_list, characters_codes_dict))
    #
    #     # PART 2
    #     elif option == 2:
    #         print("\nCeaser with 2 keys:")
    #         print("1. Encrypt a message")
    #         print("2. Decrypt a message")
    #         option_part2 = input("Your choice: ")
    #         if option_part2 not in ["1", "2"]:
    #             print("Error: Incorrect choice. It should be 1 or 2.")
    #             continue
    #
    #         print("Input the message:")
    #         message_part2 = input()
    #         if not message_part2.isalpha():
    #             print("Error: Message must contain only letters.")
    #             continue
    #
    #         print("Input the first key (1-25): ")
    #         key1_part2_str = input()
    #         if not key1_part2_str.isdigit():
    #             print("Error: The first key should be a number.")
    #             continue
    #         key1_part2 = int(key1_part2_str)
    #         if key1_part2 < 1 or key1_part2 >= 26:
    #             print("Error: Wrong key. Key should be between 0 and 25.")
    #             continue
    #
    #         print("Input the second key (min 7 letters): ")
    #         key2_part2 = input()
    #         if len(key2_part2) < 7 or not key2_part2.isalpha():
    #             print("Error: Second key must have at least 7 letters and only letters.")
    #             continue
    #
    #         characters_codes_dict_2 = ceaser_cipher.add_second_key(key2_part2, characters_list)
    #         new_characters_list = list(characters_codes_dict_2.values())
    #         print(new_characters_list)
    #
    #         if option_part2 == "1":
    #             encrypted = ceaser_cipher.encrypt_text(message_part2, key1_part2, new_characters_list,
    #                                                    characters_codes_dict_2)
    #             print("Encrypted:", encrypted)
    #         else:
    #             decrypted = ceaser_cipher.decrypt_text(message_part2, key1_part2, new_characters_list,
    #                                                    characters_codes_dict_2)
    #             print("Decrypted:", decrypted)
    #
    #     # PART 3
    #     elif option == 3:
    #         message_to_decrypt = "ejqqhchtqi"
    #         key_for_message = 3
    #         key_for_message_2 = "cryptography"
    #
    #         characters_codes_dict_2 = ceaser_cipher.add_second_key(key_for_message_2, characters_list)
    #         new_characters_list = list(characters_codes_dict_2.values())
    #
    #         print(f"\nDecrypting the predefined message: {message_to_decrypt} with key1 = {key_for_message} and key2 = {key_for_message_2}")
    #         decrypted_message = ceaser_cipher.decrypt_text(message_to_decrypt, key_for_message, new_characters_list,
    #                                                        characters_codes_dict_2)
    #         print(f"Decrypted message: {decrypted_message}")
    #
    #     elif option == 4:
    #         print("Exiting program...")
    #         break

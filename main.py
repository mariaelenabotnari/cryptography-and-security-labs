from Lab1 import CeaserCipher

if __name__ == '__main__':
    # LABORATORY WORK 1
    ceaser_cipher = CeaserCipher()
    characters_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    characters_codes_dict = {i: char for i, char in enumerate(characters_list)}

    while True:
        print("\nChoose an option:")
        print("1. Ceaser algorithm")
        print("2. Ceaser with 2 keys")
        print("3. Decrypt a predefined message")
        print("4. Exit")
        option = input("Your choice: ")

        if option not in ["1", "2", "3", "4"]:
            print("Error: the option picked should be 1, 2, 3 or 4.")
            continue

        option = int(option)

        # PART 1
        if option == 1:
            print("\nCeaser algorithm:")
            print("1. Encrypt a message")
            print("2. Decrypt a message")
            option_part1 = input("Your choice: ")
            if option_part1 not in ["1", "2"]:
                print("Error: Incorrect choice. It should be 1 or 2.")
                continue

            print("Input the message:")
            message_part1 = input()
            if not message_part1.isalpha():
                print("Error: Message must contain only letters.")
                continue

            print("Input the key (0-25): ")
            key_part1_str = input()
            if not key_part1_str.isdigit():
                print("Error: Key should be a number.")
                continue
            key_part1 = int(key_part1_str)
            if key_part1 < 0 or key_part1 >= 26:
                print("Error: Wrong key. Key should be between 0 and 25.")
                continue

            if option_part1 == "1":
                print("Encrypted:",
                      ceaser_cipher.encrypt_text(message_part1, key_part1, characters_list, characters_codes_dict))
            else:
                print("Decrypted:",
                      ceaser_cipher.decrypt_text(message_part1, key_part1, characters_list, characters_codes_dict))

        # PART 2
        elif option == 2:
            print("\nCeaser with 2 keys:")
            print("1. Encrypt a message")
            print("2. Decrypt a message")
            option_part2 = input("Your choice: ")
            if option_part2 not in ["1", "2"]:
                print("Error: Incorrect choice. It should be 1 or 2.")
                continue

            print("Input the message:")
            message_part2 = input()
            if not message_part2.isalpha():
                print("Error: Message must contain only letters.")
                continue

            print("Input the first key (0-25): ")
            key1_part2_str = input()
            if not key1_part2_str.isdigit():
                print("Error: The first key should be a number.")
                continue
            key1_part2 = int(key1_part2_str)
            if key1_part2 < 0 or key1_part2 >= 26:
                print("Error: Wrong key. Key should be between 0 and 25.")
                continue

            print("Input the second key (min 7 letters): ")
            key2_part2 = input()
            if len(key2_part2) < 7 or not key2_part2.isalpha():
                print("Error: Second key must have at least 7 letters and only letters.")
                continue

            characters_codes_dict_2 = ceaser_cipher.add_second_key(key2_part2, characters_list)
            new_characters_list = list(characters_codes_dict_2.values())

            if option_part2 == "1":
                encrypted = ceaser_cipher.encrypt_text(message_part2, key1_part2, characters_list,
                                                       characters_codes_dict_2)
                print("Encrypted:", encrypted)
            else:
                decrypted = ceaser_cipher.decrypt_text(message_part2, key1_part2, new_characters_list,
                                                       characters_codes_dict)
                print("Decrypted:", decrypted)

        # PART 3
        elif option == 3:
            message_to_decrypt = "JRRGMRE"
            key_for_message = 3
            print(f"\nDecrypting the predefined message: {message_to_decrypt} with key {key_for_message}")
            decrypted_message = ceaser_cipher.decrypt_text(message_to_decrypt, key_for_message, characters_list,
                                                           characters_codes_dict)
            print(f"Decrypted message: {decrypted_message}")

        elif option == 4:
            print("Exiting program...")
            break

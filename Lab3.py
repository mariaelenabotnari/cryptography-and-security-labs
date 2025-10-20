import random

class PlayFair:

    def substitute_letters_in_string(self, string):
        string = string.upper().replace(' ', '')

        new_string = ''
        for char in string:
            if char == 'J':
                new_string += 'I'
            else:
                new_string += char

        return new_string

    def split_string_into_digraphs(self, string):
        string_no_spaces = string.replace(' ', '')
        digraphs_list = []

        for i in range(0, len(string_no_spaces), 2):
            digraph = string_no_spaces[i:i + 2]
            digraphs_list.append(digraph)

        new_string = " ".join(digraphs_list)

        return new_string

    def pick_letter(self):
        letters = ["Q", "X", "Z"]
        random_choice = random.choice(letters)
        return random_choice

    def handle_double_letters(self, string):
        string = string.replace(" ", "")

        i = 0
        new_string = ''
        while i < len(string):
            char1 = string[i]

            if i + 1 >= len(string):
                new_string += char1
                break

            char2 = string[i + 1]

            if char1 == char2:
                new_letter = self.pick_letter()
                while char1 == new_letter:
                    new_letter = self.pick_letter()
                new_string += char1 + new_letter
                i += 1
            else:
                new_string += char1 + char2
                i += 2

        return new_string

    def handle_incomplete_pairs(self, string):
        string_no_spaces = string.replace(' ', '')
        if len(string_no_spaces) % 2 == 1:
            new_letter = self.pick_letter()

            while string_no_spaces[-1] == new_letter:
                new_letter = self.pick_letter()

            string_no_spaces += new_letter

        return self.split_string_into_digraphs(string_no_spaces)

    def build_encryption_matrix(self, key, alphabet):
        key = key.upper().replace(" ", "").replace("J", "I")

        new_alphabet = []
        for char in key:
            if char not in new_alphabet:
                new_alphabet.append(char)

        for char in alphabet:
            if char not in new_alphabet:
                new_alphabet.append(char)

        encryption_matrix = []
        for i in range(0, len(new_alphabet), 6):
            row = new_alphabet[i:i + 6]
            encryption_matrix.append(row)

        print("Encryption Matrix:")
        for row in encryption_matrix:
            print(row)

        return encryption_matrix

    def find_position(self, char, encryption_matrix):
        for row_index, row in enumerate(encryption_matrix):
            for column_index, matrix_char in enumerate(row):
                if matrix_char == char:
                    return row_index, column_index

    def encrypt_pair(self, pair, encryption_matrix):
        first_char = pair[0]
        second_char = pair[1]

        first_char_position = self.find_position(first_char, encryption_matrix)
        second_char_position = self.find_position(second_char, encryption_matrix)

        r1, c1 = first_char_position
        r2, c2 = second_char_position

        if r1 == r2:
            encrypted_first = encryption_matrix[r1][(c1 + 1) % 6]
            encrypted_second = encryption_matrix[r2][(c2 + 1) % 6]

        elif c1 == c2:
            encrypted_first = encryption_matrix[(r1 + 1) % 5][c1]
            encrypted_second = encryption_matrix[(r2 + 1) % 5][c2]

        else:
            encrypted_first = encryption_matrix[r1][c2]
            encrypted_second = encryption_matrix[r2][c1]

        return encrypted_first + encrypted_second

    def encrypt_string(self, string, encryption_matrix):
        string_no_spaces = string.replace(' ', '')

        encrypted_string = ''
        for i in range(0, len(string_no_spaces), 2):
            current_pair = string_no_spaces[i:i + 2]
            encrypted_pair = self.encrypt_pair(current_pair, encryption_matrix)
            encrypted_string += encrypted_pair
        print(encrypted_string)

    def decrypt_pair(self, pair, encryption_matrix):
        first_char = pair[0]
        second_char = pair[1]

        first_char_position = self.find_position(first_char, encryption_matrix)
        second_char_position = self.find_position(second_char, encryption_matrix)

        r1, c1 = first_char_position
        r2, c2 = second_char_position

        if r1 == r2:
            encrypted_first = encryption_matrix[r1][(c1 - 1) % 6]
            encrypted_second = encryption_matrix[r2][(c2 - 1) % 6]

        elif c1 == c2:
            encrypted_first = encryption_matrix[(r1 - 1) % 5][c1]
            encrypted_second = encryption_matrix[(r2 - 1) % 5][c2]

        else:
            encrypted_first = encryption_matrix[r1][c2]
            encrypted_second = encryption_matrix[r2][c1]

        return encrypted_first + encrypted_second

    def decrypt_string(self, string, encryption_matrix):
        string_no_spaces = string.replace(' ', '')

        decrypted_string = ''
        for i in range(0, len(string_no_spaces), 2):
            current_pair = string_no_spaces[i:i + 2]
            decrypted_pair = self.decrypt_pair(current_pair, encryption_matrix)
            decrypted_string += decrypted_pair
        print(self.split_string_into_digraphs(decrypted_string))

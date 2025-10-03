
class CeaserCipher:

    def encrypt(self, char, key, characters_list):
        char_lower = char.upper()
        char_position = characters_list.index(char_lower)
        return (char_position + key) % 26

    def decrypt(self, char, key, characters_list):
        char_lower = char.upper()
        char_position = characters_list.index(char_lower)
        return (char_position - key) % 26

    def encrypt_text(self, text, key, characters_list, characters_codes_dict):
        text_modified = text.upper().strip()
        new_string = ''

        for char in text_modified:
            new_char_pos = self.encrypt(char, key, characters_list)
            new_char = characters_codes_dict.get(new_char_pos)
            new_string = new_string + new_char

        return new_string

    def decrypt_text(self, text, key, characters_list, characters_codes_dict):
        text_modified = text.upper().strip()
        new_string = ''

        for char in text_modified:
            new_char_pos = self.decrypt(char, key, characters_list)
            new_char = characters_codes_dict.get(new_char_pos)
            new_string = new_string + new_char

        return new_string

    def add_second_key(self, key2, characters_list):
        key2 = "".join(dict.fromkeys(key2.upper()))

        new_alphabet = key2 + "".join([c for c in characters_list if c not in key2])

        return {i: char for i, char in enumerate(new_alphabet)}



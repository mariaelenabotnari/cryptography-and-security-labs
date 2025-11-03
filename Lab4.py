import random
class DES:

    def generate_key(self):
        random_64_bit_number = random.getrandbits(56)
        binary_key = format(random_64_bit_number, '056b')

        return binary_key

    def convert_binary_to_hex(self, key):
        decimal_value = int(key, 2)
        hex_key = format(decimal_value, '016x')

        return hex_key

    def split_key_right_left_halves(self, key):
        middle = len(key) // 2
        C0 = key[:middle]
        D0 = key[middle:]

        return C0, D0

    def display_shift_table(self):
        shift_dict = {
            (1, 2, 9, 16): 1,
            tuple(i for i in range(1, 17) if i not in (1, 2, 9, 16)): 2
        }

        round_to_shift = {}
        for rounds, shift in shift_dict.items():
            for round in rounds:
                round_to_shift[round] = shift

        rounds_sorted = sorted(round_to_shift.keys())

        rounds_row = ' '.join(f"{r:>2}" for r in rounds_sorted)
        shifts_row = ' '.join(f"{round_to_shift[row]:>2}" for row in rounds_sorted)

        print(rounds_row)
        print(shifts_row)

        return shift_dict

    def display_pc_2_table(self):
        pc2 = [
            14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32
        ]

        print("\nPermutation Choice 2 (PC-2) Table")
        print("---------------------------------")

        for i in range(0, len(pc2), 6):
            row = pc2[i:i + 6]
            print('  '.join(f"{num:2}" for num in row))
        print("\n")
        return pc2

    def shift_right_left_half(self, round, left_half, right_half, shift_dictionary):
        shift_number = None
        for rounds, shift in shift_dictionary.items():
            if round in rounds:
                shift_number = shift
                break

        shifted_left_half = left_half[shift_number:] + left_half[:shift_number]
        shifted_right_half = right_half[shift_number:] + right_half[:shift_number]

        return shifted_left_half, shifted_right_half

    def permuted_choice_2(self, left_half, right_half, pc_2_table):
        new_key_56_bit = left_half + right_half

        key_dictionary = {i + 1: char for i, char in enumerate(new_key_56_bit)}
        print("The bits and their positions:", key_dictionary)
        key_48_bit = ""

        for position in pc_2_table:
            key_48_bit += key_dictionary[position]

        print("\n48-bit key after Permutation Choice 2:", key_48_bit)
        print("48-bit key in table form:")
        for i in range(0, len(key_48_bit), 6):
            row = key_48_bit[i:i+6]
            print('  '.join(f"{bit:2}" for bit in row))






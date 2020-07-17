import unittest
from sys import argv

def hex_to_rgb(hex_str: str) -> tuple:
    dct = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "a": 10,
            "b": 11,
            "c": 12,
            "d": 13,
            "e": 14,
            "f": 15
            }
    if hex_str.startswith("#"):
        hex_str = hex_str[1:]
    if len(hex_str) == 3:
        hex_str = "".join([ch + ch for ch in hex_str])
    if len(hex_str) == 6:
        seperated_vals = hex_str[:2], hex_str[2:4], hex_str[4:]
        try:
            return tuple([16 * dct[val[0]] + dct[val[1]]for val in seperated_vals])
        except: pass
    return (0, 0, 0)

class hex_to_rgb_test(unittest.TestCase):
    def test1(self):
        self.assertEqual(hex_to_rgb("#ffffff"), (255, 255, 255))

    def test2(self):
        self.assertEqual(hex_to_rgb("#000000"), (0, 0, 0))

    def test3(self):
        self.assertEqual(hex_to_rgb("#aaaaaa"), (170, 170, 170))

    def test4(self):
        self.assertEqual(hex_to_rgb("#123456"), (18, 52, 86))

    def test5(self):
        self.assertEqual(hex_to_rgb("#0c2238"), (12, 34, 56))

    def test6(self):
        self.assertEqual(hex_to_rgb("123456"), (18, 52, 86))

    def test7(self):
        self.assertEqual(hex_to_rgb("#fff"), (255, 255, 255))

    def test8(self):
        self.assertEqual(hex_to_rgb("#aaa"), (170, 170, 170))

    def test9(self):
        self.assertEqual(hex_to_rgb("1"), (0, 0, 0))

    def test10(self):
        self.assertEqual(hex_to_rgb("8888888"), (0, 0, 0))

    def test11(self):
        self.assertEqual(hex_to_rgb("gggggg"), (0, 0, 0))

def main():
    if len(argv) == 1:
        unittest.main()
    elif len(argv) == 2:
        if argv[1].startswith("#"):
            argv[1] = argv[1][1:]
        print(f"#{argv[1]} = rgb{hex_to_rgb(argv[1])}")
    else:
        print("Incorrect Usage")

if __name__ == "__main__":
    main()

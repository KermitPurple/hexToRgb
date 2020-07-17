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
    if len(hex_str) != 6:
        return (0, 0, 0)
    seperated_vals = hex_str[:2], hex_str[2:4], hex_str[4:]
    return [16 * dct[val[0]] + dct[val[1]]for val in seperated_vals]

def main():
    print(hex_to_rgb("#ffff32"))

if __name__ == "__main__":
    main()

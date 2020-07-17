def hex_to_rgb(hex_str: str) -> tuple:
    if hex_str.startswith("#"):
        hex_str = hex_str[1:]
    return hex_str

def main():
    print(hex_to_rgb("#000000"))

if __name__ == "__main__":
    main()

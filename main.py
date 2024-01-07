import os
import sys


# Function to read banner file
def read_banner(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content


def parse_banner(file_content):
    lower_bound = 32
    upper_bound = 126

    # Split the content into arts of each character
    char_arts = file_content.split("\n\n")
    ascii_dict = {}

    for i, art in enumerate(char_arts):
        if i + lower_bound > upper_bound:
            break  # Stop if ascii value > 126
        char_key = chr(i + lower_bound)
        ascii_dict[char_key] = art

    return ascii_dict


def generate_ascii_art(string_to_convert, ascii_dict):
    lines = string_to_convert.split("\\n")
    ascii_art_lines = []

# 'hello\nthere' lines = ['hello', 'there']
    for line in lines:
        ascii_art_for_line = [
            '' for _ in range(8)
        ]  # since height is 8
        for char in line:
            if char in ascii_dict:
                char_art = ascii_dict[char].split("\n")
                for i in range(8):
                    ascii_art_for_line[i] += (
                        char_art[i] + " "
                    )  # space betwen chars for clarity
        ascii_art_lines.append("\n".join(ascii_art_for_line))

    return "\n".join(ascii_art_lines)  # complete ascii art


if __name__ == '__main__':
    user_input = sys.argv
    # print(user_input)
    BANNER_TYPE = ('shadow', 'standard', 'thinkertoy')
    string_to_parse = user_input[1]
    if len(user_input) == 3:
        if user_input[2] in BANNER_TYPE:
            banner_type = user_input[2]
    else:
        banner_type = 'standard'

    banner_path = os.path.join("./", f"{banner_type}.txt")  # path to banner
    banner_content = read_banner(banner_path)  # read banner file
    ascii_dict = parse_banner(banner_content)  # parse banner&create ascii dict
    # user_input = input()
    ascii_art = generate_ascii_art(string_to_parse, ascii_dict)
    print(ascii_art)

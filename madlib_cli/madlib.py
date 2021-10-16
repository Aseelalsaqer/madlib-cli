
import re


def welcome_msg():
    """
Welcoming message
"""
    print("Welcome to Madlib Game")


welcome_msg()


def read_template(path):
    """
    read_template function Read a file and return the content
    """

    try:
        with open(path) as f:
            file_content = f.read().strip()
            print('\n', file_content, '\n')
            return file_content
    except:
        raise Exception(f"({path}) not found")


if __name__ == "__main__":

    file_to_read = read_template("assets/dark_and_stormy_night_template.txt")

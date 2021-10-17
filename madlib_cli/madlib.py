
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
        raise FileNotFoundError(f"({path}) not found")


def parse_template(word):
    """
    parse function that Remove words inside of brackets and replace it.
    """
    word_types = list(re.findall(r'{(.*?)}', word))

    text = re.sub('{.*?}', '{}', word)

    return text, word_types


def merge(text, word):
    """
    merge function that returns a string with the language parts inserted into the template.
    """
    merged_text = text.format(*word)
    with open('assets/result.txt', 'w') as result:
        result.write(merged_text)
        print(merged_text)
    return merged_text


if __name__ == "__main__":

    file_to_read = read_template("assets/dark_and_stormy_night_template.txt")
    text, words = parse_template(file_to_read)
    word_result = []
    for i in words:
        user_input = input(f"Enter {i} >> ")
        word_result.append(user_input)
        madlib_result = merge(text, word_result)

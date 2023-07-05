#!/usr/bin/python3


def text_indentation(text):
    """
    Prints text with 2 new lines after each ".", "?", and ":"

    Args:
        text (str): The input text.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = (".", "?", ":")
    for char in punctuation_marks:
        text = text.replace(char, char + "\n\n")
    lines = [line.strip() for line in text.split("\n")]
    revised_text = "\n".join(lines)
    print(revised_text, end="")

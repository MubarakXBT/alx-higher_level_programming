#!/usr/bin/python3
""" Contain a a function that prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """ text_indentation - indent text where there is '.' , '?' or ':'
    Args:
        text: the string to be formatted
    Returns:
        Prints the formatted string
    """


    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 0
    while c < (len(text)):
        if text[c] not in '?:.':
            print(text[c], end='')
            c += 1
        else:
            print(text[c])
            print()
            c += 2
        if ((c)) == (len(text)):
            break
"""
Program to capitalize every first letter of the work after each space
"""


def cap_words(text: str) -> str:
    # return text.title()
    return " ".join(word.capitalize() for word in text.split())

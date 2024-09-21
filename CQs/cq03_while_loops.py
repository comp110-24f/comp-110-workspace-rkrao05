"""My third challenge question in COMP110."""

___author___ = "730768981"


def num_instances(phrase: str, search_char: str) -> None:
    """Finds every instance of a character in a given phrase."""
    count: int = 0  # local variable that keeps count of character instance
    index: int = 0  # local variable to keep track of index
    while index < len(phrase):  # makes sure string index isn't out of range
        if (
            phrase[index] == search_char
        ):  # conditional that checks if search_char = phrase
            count += 1
        index += 1
    print(count)


num_instances(phrase="HelloHelloHEllo", search_char="E")

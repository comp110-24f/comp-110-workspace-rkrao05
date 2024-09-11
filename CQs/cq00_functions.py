"""My second exercise in COMP110."""

__author__ = "730768981"


def mimic(message: str) -> str:
    """Repeats a message back to you."""
    return message


def main() -> None:
    """Prints the result of mimic function."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()

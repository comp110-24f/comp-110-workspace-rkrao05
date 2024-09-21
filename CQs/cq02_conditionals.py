"""My second challenge question in COMP 110."""

__author__ = "730768981"


def guess_a_number() -> None:
    """Takes user input to guess the secret number."""
    secret: int = 7  # sets secret number equal to 7
    guess: int = int(input("Guess a number: "))  # takes user input to guess number
    print("Your guess was " + str(guess))  # prints result of user's guess
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    elif guess > secret:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()

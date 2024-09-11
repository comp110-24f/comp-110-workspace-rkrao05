"""A program that calculates the costs of throwing a tea party using multiple functions."""

__author__: str = "730768981"


def main_planner(guests: int) -> None:
    """the entrypoint of the program."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# turned int to str to concatenate
# for cost call -> used tea_bags and treats as arguments for cost


def tea_bags(people: int) -> int:
    """# of tea bags based on people attending."""
    return people * 2


# two tea bags per person -> multiply people by 2


def treats(people: int) -> int:
    """# of treats based on people attending."""
    return int((tea_bags(people=people)) * 1.5)


# call tea bags first; 1.5 treats per tea bags
# make sure function returns int
# people = local variable
# return value of tea bags is x 1.5 to get # of treats


def cost(tea_count: int, treat_count: int) -> float:
    """returns the total cost of the tea party."""
    return (tea_count * 0.50) + (treat_count * 0.75)


# added both for total cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))

# conditional statement that asks for user input as a number (int)

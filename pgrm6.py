# Python's Switch is called match.
# We can combine if-else in case also.
# Plus, no need to write break every time.
# Default is denoted with an underscore symbol.
import json

var = input("Enter a number/list: ")
try:
    var = json.loads(var)
except (ValueError,TypeError):
    pass

match var:
    case 0:
        print("It is zero")
    case 10:
        print("It is 10")
    case 20 | 30 | 40:
        print(f"It is either 20, 30, or 40")
    case [a, b]:
        print(f"Two-valued list: {a}, {b}")
    case [a, b, c]:
        print(f"Three-valued list: {a}, {b}, {c}")
    #case list() as lst:  # Handle lists of any length
    #    print(f"List detected with values: {lst}")
    case _ if isinstance(var, int) and var % 2 == 0:
        print("Unknown, but surely an even number")
    case _ if isinstance(var, int) and var % 2 != 0:
        print("Unknown, but surely an odd number")
    case _ if isinstance(var, (int, list)):     # Check if var is one of the types described in the type parameter
        print("Unknown number/list with values", var)
    case _:
        print("Neither number nor list")
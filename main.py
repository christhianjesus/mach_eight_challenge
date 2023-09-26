import argparse

from mach_eight_challenge.find_pairs import find_pairs

if __name__ == "__main__":
    """
    usage: main.py [-h] a,b,c,... sum

    Finds pairs of integers.

    positional arguments:
    a,b,c,...   comma-separated integers
    sum         target sum

    options:
    -h, --help  show this help message and exit
    """
    parser = argparse.ArgumentParser(description="Finds pairs of integers.")
    parser.add_argument(
        "numbers",
        metavar="a,b,c,...",
        help="comma-separated integers",
        type=lambda l: [int(i) for i in l.split(",")],
    )
    parser.add_argument("target", metavar="sum", help="target sum", type=int)

    args = parser.parse_args()
    result = find_pairs(args.numbers, args.target)

    for num1, num2 in result:
        print(f"+ {num1},{num2}")

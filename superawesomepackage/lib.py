from termcolor import colored
import argparse


def try_me(n=42):
    return "spam " * n


if __name__ == "__main__":
    description = "stkrgcp_description"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "--nspams", nargs=1, help="number of spams to print", required=False
    )
    args = parser.parse_args()

    if args.nspams != None:
        n = int(args.nspams[0])  # Arg nspams is a list of one item (a string)
        spam = try_me(n)
        print(colored(f"###### Here are {n} spams just for you ######", "blue"))
        print(colored(spam, "red"))
    else:
        spam = try_me()
        print(colored(f"###### Here are {42} spams just for you ######", "blue"))
        print(colored(spam, "red"))

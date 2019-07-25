import argparse


def parse_shakespeare():
    return "Most lazar-like, with vile and loathsome crust."


def store_shakespeare(text, output_filepath):
    with open(output_filepath, "w") as fh:
        fh.write(text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse Shakespeare.")
    parser.add_argument(
        "--output", type=str, help="Write the parsed Shakespeares to this filepath."
    )
    args = parser.parse_args()
    print("Parsing the Bard...")
    text = parse_shakespeare()
    print("Writing results to {}".format(args.output))
    store_shakespeare(text, args.output)

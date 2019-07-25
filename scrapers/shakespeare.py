import argparse


def parse_law_titles():
    return "Most lazar-like, with vile and loathsome crust."


def store_laws(laws, output_filepath):
    with open(output_filepath, "w") as fh:
        fh.write(laws)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Parse Shakespeare."
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Write the parsed Shakespeares to this filepath.",
    )
    args = parser.parse_args()
    print("Parsing the Bard...")
    laws = parse_law_titles()
    print("Writing results to {}".format(args.output))
    store_laws(laws, args.output)

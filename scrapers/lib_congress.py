import argparse


def parse_law_titles():
    return "laws laws laws."


def store_laws(laws, output_filepath):
    with open(output_filepath, "w") as fh:
        fh.write(laws)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Parse congressional legislation titles."
    )
    parser.add_argument(
        "--output",
        type=str,
        help="A path to which to write new line separated legislation titles.",
    )
    args = parser.parse_args()
    print("Parsing law titles...")
    laws = parse_law_titles()
    print("Writing results to {}".format(args.output))
    store_laws(laws, args.output)

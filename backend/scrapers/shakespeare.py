import os
import argparse

from bs4 import BeautifulSoup
import requests


def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, features="html.parser")


def parse_lines(a_tags):
    lines = []
    for a_tag in a_tags:
        if not a_tag.attrs.get("name"):
            continue
        if a_tag.attrs.get("name").startswith("speech"):
            continue
        else:
            lines.append(a_tag.contents[0])
    return "\n".join(lines)


def parse_work(work):
    soup = get_soup(work["url"])
    a_tags = soup.find_all("a")
    # naive version - not extracting speaker name
    return parse_lines(a_tags)


def parse_complete_works():
    url = "http://shakespeare.mit.edu"
    soup = get_soup(url)
    # Let's assume that this website wont change much, as it looks pretty old and claims
    # to have "offered Shakespeare's plays and poetry to the Internet community since 1993."
    # Also, its earliest entry in the wayback machine looks identical to its current state:
    # https://web.archive.org/web/20070221034237/http://shakespeare.mit.edu/index.html
    #
    # This assumption allows us to make some strong assertions about the order that the works come in.
    # We'll make a lookup of the order of the tables and their content.
    categories = ["comedy", "history", "tragedy", "poetry"]
    tables = soup.find_all("td")
    category_idx = 0
    works = []
    for table in tables:
        # valign == BASELINE indicates that this table contains links to Shakespeare's works
        if not table.attrs.get("valign") == "BASELINE":
            continue
        # each a tag in these sections link to a table of contents for a given work
        a_tags = table.find_all("a")
        for a_tag in a_tags:
            works.append(
                dict(
                    # strip the line breaks in the content
                    name=a_tag.contents[0].replace("\n", ""),
                    category=categories[category_idx],
                    # there's a full version of each work nested at the same level as these table of content pages
                    # called "full.html" - we'll swap this path in here
                    url=os.path.join(url, a_tag.attrs["href"]).replace("index.html", "full.html"),
                )
            )
        # increment the category index after collecting all works in this table
        category_idx += 1
    return works


def parse_shakespeare():
    works = parse_complete_works()
    complete_works = []
    for work in works:
        print("Parsing {name}".format(**work))
        complete_works.append(parse_work(work))
    return "\n".join(complete_works)


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

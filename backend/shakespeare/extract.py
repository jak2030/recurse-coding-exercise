import os
import argparse

from bs4 import BeautifulSoup
import requests


def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, features="html.parser")


def parse_lines(a_tags):
    lines = []
    character = ""
    for a_tag in a_tags:
        if not a_tag.attrs.get("name"):
            continue
        if a_tag.attrs.get("name").startswith("speech"):
            character = a_tag.text
        else:
            lines.append(dict(character=character, text=a_tag.text))
    return lines


def parse_work(url):
    soup = get_soup(url)
    a_tags = soup.find_all("a")
    # naive version - not extracting speaker name
    return parse_lines(a_tags)


def parse_shakespeare():
    root_url = "http://shakespeare.mit.edu"
    soup = get_soup(root_url)
    # Assuming that this website wont change much, as it looks pretty old and claims
    # to have "offered Shakespeare's plays and poetry to the Internet community since 1993."
    # Also, its earliest entry in the wayback machine looks identical to its current state:
    # https://web.archive.org/web/20070221034237/http://shakespeare.mit.edu/index.html
    #
    categories = ["comedy", "history", "tragedy", "poetry"]
    tables = soup.find_all("td")
    category_idx = 0
    for table in tables:
        # valign == BASELINE indicates that this table contains links to Shakespeare's works
        if not table.attrs.get("valign") == "BASELINE":
            continue
        # each a tag in these sections link to a table of contents for a given work
        a_tags = table.find_all("a")
        for a_tag in a_tags:
            # there's a full version of each work nested at the same level as these table of content pages
            # called "full.html" - we'll swap this path in here
            url = os.path.join(root_url, a_tag.attrs["href"]).replace(
                "index.html", "full.html"
            )
            lines = parse_work(url)
            # TODO this is essentially the transform step here...
            work_name = a_tag.contents[0].replace("\n", "").replace(" ", "-").replace("'", "").replace(",", "").lower()
            print("Parsing {} {}".format(categories[category_idx], work_name))
            for line in lines:
                yield dict(
                    # strip the line breaks in the content
                    play=work_name,
                    category=categories[category_idx],
                    url=url,
                    text=line["text"],
                    character=line.get("character", "").replace(" ", "-").lower(),
                )
        # increment the category index after collecting all works in this table
        category_idx += 1

# Matt Weeden
# 6/25/2020

# A small script to generate the html based on a poem text file

import argparse
from bs4 import BeautifulSoup as bs

def main():

    parser = argparse.ArgumentParser(description="A small script to generate the html based on a poem text file")
    parser.add_argument("-v", "--verbose", help="be verbose about it", action="store_true")
    parser.add_argument("in_file", help="input poetry file")
    args = parser.parse_args()

    html_template_filename = 'poem_template.html'

    
    if args.verbose:
        print(f"generating html for {args.in_file}...")

    html_template = ''
    with open(html_template_filename, 'r') as f:
        html_template = [x.strip() for x in f.readlines()]

    if args.verbose:
        print(f"  html template: {html_template}")

    if args.verbose:
        print(f"getting poem title from {args.in_file}")

    poem_text = ''
    title = ''
    body = ''

    with open(args.in_file, 'r') as f:
        poem_text = [x.strip() for x in f.readlines()]

    if args.verbose:
        print(f"  poem_test: {poem_text}")

    title = poem_text[0]

    if args.verbose:
        print(f"  title: {title}")

    for l in poem_text[2:]:
        if l == "":
            body += '<br>\n'
        else:
            body += l + '<br>\n'

    body_tabbed = ['    '+x for x in body[:-1].split("\n")]

    if args.verbose:
        print(f"body: {body_tabbed}")

    final_html = ''

    for l in html_template:
        final_html += l.replace("{title}", title) \
                        .replace("{title_lower}", title.lower()) \
                        .replace("{body}", "\n".join(body_tabbed))
        final_html += "\n"

    soup = bs(final_html.strip(), features="html.parser")
    prettyHTML = soup.prettify()

    print(prettyHTML)



if __name__ == "__main__":
    main()

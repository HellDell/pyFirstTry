# a function that reads a given HTML file, cleans all the html tags,
# and writes this text to another text file

import re
import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):

    # reading HTML file w/ auto-closing at the end
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned_content = re.sub(r'<[^>]+>', '', html)

    # clearing rows here by iterating on each of them
    cleaned_lines = [line.strip() for line in cleaned_content.splitlines() if line.strip()]

    # recording the cleared text
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write('\n'.join(cleaned_lines))

    # writing a note for a user
    print(f"Cleaned text can be found in a file called '{result_file}'")

delete_html_tags('draft.html')
import re


def parse(text: str):
    """ Convert markdown into html style."""
    text = re.sub(r'__([^\n]+?)__', r'<strong>\1</strong>', text)
    text = re.sub(r'_([^\n]+?)_', r'<em>\1</em>', text)
    text = re.sub(r'^\* (.*?$)', r'<li>\1</li>', text, flags=re.MULTILINE)
    text = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', text, flags=re.DOTALL)
    for i in range(6, 0, -1):
        text = re.sub(r'^{} (.*?$)'.format('#' * i), r'<h{0}>\1</h{0}>'.format(i), text, flags=re.MULTILINE)
    text = re.sub(r'^(?!<[hlu])(.*?$)', r'<p>\1</p>', text, flags=re.MULTILINE)
    text = re.sub(r'\n', '', text)
    return text

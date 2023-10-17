import re

def domain_name(url):
    match = re.search(r"(http)?(s)?(:\/\/)?(www\.)?([a-z0-9\-]*)\.{1}.*", url)
    match = match.group(5)
    return match
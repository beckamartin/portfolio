import re

def strip_comments(strng, markers):
    for marker in markers:
        marker = "\\" + marker
        strng = re.sub(rf"([ \t]*{marker}.*)", "", strng)
        
    return strng
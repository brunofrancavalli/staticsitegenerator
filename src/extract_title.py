import re
def extract_title(markdown: str):
    if(markdown.index("#") == 0):
        match = re.match("# *(.*)", markdown)
        return match[1]
    else:
        raise ValueError("markdown must start with #")

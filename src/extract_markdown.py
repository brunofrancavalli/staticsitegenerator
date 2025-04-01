import re

def extract_markdown(text, regex_string):
    result = []
    matches = re.findall(regex_string, text)
    for match in matches:
        result.append((match[0],match[1]))
    
    return result

def extract_markdown_images(text):
    return extract_markdown(text, r"!\[([a-zA-Z ]+)\]\(([a-zA-Z0-9\./:@]+)\)")

def extract_markdown_links(text):
    return extract_markdown(text, r"\[([a-zA-Z ]+)\]\(([a-zA-Z0-9\./:@]+)\)")
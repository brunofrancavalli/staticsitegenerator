import re

def extract_markdown_links(text):
    # "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    result = []
    # matches = re.findall(r"!\[([a-z ]+)\]\(([a-zA-Z0-9\./:])+\)")
    matches = re.findall(r"\[([a-z ]+)\]\(([a-zA-Z0-9\./:@]+)\)", text)
    for match in matches:
        result.append((match[0],match[1]))
    
    return result

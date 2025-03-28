from markdown_to_html_node import markdown_to_html_node 
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_source = open(from_path).read()
    template_source = open(template_path).read()

    html_source = markdown_to_html_node(markdown_source).to_html()
    title = extract_title(markdown_source)

    template_source.replace("{{ Title }}", title)
    template_source.replace("{{ Content }}", html_source)

    file = open(dest_path, 'w')
    file.write(template_source)
    file.close()
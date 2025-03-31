from markdown_to_html_node import markdown_to_html_node 
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    current_file_path = os.path.dirname(os.path.abspath(__file__))
    if( not from_path.startswith("/")):
        from_path = os.path.join(current_file_path, from_path)

    if( not dest_path.startswith("/")):
        dest_path = os.path.join(current_file_path, dest_path)

    if( not template_path.startswith("/")):
        template_path = os.path.join(current_file_path, template_path)


    markdown_source = open(from_path).read()
    template_source = open(template_path).read()

    html_node = markdown_to_html_node(markdown_source)
    html_source = html_node.to_html()
    title = extract_title(markdown_source)

    template_source.replace("{{ Title }}", title)
    template_source.replace("{{ Content }}", html_source)

    file = open(dest_path, 'w')
    file.write(template_source)
    file.close()
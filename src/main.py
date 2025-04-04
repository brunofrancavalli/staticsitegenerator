import os
from copy_files import copy_files
from generate_page import generate_page

def main():
    # get the path of this executing file
    python_file_path = os.path.abspath(__file__)

    # do it twice to get rid of the filename and then get rid of the directory, the we get to the parent
    parent_directory = os.path.dirname(os.path.dirname(python_file_path))
    source = os.path.join(parent_directory, "static")
    destination = os.path.join(parent_directory, "public")

    copy_files(source=source, destination=destination)

    generate_page(from_path="../content/index.md", template_path="../template.html", dest_path="../public/index.html")

main()

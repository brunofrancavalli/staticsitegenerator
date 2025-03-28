from node_text import NodeText
import os
import shutil

def copy_files(source, destination):
    if(os.path.exists(destination)):
        print(f"Deleting ${destination}..")
        shutil.rmtree(destination)
    print(f"Creating ${destination}..")
    os.mkdir(destination)
    
    file_list = os.listdir(source)
    for file_item in file_list:
        source_item = os.path.join(source, file_item)
        destination_item = os.path.join(destination, file_item)
        if(os.path.isfile(source_item)):
            print(f"Copying '${source_item}' to '${destination_item}'")
            shutil.copy(source_item, destination_item)
        else:
            # this is a directory need to call it again
            copy_files(source_item, destination_item)

def main():
    # get the path of this executing file
    python_file_path = os.path.abspath(__file__)
    # do it twice to get rid of the filename and then get rid of the directory, the we get to the parent
    parent_directory = os.path.dirname(os.path.dirname(python_file_path))
    source = os.path.join(parent_directory, "static")
    destination = os.path.join(parent_directory, "public")

    copy_files(source=source, destination=destination)

main()

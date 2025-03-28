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
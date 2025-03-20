import re

from extract_markdown import extract_markdown_images, extract_markdown_links
from node_text import NodeText, TextType

def split_nodes_image(old_node_list):
    return split_nodes_start_mid_end(old_node_list, extract_markdown_images, "![", "](", ")", TextType.IMAGE)

def split_nodes_link(old_node_list):
    return split_nodes_start_mid_end(old_node_list, extract_markdown_links, "[", "](", ")", TextType.LINK)

def split_nodes_delimiter(old_node_list, delimiter, text_type):
    new_nodes = []
    for old_node_item in old_node_list:
        # we only process those that have not been processed yet
        if old_node_item.text_type == TextType.TEXT:
            old_nodes_list = old_node_item.text.split(delimiter)
            processing_type = False
            for old_nodes_item in old_nodes_list:
                # only processs if we have something to process
                if len(old_nodes_item) > 0:
                    if processing_type:
                        new_nodes.append(NodeText(old_nodes_item, text_type))
                    else:
                        new_nodes.append(NodeText(old_nodes_item, TextType.TEXT))
                # always flip the flag since we are starting with false we flip and we should only be within the entries
                processing_type = not processing_type
        else:
            new_nodes.append(old_node_item)
    
    return new_nodes

def split_nodes_start_mid_end(old_node_list, extract_markdown, start_delimiter, mid_delimiter, end_delimiter, text_type):
    node_return = []
    for old_node in old_node_list:
        # only process those who have not been processed
        if old_node.text_type == TextType.TEXT:
            old_node_text = old_node.text
            node_image_list = extract_markdown(old_node_text)
            if len(node_image_list) > 0:
                for node_image in node_image_list:
                    find_value = f"{start_delimiter}{node_image[0]}{mid_delimiter}{node_image[1]}{end_delimiter}"
                    index_start = old_node_text.find(find_value)
                    index_end = index_start + len(find_value)

                    node_text_value = old_node_text[0:index_start]

                    # do we have text to add before adding our entry?
                    if len(node_text_value) > 0:
                        node_text = NodeText(node_text_value,TextType.TEXT )
                        node_return.append(node_text)

                    node_return.append(NodeText(node_image[0], text_type, node_image[1]))

                    # get ready for the next loop by moving the string forward
                    old_node_text = old_node_text[index_end:]
                if len(old_node_text) > 0:
                    node_return.append(NodeText(old_node_text,TextType.TEXT ))
            else:
                node_return.append(old_node)
        else:
            node_return.append(old_node)
    return node_return

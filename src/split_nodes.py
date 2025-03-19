import re

from extract_markdown_images import extract_markdown_images
from node_text import NodeText, TextType

def split_nodes_image(old_node_list, start_delimiter, mid_delimiter, end_delimiter):
    return split_nodes_start_mid_end(old_node_list, "![", "](", "]")

def split_nodes_link(old_node_list, start_delimiter, mid_delimiter, end_delimiter):
    return split_nodes_start_mid_end(old_node_list, "[", "](", "]")

def split_nodes_start_mid_end(old_node_list, start_delimiter, mid_delimiter, end_delimiter):
    node_return = []
    for old_node in old_node_list:
        old_node_text = old_node.text
        node_image_list = extract_markdown_images(old_node_text)
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

                node_return.append(NodeText(node_image[0], TextType.IMAGE, node_image[1]))

                # get ready for the next loop by moving the string forward
                old_node_text = old_node_text[index_end:]
            if len(old_node_text) > 0:
                node_return.append(NodeText(old_node_text,TextType.TEXT ))
        else:
            node_return.append(old_node)
    return node_return

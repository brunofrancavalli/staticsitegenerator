from node_text import NodeText, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_node_text(text):
    node_list = [NodeText(text, TextType.TEXT)]
    node_list = split_nodes_delimiter(node_list, TextType.CODE.value, TextType.CODE)
    node_list = split_nodes_image(node_list)
    node_list = split_nodes_link(node_list)
    node_list = split_nodes_delimiter(node_list, TextType.BOLD.value, TextType.BOLD)
    node_list = split_nodes_delimiter(node_list, TextType.ITALIC.value, TextType.ITALIC)

    return node_list
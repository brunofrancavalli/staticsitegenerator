from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from block import BlockType
from node_parent import NodeParent
from node_leaf import NodeLeaf
from node_text_to_node_html import node_text_to_node_html
from text_to_node_text import text_to_node_text


def markdown_to_html_node(markdown):
    node_leaf_list = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.CODE:
            node_text = text_to_node_text(block)
        elif block_type == BlockType.HEADING:
            node_text = text_to_node_text(block)
        elif block_type == BlockType.ORDERED_LIST:
            node_text = text_to_node_text(block)
        elif block_type == BlockType.PARAGRAPH:
            node_text = text_to_node_text(block)
        elif block_type == BlockType.QUOTE:
            node_text = text_to_node_text(block)
        elif block_type == BlockType.UNORDERED_LIST:
            node_text = text_to_node_text(block)
        node_leaf_list.append(node_text_to_node_html(node_text))

    return NodeParent("div", node_leaf_list)
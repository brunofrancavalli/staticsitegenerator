from node_text import NodeText, TextType

def split_nodes_delimiter(old_node_list, delimiter, text_type):
    for old_node_item in old_node_list:
        old_nodes_list = old_node_item.text.split(delimiter)
        processing_type = False
        new_nodes = []
        for old_nodes_item in old_nodes_list:
            # only processs if we have something to process
            if len(old_nodes_item) > 0:
                if processing_type:
                    new_nodes.append(NodeText(old_nodes_item, text_type))
                else:
                    new_nodes.append(NodeText(old_nodes_item, TextType.TEXT))
            # always flip the flag since we are starting with false we flip and we should only be within the entries
            processing_type = not processing_type
    
    return new_nodes


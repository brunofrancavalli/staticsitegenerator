def markdown_to_blocks(markdown):
    markdown_block = markdown.split('\n\n')
    markdown_block = [block.strip('\n') for block in markdown_block]
    return markdown_block
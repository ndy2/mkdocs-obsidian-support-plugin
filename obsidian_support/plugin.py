from mkdocs.plugins import BasePlugin

from obsidian_support.conversion.admonition import AdmonitionConvert
from obsidian_support.conversion.image_link import ImageLinkConvert
from obsidian_support.markdown_code_extract import get_code_indices
from obsidian_support.markdown_convert import markdown_convert

"""
A mkdocs plugin that support conversion from 
'obsidian syntax' to 'mkdocs-material syntax'
"""


class ObsidianSupportPlugin(BasePlugin):

    def on_page_markdown(self, markdown, page, config, files):
        # content code & code block should not be converted
        code_indices = get_code_indices(markdown)

        ## apply conversions
        markdown = markdown_convert(markdown, AdmonitionConvert(), code_indices)
        markdown = markdown_convert(markdown, ImageLinkConvert(), code_indices)

        return markdown

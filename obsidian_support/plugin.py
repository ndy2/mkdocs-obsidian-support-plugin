from mkdocs.plugins import BasePlugin

from obsidian_support.conversion.admonition import AdmonitionConversion
from obsidian_support.conversion.admonition_backquotes import AdmonitionBackquotesConversion
from obsidian_support.conversion.image_internal_link import ImageInternalLinkConversion
from obsidian_support.conversion.image_web_link import ImageWebLinkConversion
from obsidian_support.conversion.tags import TagsConversion
from obsidian_support.markdown_convert import markdown_convert

"""
A mkdocs plugin that support conversion from
'obsidian syntax' to 'mkdocs-material syntax'
"""


class ObsidianSupportPlugin(BasePlugin):

    def on_page_markdown(self, markdown, page, config, files):
        ## apply conversions
        markdown = markdown_convert(markdown, page, AdmonitionConversion())
        markdown = markdown_convert(markdown, page, AdmonitionBackquotesConversion())
        # markdown = markdown_convert(markdown, page, ExcalidrawConversion())
        markdown = markdown_convert(markdown, page, ImageWebLinkConversion())
        markdown = markdown_convert(markdown, page, ImageInternalLinkConversion())
        markdown = markdown_convert(markdown, page, TagsConversion())

        return markdown

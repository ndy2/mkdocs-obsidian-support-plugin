from mkdocs.plugins import BasePlugin
from overrides import overrides

from obsidian_support.conversion.admonition.admonition_backquotes import AdmonitionBackquotesConversion
from obsidian_support.conversion.admonition.admonition_callout import AdmonitionCalloutConversion
from obsidian_support.conversion.image_link.image_internal_link import ImageInternalLinkConversion
from obsidian_support.conversion.image_link.image_web_link import ImageWebLinkConversion
from obsidian_support.conversion.tags.tags import TagsConversion
from obsidian_support.markdown_convert import markdown_convert

"""
A mkdocs plugin that support conversion from
'obsidian syntax' to 'mkdocs-material syntax'
"""


class ObsidianSupportPlugin(BasePlugin):

    def __init__(self):
        super().__init__()
        self.admonition_conversions = AdmonitionCalloutConversion(), AdmonitionBackquotesConversion()
        self.web_link_conversions = ImageWebLinkConversion(), ImageInternalLinkConversion()
        self.tags_conversion = TagsConversion()

    @overrides
    def on_page_markdown(self, markdown, page, config, files):
        # apply conversions
        markdown = markdown_convert(markdown, page, *self.admonition_conversions)
        markdown = markdown_convert(markdown, page, *self.web_link_conversions)
        markdown = markdown_convert(markdown, page, self.tags_conversion)
        return markdown

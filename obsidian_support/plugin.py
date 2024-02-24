from mkdocs.plugins import BasePlugin

from obsidian_support.conversion.admonition.admonition_backquotes import AdmonitionBackquotesConversion
from obsidian_support.conversion.admonition.admonition_callout import AdmonitionCalloutConversion
from obsidian_support.conversion.comment.comment import CommentConversion
from obsidian_support.conversion.image_link.image_internal_link import ImageInternalLinkConversion
from obsidian_support.conversion.image_link.image_web_link import ImageWebLinkConversion
from obsidian_support.conversion.pdf.pdf import PdfConversion
from obsidian_support.conversion.tags.tags import TagsConversion
from obsidian_support.markdown_convert import markdown_convert

"""
A mkdocs plugin that support conversion from
'obsidian syntax' to 'mkdocs-material syntax'
"""


class ObsidianSupportPlugin(BasePlugin):

    def __init__(self):
        super().__init__()
        self.admonition_callout_conversions = AdmonitionCalloutConversion()
        self.admonition_backquotes_conversion = AdmonitionBackquotesConversion()
        self.comment_conversion = CommentConversion()
        self.pdf_conversion = PdfConversion()
        self.image_web_link_conversions = ImageWebLinkConversion()
        self.image_internal_link_conversion = ImageInternalLinkConversion()
        self.tags_conversion = TagsConversion()

    def on_page_markdown(self, markdown, page, config, files):
        # apply conversions
        markdown = markdown_convert(markdown, page, self.admonition_callout_conversions)
        markdown = markdown_convert(markdown, page, self.admonition_backquotes_conversion)
        markdown = markdown_convert(markdown, page, self.comment_conversion)
        markdown = markdown_convert(markdown, page, self.pdf_conversion)
        markdown = markdown_convert(markdown, page, self.image_web_link_conversions)
        markdown = markdown_convert(markdown, page, self.image_internal_link_conversion)
        markdown = markdown_convert(markdown, page, self.tags_conversion)
        return markdown

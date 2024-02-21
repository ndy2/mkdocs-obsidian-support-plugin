import re

from mkdocs.structure.pages import Page
from overrides import override

from obsidian_support.conversion.abstract_conversion import AbstractConversion, SyntaxGroup

"""
a strategy that convert [markdown image web link](https://www.w3schools.io/file/markdown-images/)
to [obsidian embedding files#image](https://help.obsidian.md/Linking+notes+and+files/Embedding+files#Embed+an+image+in+a+note) in wikilink
"""


class ImageWebLinkConversion(AbstractConversion):

    @property
    @override
    def obsidian_regex_pattern(self):
        # OBSIDIAN_IMAGE_WEB_LINK_REGEX
        return re.compile(r"!\[(?P<tags>.*)]\((?P<image_path>https?://.*)\)")

    @override
    def convert(self, syntax_groups: SyntaxGroup, page: Page) -> str:
        return self._convert_image_link(*syntax_groups)

    def _convert_image_link(self, tags: str, image_path: str) -> str:
        return f"![[{image_path}|{tags}]]"

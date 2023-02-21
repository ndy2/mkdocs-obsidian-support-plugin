from obsidian_support.abstract_conversion import AbstractConversion, SyntaxGroup

"""
a strategy that convert [obsidian embedding files#image](https://help.obsidian.md/Linking+notes+and+files/Embedding+files#Embed+an+image+in+a+note) in wikilink
to [mkdocs-material images](https://squidfunk.github.io/mkdocs-material/reference/images/) in markdown link
"""

OBSIDIAN_WIKILINK_IMAGE_REGEX = "!\\[\\[(?P<image_path>.+)\\]\\]"
OBSIDIAN_WIKILINK_IMAGE_REGEX_GROUPS = ['image_path']


class ImageLinkConvert(AbstractConversion):
    def __init__(self):
        super().__init__(OBSIDIAN_WIKILINK_IMAGE_REGEX, OBSIDIAN_WIKILINK_IMAGE_REGEX_GROUPS)

    def convert(self, syntax_groups: SyntaxGroup) -> str:
        return create_markdown_image_link(*syntax_groups)


def create_markdown_image_link(image_path: str) -> str:
    markdown_image_link = '![' + image_path + '](' + image_path + ')'
    return markdown_image_link

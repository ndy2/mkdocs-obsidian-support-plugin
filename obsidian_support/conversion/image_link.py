import re

from inspect import cleandoc

from obsidian_support.abstract_conversion import AbstractConversion, SyntaxGroup
from mkdocs.structure.pages import Page

"""
a strategy that convert [obsidian embedding files#image](https://help.obsidian.md/Linking+notes+and+files/Embedding+files#Embed+an+image+in+a+note) in wikilink
to [mkdocs-material images](https://squidfunk.github.io/mkdocs-material/reference/images/) in markdown link
"""

OBSIDIAN_WIKILINK_IMAGE_REGEX = "!\\[\\[(?P<image_path>[^\\|^\\]]+)(?P<tags>|.+)?\\]\\]"
OBSIDIAN_WIKILINK_IMAGE_REGEX_GROUPS = ['image_path', 'tags']


class ImageLinkConvert(AbstractConversion):
    def __init__(self):
        super().__init__(OBSIDIAN_WIKILINK_IMAGE_REGEX, OBSIDIAN_WIKILINK_IMAGE_REGEX_GROUPS)

    def convert(self, syntax_groups: SyntaxGroup, page: Page) -> str:
        return convert_image_link(*syntax_groups)


def convert_image_link(image_path: str, tags: str) -> str:
    markdown_image_link = '![' + image_path + '](' + image_path + ')'
    if tags is "":
        return markdown_image_link
    tags_split = tags[1:].split('|')
    caption_or_size = tags_split[0]
    size = tags_split[1] if 1 < len(tags_split) else None

    ## ![[image.png|caption|200x300]]
    if size is not None:
        size_tag = __get_size_tag(size)
        caption_tag = __get_caption_tag(caption_or_size, False)
    else:
        ## ![[image.png|caption]] or ![[image.png|200x300]]
        size_tag = __get_size_tag(caption_or_size)
        caption_tag = __get_caption_tag(caption_or_size, size_tag != "")

    return cleandoc(f"""
            <figure markdown>
              {markdown_image_link}{size_tag}
              {caption_tag}
            </figure markdown>
        """)


def __get_size_tag(tag: str) -> str:
    if tag.isnumeric():
        return f"{{ width=\"{tag}\" }}"
    else:
        split = tag.split('x')
        if len(split) == 2 and split[0].isnumeric() and split[1].isnumeric():
            return f"{{ width=\"{split[0]}\" height=\"{split[1]}\" }}"
        else:
            return ""


def __get_caption_tag(tag: str, empty_flag: bool) -> str:
    if tag == "" or empty_flag:
        return ""
    return f"<figcaption>{tag}</figcaption>"

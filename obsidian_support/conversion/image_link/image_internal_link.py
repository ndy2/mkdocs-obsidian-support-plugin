import re
from inspect import cleandoc

from mkdocs.structure.pages import Page
from overrides import override

from obsidian_support.conversion.abstract_conversion import AbstractConversion, SyntaxGroup

"""
A strategy that convert [obsidian embedding files#image](https://help.obsidian.md/Linking+notes+and+files/Embedding+files#Embed+an+image+in+a+note) in wikilink
to [mkdocs-material images](https://squidfunk.github.io/mkdocs-material/reference/images/) in markdown link

Examples:
given : `![[hello.png]]` 
converted : `![hello.png](hello.png)`
"""


class ImageInternalLinkConversion(AbstractConversion):

    @property
    @override
    def obsidian_regex_pattern(self):
        # OBSIDIAN_IMAGE_INTERNAL_LINK_REGEX
        return re.compile(r"!\[\[(?P<image_path>[^|^\]]+)(?P<tags>|.+)?]]")

    @override
    def convert(self, syntax_groups: SyntaxGroup, page: Page, depth: int) -> str:
        return self._convert_image_internal_link(*syntax_groups)

    def _convert_image_internal_link(self, image_path: str, tags: str) -> str:
        markdown_image_link = '![' + image_path + '](' + image_path + ')'
        if tags == "":
            return markdown_image_link
        tags_split = tags[1:].split('|')
        caption_or_size = tags_split[0]
        size = tags_split[1] if 1 < len(tags_split) else None

        ## ![[image.png|caption|200x300]]
        if size is not None:
            size_tag = self.__get_size_tag(size)
            caption_tag = self.__get_caption_tag(caption_or_size, False)
        else:
            ## ![[image.png|caption]] or ![[image.png|200x300]]
            size_tag = self.__get_size_tag(caption_or_size)
            caption_tag = self.__get_caption_tag(caption_or_size, size_tag != "")

        return cleandoc(f"""
                <figure markdown="span">
                  {markdown_image_link}{size_tag}
                  {caption_tag}
                </figure markdown>
            """)

    def __get_size_tag(self, tag: str) -> str:
        if tag.isnumeric():
            return f"{{ width=\"{tag}\" }}"
        else:
            split = tag.split('x')
            if len(split) == 2 and split[0].isnumeric() and split[1].isnumeric():
                return f"{{ width=\"{split[0]}\" height=\"{split[1]}\" }}"
            else:
                return ""

    def __get_caption_tag(self, tag: str, empty_flag: bool) -> str:
        if tag == "" or empty_flag:
            return ""
        return f"<figcaption>{tag}</figcaption>"

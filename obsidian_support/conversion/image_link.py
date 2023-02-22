import re

from inspect import cleandoc
from obsidian_support.abstract_conversion import AbstractConversion, SyntaxGroup

"""
a strategy that convert [obsidian embedding files#image](https://help.obsidian.md/Linking+notes+and+files/Embedding+files#Embed+an+image+in+a+note) in wikilink
to [mkdocs-material images](https://squidfunk.github.io/mkdocs-material/reference/images/) in markdown link
"""

OBSIDIAN_WIKILINK_IMAGE_REGEX = "!\\[\\[(?P<image_path>[^\\|^\\]]+)(?P<tags>|.+)?\\]\\]"
OBSIDIAN_WIKILINK_IMAGE_REGEX_GROUPS = ['image_path', 'tags']

OBSIDIAN_WIKILINK_IMAGE_TAGS_REGEX = "^(?P<caption_or_size>\\|[^\\|]+)(?P<size>\\|[^\\|]+)?$"
OBSIDIAN_WIKILINK_IMAGE_TAGS_REGEX_GROUPS = ['caption_or_size', 'size']


class ImageLinkConvert(AbstractConversion):
    def __init__(self):
        super().__init__(OBSIDIAN_WIKILINK_IMAGE_REGEX, OBSIDIAN_WIKILINK_IMAGE_REGEX_GROUPS)
        self.obsidian_wikilink_image_tags_pattern = re.compile(OBSIDIAN_WIKILINK_IMAGE_TAGS_REGEX)
        self.obsidian_wikilink_image_tags_group = OBSIDIAN_WIKILINK_IMAGE_TAGS_REGEX_GROUPS

    def convert(self, syntax_groups: SyntaxGroup) -> str:
        return self.convert_image_link(*syntax_groups)

    def convert_image_link(self, image_path: str, tags: str) -> str:
        markdown_image_link = '![' + image_path + '](' + image_path + ')'

        if tags == "":
            replaced_image_link = markdown_image_link
        else:
            tags_pattern_match = self.obsidian_wikilink_image_tags_pattern.match(tags)
            print(tags)
            caption_or_size = tags_pattern_match.group("caption_or_size")[1:]
            size = tags_pattern_match.group("size")
            captionTag = ""
            sizeTags = ""

            ## given image form : ![[image.png|caption|200]]
            if size is not None:
                size = size[1:]
                caption = caption_or_size
                captionTag = f"<figcaption>{caption}</figcaption>"
            else:
                split = caption_or_size.split('x')
                ## given image form : ![[image.png|200x300]]
                if len(split) == 2 and split[0].isnumeric() and split[1].isnumeric():
                    sizeTags += f"width=\"{split[0]}\" "
                    sizeTags += f"height=\"{split[1]}\""

                ## given image form : ![[image.png|200]]
                elif caption_or_size.isnumeric():
                    sizeTags += f"width=\"{split[0]}\""

                ## given image form : ![[image.png|caption]]
                else:
                    caption = caption_or_size
                    captionTag = f"<figcaption>{caption}</figcaption>"

                if sizeTags != "":
                    markdown_image_link += f"{{ {sizeTags} }}"

            replaced_image_link = cleandoc(f"""
                <figure markdown>
                  {markdown_image_link}
                  {captionTag}
                </figure markdown>
            """)

        return replaced_image_link


def is_size(tag: str) -> bool:
    return all(s.isnumeric() for s in tag.split('x'))

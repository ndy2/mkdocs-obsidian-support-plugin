from obsidian_support.abstract_conversion import AbstractConversion, SyntaxGroup
from mkdocs.structure.pages import Page

"""
a strategy that convert obsidian #tags (refer https://help.obsidian.md/Editing+and+formatting/Tags)
to **tags**{: .hash} (refer https://python-markdown.github.io/extensions/attr_list/) in markdown
"""

OBSIDIAN_TAGS_REGEX = "(?<!\\)#(?P<tags>[\w\-_\/]+)(?![^\[\(`]*[\]\)`])"
OBSIDIAN_TAGS_REGEX_GROUPS = ['tags']


class TagsConvert(AbstractConversion):
    def __init__(self):
        super().__init__(OBSIDIAN_TAGS_REGEX, OBSIDIAN_TAGS_REGEX_GROUPS)

    def convert(self, syntax_groups: SyntaxGroup, page: Page) -> str:
        return convert_tags(*syntax_groups)


def convert_tags(tags: str) -> str:
    return "**" + tags + "**{: .hash}"

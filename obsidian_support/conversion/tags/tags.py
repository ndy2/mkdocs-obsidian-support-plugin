import re

from mkdocs.structure.pages import Page
from overrides import override

from obsidian_support.conversion.abstract_conversion import AbstractConversion, SyntaxGroup

"""
a strategy that convert obsidian #tags (refer https://help.obsidian.md/Editing+and+formatting/Tags)
to **tags**{: .hash} (refer https://python-markdown.github.io/extensions/attr_list/) in markdown
"""


class TagsConversion(AbstractConversion):

    @property
    @override
    def obsidian_regex_pattern(self):
        # OBSIDIAN_TAGS_REGEX
        return re.compile(r"(?<!\\)#(?P<tags>[\w\-_\/]+)(?![^\[\(]*[\]\)])")

    @override
    def convert(self, syntax_groups: SyntaxGroup, page: Page, depth: int) -> str:
        return self._convert_tags(*syntax_groups)

    def _convert_tags(self, tags: str) -> str:
        return "**" + tags + "**{: .hash}"

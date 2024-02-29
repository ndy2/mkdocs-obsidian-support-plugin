import re

from mkdocs.structure.pages import Page
from overrides import override

from obsidian_support.conversion.abstract_conversion import AbstractConversion, SyntaxGroup


class TabsBackquotesConversion(AbstractConversion):

    @property
    @override
    def obsidian_regex_pattern(self):
        # OBSIDIAN_HTML_BACKQUOTES_TAB_REGEX
        return re.compile(r"""
        (?:^|[\r\n])                             # admonition must starts with `\n` or in the beginning of markdown
        ```tabs\n                                # admonition type
        (?P<contents>((?!```).*\n)*)             # admonition contents
        ```
        """, flags=re.VERBOSE)

    @override
    def convert(self, syntax_groups: SyntaxGroup, page: Page) -> str:
        print(syntax_groups)
        return self._create_content_tabs(*syntax_groups)

    def _create_content_tabs(self, contents) -> str:
        return "WIP"

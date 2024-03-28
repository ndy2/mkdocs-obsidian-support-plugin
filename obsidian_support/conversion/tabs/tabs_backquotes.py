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
        (?P<place>^|[\r\n])                      # tab must starts with `\n` or in the beginning of markdown
        ```tabs\n                                # tab code block
        (?P<tabs>((?!```).*\n)*)                 # tabs
        ```
        """, flags=re.VERBOSE)

    @override
    def convert(self, syntax_groups: SyntaxGroup, page: Page, depth: int) -> str:
        return self._create_content_tabs(*syntax_groups)

    def _create_content_tabs(self, place, tabs) -> str:
        content_tabs = ""
        tabs = tabs.split("---tab ")[1:]
        for tab in tabs:
            index_of_newline = tab.find("\n")
            tab_label = tab[:index_of_newline]
            tab_content = tab[index_of_newline:-1]
            tab_content = tab_content.replace("\n", "\n    ")
            content_tabs += "=== \"" + tab_label + "\"\n" + tab_content + "\n"
        return place + content_tabs[:-1]

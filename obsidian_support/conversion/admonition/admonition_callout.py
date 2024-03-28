import re

from mkdocs.structure.pages import Page
from overrides import override

from obsidian_support.conversion.abstract_conversion import AbstractConversion, SyntaxGroup

"""
A strategy that convert [obsidian callout](https://help.obsidian.md/Editing+and+formatting/Callouts)
to [mkdocs-material admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)

Examples:
given : 
```
> [!note]
> some note!
```

converted :
```
! note

    some note!
```
"""


class AdmonitionCalloutConversion(AbstractConversion):
    @property
    @override
    def obsidian_regex_pattern(self):
        # OBSIDIAN_CALL_OUT_REGEX
        return re.compile(r"""
        (?P<place>^|[\r\n])                 # callout must starts with `\n` or in the beginning of markdown
        [ ]?>[ ]?\[!(?P<type>[A-Za-z]+)]    # callout type
        (?P<collapse>\+|-?)                 # callout collapse (optional) - add `+` or `-` to make foldable callout 
        (?P<title>[ ].*)?                   # callout title (optional)
        (?P<contents>(\n[ ]?>.*)*)?         # callout contents
        """, flags=re.VERBOSE)

    @override
    def convert(self, syntax_groups: SyntaxGroup, page: Page, depth: int) -> str:
        return self._create_admonition(page, depth, *syntax_groups)

    def _create_admonition(self, page: Page, depth: int, place: str, ad_type: str, collapse: str, title: str,
                           contents: str) -> str:
        contents = contents.replace("\n> ", "\n    ")
        contents = contents.replace("\n > ", "\n    ")
        contents = contents.replace("\n>", "\n    ")
        contents = contents.replace("\n >", "\n    ")

        if title is None:
            title = ""
        else:
            title = ' \"' + title[1:] + '\"'

        if collapse == "+":
            collapse = "???+ "
        elif collapse == "-":
            collapse = "??? "
        else:
            collapse = "!!! "

        de_indented_contents = self._de_indent(contents)
        contents = self.markdown_convert(de_indented_contents, page, depth)
        re_indented_contents = self._indent(depth + 1, contents)

        admonition = place + collapse + ad_type + title + "\n" + re_indented_contents
        return admonition

    def _de_indent(self, contents: str) -> str:
        contents = contents.replace("\n    ", "\n")
        return contents

    def _indent(self, depth: int, contents: str) -> str:
        indent = " " * 4 * depth
        contents = contents.replace("\n", "\n" + indent)
        return contents

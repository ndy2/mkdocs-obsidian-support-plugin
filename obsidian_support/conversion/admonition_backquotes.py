import re

from mkdocs.structure.pages import Page
from overrides import override

from obsidian_support.abstract_conversion import AbstractConversion, SyntaxGroup

"""
a strategy that convert [obsidian block-styled admonition](https://github.com/javalent/admonitions)
to [mkdocs-material admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)
"""


class AdmonitionBackquotesConversion(AbstractConversion):

    @property
    @override
    def obsidian_regex_pattern(self):
        # OBSIDIAN_ADMONITION_REGEX (CALLOUT)
        return re.compile(r"""
        ```(ad-(?P<type>[a-z-]+))\n              # callout type
        ((title:[ ](?P<title>[^\n]+))\n)?        # callout title (optional)
        ((collapse:[ ](?P<collapse>[^\n]+))\n)?  # callout collapse (optional) - add `closed` or `open` to make foldable callout
        (?P<contents>((?!```).*\n)*)             # callout contents
        ```
        """, flags=re.VERBOSE)

    @override
    def convert(self, syntax_groups: SyntaxGroup, page: Page) -> str:
        return self._create_admonition(*syntax_groups)

    def _create_admonition(self, ad_type: str, title: str, collapse: str, contents: str) -> str:
        contents = contents.strip()
        contents = "    " + contents.replace("\n", "\n    ")

        if title is None:
            title = ""
        else:
            title = ' \"' + title + '\"'

        if collapse == "closed":
            collapse = '???'
        elif collapse == "open":
            collapse = '???+'
        else:
            collapse = "!!!"

        admonition = collapse + " " + ad_type + title + "\n\n" + contents
        return admonition

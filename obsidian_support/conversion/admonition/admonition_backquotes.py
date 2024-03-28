import re

from mkdocs.structure.pages import Page
from overrides import override

from obsidian_support.conversion.abstract_conversion import AbstractConversion, SyntaxGroup

"""
A strategy that convert [obsidian block-styled admonition](https://github.com/javalent/admonitions)
to [mkdocs-material admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)

Examples:
given : 
```
```ad-tip
Line 1: This is the content of the admonition tip.
Line 2: This is the content of the admonition tip.
Line 3: This is the content of the admonition tip.
```
```

converted :
```
!!! tip

    Line 1: This is the content of the admonition tip.
    Line 2: This is the content of the admonition tip.
    Line 3: This is the content of the admonition tip.
```
"""


class AdmonitionBackquotesConversion(AbstractConversion):

    @property
    @override
    def obsidian_regex_pattern(self):
        # OBSIDIAN_ADMONITION_REGEX (CALLOUT)
        return re.compile(r"""
        (?P<place>^|[\r\n])                      # admonition must starts with `\n` or in the beginning of markdown
        ```(ad-(?P<type>[A-Za-z]+))\n            # admonition type
        ((title:[ ](?P<title>[^\n]+))\n)?        # admonition title (optional)
        ((collapse:[ ](?P<collapse>[^\n]+))\n)?  # admonition collapse (optional) - add `closed` or `open` to make it collapsible
        (?P<contents>((?!```).*\n)*)             # admonition contents
        ```
        """, flags=re.VERBOSE)

    @override
    def convert(self, syntax_groups: SyntaxGroup, page: Page, depth: int) -> str:
        return self._create_admonition(*syntax_groups)

    def _create_admonition(self, place, ad_type: str, title: str, collapse: str, contents: str) -> str:
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

        admonition = place + collapse + " " + ad_type + title + "\n\n" + contents
        return admonition

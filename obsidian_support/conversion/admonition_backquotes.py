from mkdocs.structure.pages import Page

from obsidian_support.abstract_conversion import AbstractConversion, SyntaxGroup

"""
a strategy that convert [obsidian block-styled admonition](https://github.com/javalent/admonitions)
to [mkdocs-material admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)
"""

OBSIDIAN_CALL_OUT_REGEX = r"""
    ```(ad-(?P<type>[a-z-]+))\n              # callout type
    ((title:[ ](?P<title>[^\n]+))\n)?        # callout title (optional)
    ((collapse:[ ](?P<collapse>[^\n]+))\n)?  # callout collapsable (optional) - add `closed` or `open` to make foldable callout
    (?P<contents>((?!```).*\n)*)             # callout contents
    ```
"""
OBSIDIAN_CALL_OUT_REGEX_GROUPS = ['type', 'title', 'collapse', 'contents']


class AdmonitionBackquotesConvert(AbstractConversion):
    def __init__(self):
        super().__init__(OBSIDIAN_CALL_OUT_REGEX, OBSIDIAN_CALL_OUT_REGEX_GROUPS)

    def convert(self, syntax_groups: SyntaxGroup, page: Page) -> str:
        return create_admonition(*syntax_groups)


def create_admonition(ad_type: str, title: str, collapse: str, contents: str) -> str:
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

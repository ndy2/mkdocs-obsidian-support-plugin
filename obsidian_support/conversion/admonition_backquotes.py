from obsidian_support.abstract_conversion import AbstractConversion, SyntaxGroup
from mkdocs.structure.pages import Page

"""
a strategy that convert [obsidian block-styled admonition](https://github.com/javalent/admonitions)
to [mkdocs-material admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)
"""

OBSIDIAN_CALL_OUT_REGEX = r"```(ad-(?P<type>[a-z-]+))\n((title: (?P<title>[^\n]+))\n)?((collapse: (?P<collapse>[^\n]+))\n)?(?P<lines>((?!```).*\n)*)```"
OBSIDIAN_CALL_OUT_REGEX_GROUPS = ['type', 'title', 'collapse', 'lines']


class AdmonitionBackquotesConvert(AbstractConversion):
    def __init__(self):
        super().__init__(OBSIDIAN_CALL_OUT_REGEX, OBSIDIAN_CALL_OUT_REGEX_GROUPS)

    def convert(self, syntax_groups: SyntaxGroup, page: Page) -> str:
        return create_admonition(*syntax_groups)


def create_admonition(ad_type: str, title: str, collapse: str, lines: str) -> str:
    if title is None:
        title = ""
    else:
        title = '"'+ title + '"'

    if collapse == "closed":
        collapse = '??? '
    elif collapse == "open":
        collapse = '???+ '
    else:
        collapse = "!!! "

    lines = lines.replace("\n", "\n\n    ")

    admonition = "\n"+ collapse + ad_type + ' ' + title + "\n    " + lines
    return admonition

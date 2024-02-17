from mkdocs.structure.pages import Page

from obsidian_support.abstract_conversion import AbstractConversion, SyntaxGroup

"""
a strategy that convert [obsidian callout](https://help.obsidian.md/Editing+and+formatting/Callouts)
to [mkdocs-material admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)
"""

OBSIDIAN_CALL_OUT_REGEX = r"""
    \n[ ]?>[ ]?                     # callout must starts with `\n` and `>`
    \[!(?P<type>[a-z]+)\]           # callout type
    (?P<collapsable>\+|\-?)         # callout collapsable (optional) - add `+` or `-` to make foldable callout 
    (?P<title>[ ].*)?               # callout title (optional)
    (?P<contents>(\n[ ]?>.*)*)      # callout contents
"""
OBSIDIAN_CALL_OUT_REGEX_GROUPS = ['type', 'collapsable', 'title', 'contents']


class AdmonitionConvert(AbstractConversion):
    def __init__(self):
        super().__init__(OBSIDIAN_CALL_OUT_REGEX, OBSIDIAN_CALL_OUT_REGEX_GROUPS)

    def convert(self, syntax_groups: SyntaxGroup, page: Page) -> str:
        return create_admonition(*syntax_groups)


def create_admonition(ad_type: str, collapsable: str, title: str, contents: str) -> str:
    contents = contents.replace("\n> ", "\n    ")
    contents = contents.replace("\n > ", "\n    ")
    contents = contents.replace("\n>", "\n    ")
    contents = contents.replace("\n >", "\n    ")

    if title is None:
        title = ""
    else:
        title = ' \"' + title[1:] + '\"'

    # issue #4 collapsible admonitions from Obsidian syntax
    # https://github.com/ndy2/mkdocs-obsidian-support-plugin/issues/4
    if collapsable == "+":
        ad_syntax_type = "???+ "
    elif collapsable == "-":
        ad_syntax_type = "??? "
    else:
        ad_syntax_type = "!!! "

    admonition = "\n" + ad_syntax_type + ad_type + title + "\n" + contents
    return admonition

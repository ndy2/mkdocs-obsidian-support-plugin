from obsidian_support.abstract_conversion import AbstractConversion, SyntaxGroup

"""
a strategy that convert [obsidian format your code#highlighting](https://help.obsidian.md/How+to/Format+your+notes#Highlighting)
to [mkdocs-material highlighting text](https://squidfunk.github.io/mkdocs-material/reference/formatting/?h=highlight#highlighting-text)
"""

OBSIDIAN_TEXT_HIGHLIGHT_REGEX = '==(?P<content>[\\s\\S]*?)=='
OBSIDIAN_TEXT_HIGHLIGHT_REGEX_GROUP = ['content']


class TextHighlightingConvert(AbstractConversion):
    def __init__(self):
        super().__init__(OBSIDIAN_TEXT_HIGHLIGHT_REGEX, OBSIDIAN_TEXT_HIGHLIGHT_REGEX_GROUP)

    def convert(self, syntax_groups: SyntaxGroup) -> str:
        return create_mkdocs_highlight_text(*syntax_groups)


def create_mkdocs_highlight_text(content: str) -> str:
    return f'{{=={content}==}}'

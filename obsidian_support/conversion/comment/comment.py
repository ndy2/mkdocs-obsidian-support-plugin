import re

from mkdocs.structure.pages import Page
from overrides import override

from obsidian_support.conversion.abstract_conversion import AbstractConversion, SyntaxGroup

"""
A strategy that convert [obsidian comments](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#Comments) 
to [HTML Comment Tag](https://www.w3schools.com/tags/tag_comment.asp)

Examples:
given : `This is an %%inline%% comment.` 
converted : `This is an <!--inline--> comment.`
"""


class CommentConversion(AbstractConversion):

    @property
    @override
    def obsidian_regex_pattern(self):
        # OBSIDIAN_COMMENT_REGEX
        return re.compile(r"%%(?P<comment>[\S\s]*?)%%")

    @override
    def convert(self, syntax_groups: SyntaxGroup, page: Page, depth: int) -> str:
        return self._convert_comment(*syntax_groups)

    def _convert_comment(self, comment):
        return f"<!--{comment}-->"

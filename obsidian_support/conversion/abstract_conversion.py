from abc import *
from typing import List

from mkdocs.structure.pages import Page
from overrides import final

from obsidian_support.conversion.util import is_overlapped, get_exclude_indices

"""
An abstract class that implies a conversion from `obsidian syntax` to `mkdocs-material syntax`

It contains
 - self.obsidian_regex : an regex that implies `obsidian syntax`
 - @abstractmethod convert : an abstract method that convert `obsidian syntax` to `mkdocs-material syntax`

Every conversion should extends this class
"""

# a list of string that implies the syntax groups in regex
SyntaxGroup = List[str]


class AbstractConversion(metaclass=ABCMeta):

    @property
    @abstractmethod
    def obsidian_regex_pattern(self):
        pass

    @property
    @final
    def obsidian_regex_groups(self):
        return list(self.obsidian_regex_pattern.groupindex.keys())

    @abstractmethod
    def convert(self, syntax_groups: SyntaxGroup, page: Page, depth: int) -> str:
        pass

    """
    A template method that applies conversion for every regex matches
    """

    def markdown_convert(self, markdown: str, page: Page, depth: int = 0) -> str:
        converted_markdown = ""
        index = 0
        excluded_indices = get_exclude_indices(markdown)

        for obsidian_syntax in self.obsidian_regex_pattern.finditer(markdown):
            # find range of markdown where the obsidian_regex matches
            start = obsidian_syntax.start()
            end = obsidian_syntax.end() - 1

            # continue if match is in excluded range
            if is_overlapped(start, end, excluded_indices):
                continue

            syntax_groups = list(map(lambda group: obsidian_syntax.group(group), self.obsidian_regex_groups))

            mkdocs_syntax = self.convert(syntax_groups, page, depth)
            converted_markdown += markdown[index:start]
            converted_markdown += mkdocs_syntax
            index = end + 1

        converted_markdown += markdown[index:len(markdown)]
        return converted_markdown

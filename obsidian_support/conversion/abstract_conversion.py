import re
from abc import *
from enum import Enum
from typing import List, Tuple

from mkdocs.structure.pages import Page
from overrides import final

"""
An abstract class that implies a conversion from `obsidian syntax` to `mkdocs-material syntax`

It contains
 - self.obsidian_regex : an regex that implies `obsidian syntax`
 - @abstractmethod convert : an abstract method that convert `obsidian syntax` to `mkdocs-material syntax`

Every conversion should extends this class
"""

# a list of string that implies the syntax groups in regex
SyntaxGroup = List[str]


class MarkdownPatterns(Enum):
    # Exclude Patterns
    """ regex that matches markdown `tilde code block` (triple tilde syntax)"""
    TILDE_CODE_BLOCK = r"([A-Za-z \t]*)~~~([-A-Za-z]*)?\n([\s\S]*?)~~~([A-Za-z \t]*)*"

    """regex that matches markdown `backtick code block` (triple backtick syntax)"""
    BACKTICK_CODE_BLOCK = r"([A-Za-z \t]*)```([-A-Za-z]*)?\n([\s\S]*?)```([A-Za-z \t]*)*"

    """regex that matches markdown code (single backtick syntax)"""
    BACKTICK_CODE = r"`[\S\s]*?`"

    # Do Not Exclude Patterns
    """regex that matches markdown `admonition backquotes` (triple tilde syntax)"""
    ADMONITION_BACKQUOTES_CODE_BLOCK = r"([A-Za-z \t]*)```ad-([-A-Za-z]*)?\n([\s\S]*?)```([A-Za-z \t]*)*"

    """regex that matches markdown `tabs backquotes code block` (triple tilde syntax)"""
    TABS_BACKQUOTES_CODE_BLOCK = r"([A-Za-z \t]*)```tabs([-A-Za-z]*)?\n([\s\S]*?)```([A-Za-z \t]*)*"

    """regex that matches markdown `tabs tilde code block` (triple tilde syntax)"""
    TABS_TILDE_CODE_BLOCK = r"([A-Za-z \t]*)~~~tabs([-A-Za-z]*)?\n([\s\S]*?)~~~([A-Za-z \t]*)*"

    @property
    def regex(self):
        return self.value


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
    def convert(self, syntax_groups: SyntaxGroup, page: Page) -> str:
        pass

    """
    A template method that applies conversion for every regex matches
    """

    def markdown_convert(self, markdown: str, page: Page) -> str:
        converted_markdown = ""
        index = 0
        excluded_indices = self._get_excluded_indices(markdown)
        excluded_indices = self._filter_do_not_exclude_indices(excluded_indices, markdown)

        for obsidian_syntax in self.obsidian_regex_pattern.finditer(markdown):
            ## found range of markdown where the obsidian_regex matches
            start = obsidian_syntax.start()
            end = obsidian_syntax.end() - 1

            ## continue if match is in excluded range
            if self._is_overlapped(start, end, excluded_indices):
                continue

            syntax_groups = list(map(lambda group: obsidian_syntax.group(group), self.obsidian_regex_groups))

            mkdocs_syntax = self.convert(syntax_groups, page)
            converted_markdown += markdown[index:start]
            converted_markdown += mkdocs_syntax
            index = end + 1

        converted_markdown += markdown[index:len(markdown)]
        return converted_markdown

    @staticmethod
    def _get_excluded_indices(markdown: str) -> List[tuple]:
        tilde_code_block_indices = []
        for code in re.finditer(MarkdownPatterns.TILDE_CODE_BLOCK.regex, markdown):
            tilde_code_block_indices.append((code.start(), code.end() - 1))

        backtick_code_block_indices = []
        for code in re.finditer(MarkdownPatterns.BACKTICK_CODE_BLOCK.regex, markdown):
            if not AbstractConversion._is_overlapped(code.start(), code.end() - 1, tilde_code_block_indices):
                backtick_code_block_indices.append((code.start(), code.end() - 1))

        backtick_code_indices = []
        for code in re.finditer(MarkdownPatterns.BACKTICK_CODE.regex, markdown):
            if not AbstractConversion._is_overlapped(code.start(), code.end() - 1, tilde_code_block_indices) and \
                    not AbstractConversion._is_overlapped(code.start(), code.end() - 1, backtick_code_block_indices):
                backtick_code_indices.append((code.start(), code.end() - 1))

        return tilde_code_block_indices + backtick_code_block_indices + backtick_code_indices

    @staticmethod
    def _filter_do_not_exclude_indices(exclude_indices: List[Tuple], markdown) -> List[Tuple]:
        admonition_backquotes_code_block_indices = []
        for code in re.finditer(MarkdownPatterns.ADMONITION_BACKQUOTES_CODE_BLOCK.regex, markdown):
            admonition_backquotes_code_block_indices.append((code.start(), code.end() - 1))

        tabs_backquotes_code_block_indices = []
        for code in re.finditer(MarkdownPatterns.TABS_BACKQUOTES_CODE_BLOCK.regex, markdown):
            tabs_backquotes_code_block_indices.append((code.start(), code.end() - 1))

        tabs_tilde_code_block_indices = []
        for code in re.finditer(MarkdownPatterns.TABS_TILDE_CODE_BLOCK.regex, markdown):
            tabs_tilde_code_block_indices.append((code.start(), code.end() - 1))

        do_not_exclude_indices = admonition_backquotes_code_block_indices + tabs_backquotes_code_block_indices + tabs_tilde_code_block_indices
        return list(filter(lambda indices: indices not in do_not_exclude_indices, exclude_indices))

    @staticmethod
    def _is_overlapped(start: int, end: int, exclude_indices_pairs: List[tuple]) -> bool:
        for exclude_indices_pair in exclude_indices_pairs:
            if exclude_indices_pair[0] <= start and end <= exclude_indices_pair[1]:
                return True
        return False

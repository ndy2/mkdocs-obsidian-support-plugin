import re
from typing import List

from mkdocs.structure.pages import Page

from obsidian_support.conversion.abstract_conversion import AbstractConversion

"""
A template method that applies conversion for every regex matches
"""


def markdown_convert(markdown: str, page: Page, conversion: AbstractConversion) -> str:
    converted_markdown = ""
    index = 0
    excluded_indices = _get_excluded_indices(markdown)

    for obsidian_syntax in conversion.obsidian_regex_pattern.finditer(markdown):
        ## found range of markdown where the obsidian_regex matches
        start = obsidian_syntax.start()
        end = obsidian_syntax.end() - 1

        ## continue if match is in excluded range
        if _is_excluded(start, end, excluded_indices):
            continue

        syntax_groups = list(map(lambda group: obsidian_syntax.group(group), conversion.obsidian_regex_groups))

        mkdocs_syntax = conversion.convert(syntax_groups, page)
        converted_markdown += markdown[index:start]
        converted_markdown += mkdocs_syntax
        index = end + 1

    converted_markdown += markdown[index:len(markdown)]
    return converted_markdown


def _get_excluded_indices(markdown: str) -> List[tuple]:
    indices = []
    """ regex that matches markdown `code block` (triple backtick syntax) and code(single backtick syntax) """
    MARKDOWN_CODE_REGEX = r"`[\S\s]*?`"

    for code in re.finditer(MARKDOWN_CODE_REGEX, markdown):
        indices.append((code.start(), code.end() - 1))
    return indices


def _is_excluded(start: int, end: int, exclude_indices_pairs: List[tuple]) -> bool:
    for exclude_indices_pair in exclude_indices_pairs:
        if exclude_indices_pair[0] <= start and end <= exclude_indices_pair[1]:
            return True
    return False

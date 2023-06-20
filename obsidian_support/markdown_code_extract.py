import re

from typing import List

EXCLUDE_RANGES = List[tuple]

""" regex that matches markdown `code block` (triple backtick syntax) and code(single backtick syntax) """
MARKDOWN_CODE_REGEX = r'`(?!ad-).*?`'


def get_code_indices(markdown: str) -> EXCLUDE_RANGES:
    indices = []
    for code in re.finditer(MARKDOWN_CODE_REGEX, markdown):
        indices.append((code.start(), code.end()-1))

    return indices
